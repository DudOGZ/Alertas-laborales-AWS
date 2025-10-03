import boto3
import requests

def lambda_handler(event, context):
    # 1. Definir lista de URLs a monitorizar
    # 1. Define list of URLs to monitor
    urls = [
        "https://ejemplo1.com/ofertas",
        "https://ejemplo2.com/trabajo"
        # Añadir más si es necesario / Add more if needed
    ]

    # 2. Definir palabras clave
    # 2. Define keywords
    keywords = ["Informatica", "sistemas", "redes", "Windows", "tai", "Informática", "informático", "informatico"]

    # 3. Descargar contenido y buscar coincidencias
    # 3. Download content and search for matches
    matches = []
    for url in urls:
        try:
            response = requests.get(url)
            content = response.text.lower()
            for keyword in keywords:
                if keyword.lower() in content:
                    matches.append((url, keyword))
        except Exception as e:
            print(f"Error al acceder a {url}: {e}")
            # Error accessing URL

    # 4. Enviar correo si hay coincidencias
    # 4. Send email if matches are found
    if matches:
        ses = boto3.client('ses')
        body_text = "Se han encontrado coincidencias:\n\n"
        for url, keyword in matches:
            body_text += f"- {keyword} en {url}\n"

        try:
            ses.send_email(
                Source='remitente-verificado@example.com',
                Destination={'ToAddresses': ['destinatario@example.com']},
                Message={
                    'Subject': {'Data': 'Nueva alerta laboral'},
                    'Body': {'Text': {'Data': body_text}}
                }
            )
        except Exception as e:
            print(f"Error al enviar el correo: {e}")
            # Error sending email

    return {"status": "ok", "matches": matches}

