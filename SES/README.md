# SES – Configuración de notificaciones por correo

## Propósito  
Enviar alertas por correo cuando se detecten coincidencias con palabras clave definidas por el usuario.

## Requisitos  
- Dirección de correo verificada en modo sandbox de SES  
- Permiso IAM: `ses:SendEmail`  
- Integración con Lambda usando `boto3` (SDK de Python)

## Notas  
- SES opera actualmente en modo sandbox  
- Solo los destinatarios verificados pueden recibir correos  
- Versiones futuras podrían incluir formato con plantillas y verificación a nivel de dominio

## Ejemplo

```python
import boto3

ses = boto3.client('ses')

response = ses.send_email(
    Source='remitente-verificado@example.com',
    Destination={'ToAddresses': ['destinatario@example.com']},
    Message={
        'Subject': {'Data': 'Nueva alerta laboral'},
        'Body': {'Text': {'Data': 'Se ha encontrado una coincidencia en una página monitorizada'}}
    }
)



---

### 🇬🇧 English version

```markdown
# SES – Email Notification Setup

## Purpose  
Send email alerts when matches are found based on user-defined keywords.

## Requirements  
- Verified sender email address in SES sandbox mode  
- IAM permission: `ses:SendEmail`  
- Lambda integration using `boto3` (Python SDK)

## Notes  
- SES is currently operating in sandbox mode  
- Only verified recipients can receive emails  
- Future versions may include template-based formatting and domain-level verification

## Example

```python
import boto3

ses = boto3.client('ses')

response = ses.send_email(
    Source='verified-sender@example.com',
    Destination={'ToAddresses': ['recipient@example.com']},
    Message={
        'Subject': {'Data': 'New job alert'},
        'Body': {'Text': {'Data': 'A match was found on a monitored site'}}
    }
)
