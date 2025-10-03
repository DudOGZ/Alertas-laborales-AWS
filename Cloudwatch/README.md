# CloudWatch – Configuración de eventos / Event configuration

---

## 📌 Propósito / Purpose

Esta carpeta contiene la configuración de eventos para activar automáticamente la función Lambda del sistema de alertas laborales.

This folder contains the event configuration to automatically trigger the Lambda function in the job alert system.

---

## 📁 Archivos incluidos / Included files

- `trigger-config.txt` → Expresión `cron` para ejecución semanal

---

## 🕒 Regla de evento / Event rule

**Nombre / Name:** `alertaLaboralTrigger`  
**Expresión / Expression:** `cron(0 8 ? * 3 *)`  
**Descripción / Description:** Ejecuta la función Lambda cada miércoles a las 08:00 UTC (10:00 hora de Madrid)  
**Destino / Target:** Función Lambda (`alertaLaboralHandler`)  
**Finalidad / Purpose:** Revisión semanal de nuevas ofertas laborales según palabras clave definidas por el usuario

---

## 🔗 Asociación / Linking

La expresión `cron` debe asociarse a una **regla de evento en CloudWatch** que tenga como destino la función Lambda.  
Esto puede configurarse desde la consola de AWS o mediante infraestructura como código.

The `cron` expression must be linked to a **CloudWatch event rule** targeting the Lambda function.  
You can configure this via the AWS console or infrastructure as code.

---

## 🧠 Notas / Notes

- La expresión `cron(0 8 ? * 3 *)` representa “cada miércoles a las 08:00 UTC”  
- Puedes modificarla para ajustar frecuencia, día o zona horaria  
- Se recomienda documentar cualquier cambio en `trigger-config.txt` o en esta regla

