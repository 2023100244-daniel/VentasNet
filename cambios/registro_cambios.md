# Registro de cambios

**Proyecto:** VentasNet  
**Versión base:** v1.0.0  
**Estado:** Solicitudes evaluadas

---

## 1. Solicitud INC-001

| Campo | Descripción |
|---|---|
| ID | INC-001 |
| Origen | Reporte de error detectado en el sistema |
| Descripción | El cálculo del total de una venta no considera la cantidad de productos adquiridos. |
| Justificación | El sistema muestra un importe incorrecto cuando se compran varias unidades. |
| Requisito afectado | RF-001 |
| Archivos involucrados | src/ventas.py |
| Riesgo | Mostrar totales incorrectos y generar errores en las ventas. |
| Criterio de aceptación | Al ingresar precio S/ 50 y cantidad 3, el sistema debe mostrar S/ 150. |
| Prioridad | Alta |
| Decisión | Aprobada |
| Responsable | Desarrollador del proyecto |

## 2. Solicitud CR-002

| Campo | Descripción |
|---|---|
| ID | CR-002 |
| Origen | Solicitud del área comercial |
| Descripción | Incorporar un descuento del 10 % cuando el subtotal sea igual o superior a S/ 200. |
| Justificación | Ofrecer descuentos a los clientes que realicen compras de mayor importe. |
| Requisito afectado | RF-002 (nuevo) |
| Archivos involucrados | src/ventas.py y docs/requisitos.md |
| Riesgo | Aplicar descuentos incorrectos cuando el subtotal alcance el importe mínimo. |
| Criterio de aceptación | Subtotal S/ 200 → S/ 180; subtotal S/ 150 → S/ 150. |
| Prioridad | Media |
| Decisión | Aprobada |
| Responsable | Desarrollador del proyecto |

---

## 3. Matriz de evaluación de impacto

| Criterio | INC-001 | CR-002 |
|---|---|---|
| Requisito | RF-001 | RF-002 (nuevo) |
| Archivo | src/ventas.py | src/ventas.py; docs/requisitos.md |
| Riesgo | Total incorrecto | Descuento incorrecto en el umbral |
| Prueba | 50 × 3 = 150 | Subtotales 150, 200 y 300 |
| Decisión simulada | Aprobada | Aprobada |

## 4. Registro de aprobación académica

Se realizó una evaluación simulada de las solicitudes INC-001 y CR-002.

Ambas solicitudes fueron aprobadas para su implementación, debido a que permiten corregir un defecto existente y mejorar las funcionalidades del sistema de ventas.

La implementación se realizará de manera independiente mediante ramas Git, conservando la trazabilidad de cada modificación.

**Estado de aprobación:**
- INC-001: Aprobada.
- CR-002: Aprobada.

**Responsable:** Desarrollador del proyecto.