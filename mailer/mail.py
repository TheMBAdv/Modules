from msilib import sequence
import smtplib, ssl

def mailText(SENDER_MAIL: str, PASSWORD: str, receiver_email: list, asunto: str, texto_mensaje: str, SMTP: str, PORT: int, CC: list):
    
    message = f"""\
From: {SENDER_MAIL} 
To: {receiver_email}
Subject: {asunto}
CC:{CC}

{texto_mensaje}"""

    context = ssl.create_default_context()
    
    receiver_email.append(CC)
    
    with smtplib.SMTP_SSL(SMTP, PORT, context=context) as server:
        server.login(SENDER_MAIL, PASSWORD)
        server.sendmail(SENDER_MAIL, receiver_email, message)
    
    return True






