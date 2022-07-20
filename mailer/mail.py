import smtplib, ssl

def mailText(SENDER_MAIL: str, PASSWORD: str, receiver_email: str, asunto: str, texto_mensaje: str, SMTP: str, PORT: int):
    message = f"""\
From: {SENDER_MAIL} 
To: {receiver_email}
Subject: {asunto}

{texto_mensaje}"""
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(SMTP, PORT, context=context) as server:
        server.login(SENDER_MAIL, PASSWORD)
        server.sendmail(SENDER_MAIL, receiver_email, message)
        
mailText("informatica@kingregal.com", "8x9J9b~n", "informatica@kingregal.com", "hola", "Esto es una prueba", "mail.aws.cloud-services.es", 465)