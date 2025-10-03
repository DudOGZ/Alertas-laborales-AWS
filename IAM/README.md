# IAM – Política mínima para Lambda  
**IAM – Minimal policy for Lambda**

---

## 📌 Propósito / Purpose

Este directorio contiene la política de permisos (`policy.json`) necesaria para que la función Lambda del sistema de alertas laborales pueda:

- Enviar correos electrónicos mediante Amazon SES  
- Registrar eventos y errores en CloudWatch Logs

This directory contains the permission policy (`policy.json`) required for the Lambda function in the job alert system to:

- Send emails via Amazon SES  
- Log events and errors to CloudWatch Logs

---

## 📁 Archivos incluidos / Included files

- `policy.json` → Política IAM en formato JSON  
- `README.md` → Documentación bilingüe de la política

---

## 🔐 Detalles de la política / Policy details

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PermitirEnvioSES",
      "Effect": "Allow",
      "Action": "ses:SendEmail",
      "Resource": "*"
    },
    {
      "Sid": "PermitirLogsCloudWatch",
      "Effect": "Allow",
      "Action": [
        "logs:CreateLogGroup",
        "logs:CreateLogStream",
        "logs:PutLogEvents"
      ],
      "Resource": "*"
    }
  ]
}
