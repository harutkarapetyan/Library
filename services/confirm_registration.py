
from services.service_email import send_email

subject = "Confirm Registration"

URL = "http://127.0.0.1:8000/mail_verification"

body = f"""Dear user,
            Thank you for creating your account.
            Please confirm your email address. The confirmation code is:
          {URL}

          If you have not requested a verification code, you can safely ignore this email․
          """

recipients = []


sender = "harut.karapetyan.2022@gmail.com"

password = "dzok bydv rbqw lsab"


def mail_verification_email(email):
    recipients.append(email)
    send_email(subject, body, sender, recipients, password)






