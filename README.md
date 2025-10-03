# Sistema de alertas laborales en la nube / Cloud-Based Job Alert System

🛠️ Proyecto en desarrollo / Project in progress

---

## 🇪🇸 Español

Este proyecto personal tiene como objetivo crear un sistema automatizado que detecte nuevas ofertas de trabajo relevantes en páginas web seleccionadas y envíe notificaciones al usuario.

Está siendo desarrollado mediante servicios de **Amazon Web Services (AWS)**, con enfoque en automatización, gestión de eventos y administración segura de recursos cloud.

### Estado del proyecto

- En fase de diseño y pruebas  
- Se irán incorporando componentes progresivamente

### Objetivos

- Aplicar conocimientos adquiridos en formación técnica (ASIR, AWS Educate)  
- Explorar la integración de servicios cloud para automatizar tareas útiles  
- Practicar buenas prácticas de seguridad y eficiencia en entornos AWS

### Autor

**Enrique P.**  
Estudiante de Administración de Sistemas Informáticos en Red (ASIR)  
San Fernando de Henares, Madrid

---

## 🇬🇧 English

This personal project aims to create an automated system that monitors selected websites for new job postings and sends notifications to the user when relevant opportunities appear.

It is being developed using **Amazon Web Services (AWS)**, with a focus on automation, event-driven architecture, and secure cloud resource management.

### Project status

- Currently in design and testing phase  
- Components will be added progressively

### Objectives

- Apply technical knowledge acquired through ASIR and AWS Educate training  
- Explore cloud service integration to automate useful tasks  
- Practice security and efficiency best practices in AWS environments


---

## 🔗 Documentación por módulo / Module documentation

- [Lambda](lambda/README.md) – Lógica de ejecución y filtrado  
- [SES](ses/README.md) – Configuración del servicio de correo  
- [IAM](iam/README.md) – Permisos mínimos para Lambda  
- [CloudWatch](cloudwatch/README.md) – Programación automática con eventos

---

## 📌 Estado actual / Current status

- [x] Estructura del repositorio  
- [x] Función Lambda básica (`main.py`)  
- [x] Política IAM mínima (`policy.json`)  
- [x] Configuración de trigger (`trigger-config.txt`)  
- [x] Documentación bilingüe por módulo  
- [ ] Validación de remitente en SES  
- [ ] Pruebas con páginas reales  
- [ ] Mejora del filtrado por contenido

---

## 🚀 Cómo desplegar / How to deploy

1. Verifica que el remitente esté validado en SES  
2. Asocia la política IAM al rol de Lambda  
3. Configura el trigger en CloudWatch con `trigger-config.txt`  
4. Sube el código a Lambda y prueba manualmente o espera ejecución automática


1. Verify that the sender is validated in SES  
2. Attach the IAM policy to the Lambda role  
3. Configure the CloudWatch trigger using `trigger-config.txt`  
4. Upload the code to Lambda and test manually or wait for automatic execution


---

## 📎 Enlaces útiles / Useful links

- [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html)  
- [Amazon SES](https://docs.aws.amazon.com/ses/latest/dg/send-email.html)  
- [CloudWatch Events](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/WhatIsCloudWatchEvents.html)  
- [IAM Policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html)


