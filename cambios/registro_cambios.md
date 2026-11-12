# Registro de cambios

**Proyecto:** VentasNet  
**Versión base:** v1.0.0

## 1. Solicitud INC-001

| Campo | Descripción |
|---|---|
| ID | INC-001 |
| Origen | Reporte de error detectado en el sistema |
| Descripción | El cálculo del total no consideraba la cantidad de productos. |
| Justificación | El sistema mostraba un importe incorrecto en compras de varias unidades. |
| Requisito afectado | RF-001 |
| Archivos involucrados | src/ventas.py; pruebas/casos_prueba.md |
| Riesgo | Mostrar totales incorrectos. |
| Criterio de aceptación | Precio S/ 50 y cantidad 3 deben producir S/ 150. |
| Prioridad | Alta |
| Decisión | Aprobada |
| Responsable | Desarrollador del proyecto |
| Estado | Implementada y verificada |

## 2. Solicitud CR-002

| Campo | Descripción |
|---|---|
| ID | CR-002 |
| Origen | Solicitud del área comercial |
| Descripción | Incorporar descuento del 10 % cuando el subtotal sea igual o superior a S/ 200. |
| Justificación | Ofrecer descuentos a clientes con compras de mayor importe. |
| Requisito afectado | RF-002 (nuevo) |
| Archivos involucrados | src/ventas.py; docs/requisitos.md |
| Riesgo | Aplicar descuentos incorrectos. |
| Criterio de aceptación | S/ 200 → S/ 180; S/ 150 → S/ 150. |
| Prioridad | Media |
| Decisión | Aprobada |
| Responsable | Desarrollador del proyecto |
| Estado | Aprobada, pendiente de implementación |

## 3. Matriz de evaluación de impacto

| Criterio | INC-001 | CR-002 |
|---|---|---|
| Requisito | RF-001 | RF-002 (nuevo) |
| Archivo | src/ventas.py | src/ventas.py; docs/requisitos.md |
| Riesgo | Total incorrecto | Descuento incorrecto en umbral |
| Prueba | 50 × 3 = 150 | Subtotales 150, 200 y 300 |
| Decisión | Aprobada | Aprobada |

## 4. Seguimiento de implementación

### INC-001
- Rama: fix/INC-001-total
- Commit: INC-001: corregir calculo por cantidad
- Integración: merge --no-ff a main
- Prueba: S/ 50 × 3 = S/ 150
- Estado: Implementada y verificada

### CR-002
- Rama prevista: feature/CR-002-descuento
- Estado: Aprobada, pendiente de implementación

## 5. Aprobación académica

Las solicitudes INC-001 y CR-002 fueron aprobadas para su implementación. La primera fue corregida y verificada satisfactoriamente. La segunda queda pendiente para la siguiente fase.