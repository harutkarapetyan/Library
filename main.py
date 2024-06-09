# FastAPI
import time
from fastapi import FastAPI, status
from fastapi.responses import JSONResponse

# SQL - postgres
import psycopg2
from psycopg2.extras import RealDictCursor


from database import engine
from models.models import Base

from routers.auth import auth_router
from routers.forgot_password import forgot_router
from routers.settings import setting_router


Base.metadata.create_all(bind=engine)

while True:
    try:
        conn = psycopg2.connect(
            host='127.0.0.1',
            port=5432,
            database='post_blog',
            user='postgres',
            password='password',
            cursor_factory=RealDictCursor
            )
        print("Connection successfully")

        cursor = conn.cursor()
        break
    except Exception as error:
        print(error)
        time.sleep(3)


app = FastAPI()


@app.get("/")
def main():
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "OK"})


app.include_router(auth_router)
app.include_router(setting_router)
app.include_router(forgot_router)
