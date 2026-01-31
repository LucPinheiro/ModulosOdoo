# Modulos Personalizados Odoo 14

Módulo FDC: Documento de Captura de Pesca
## Fishing Capture Document (FCD)

Módulo para **Odoo Community / Enterprise** orientado al **sector pesquero**, que permite gestionar el **Documento de Captura de Pesca**, asegurando la trazabilidad del producto desde la captura hasta el inventario.

## 📌 Descripción
Este módulo añade nuevos modelos y funcionalidades para la gestión del Documento de Captura de Pesca, integrándose con Inventario, Compras y Control de Calidad. Facilita el cumplimiento normativo y el control detallado de la información asociada a la captura.

## ⚙️ Funcionalidades principales
- Gestión del **Documento de Captura de Pesca**
- Asociación de documentos a **lotes de inventario**
- Gestión de **Zonas FAO** y **subzonas**
- Registro y filtrado de **buques**
- Integración con **lectura de códigos QR**
- Control de calidad asociado al lote de pesca
- Visualización de datos de captura desde Inventario

## 🧩 Integración con Odoo
- Inventario (`stock`)
- Compras (`purchase`)
- Calidad (`quality`) *(opcional, según configuración)*

## 🐟 Casos de uso
- Empresas del sector pesquero
- Trazabilidad alimentaria
- Control documental de capturas
- Cumplimiento de normativas de pesca y seguridad alimentaria

  
## Módulo stock_move_line_partner_tree
Extiende Odoo Inventory mostrando el cliente/proveedor en la vista árbol de los movimientos de stock (stock.move.line), facilitando la trazabilidad logística.
Muestra el partner en la vista lista de movimientos de stock en Odoo.


## Módulo stock_secondary_unit_stock_quant
Añade soporte de unidad de medida secundaria en los quants de stock, mejorando el control de inventario con múltiples unidades en Odoo.
=======
# Modulos Personalizados Odoo 17

## Módulo TMS (Transport Management System)
Permite gestionar rutas, solicitudes de transporte, viajes, vehículos, conductores, kilometraje y facturación, todo integrado en Odoo.

## Módulo Food Allergens
Permite gestionar y asociar alérgenos alimentarios a los productos, facilitando el control y la información obligatoria sobre alérgenos.

## Módulo Formulario Website RMA
Módulo para Odoo Website, que permite a los clientes solicitar devoluciones y garantías directamente desde el portal web, integrándose con productos, clientes y configuraciones del sistema.


=======
# Modulos ERP Odoo

Este repositorio contiene una colección de módulos personalizados desarrollados para Odoo, orientados a distintas versiones del ERP y a diferentes aplicaciones funcionales. Los módulos están diseñados para ampliar, adaptar y optimizar las funcionalidades estándar de Odoo según necesidades reales de negocio.

El objetivo del repositorio es centralizar desarrollos propios que abarcan áreas como ventas, contabilidad, inventario, CRM, recursos humanos y automatización de procesos, manteniendo una estructura organizada por versión de Odoo para facilitar su mantenimiento y reutilización.

Los módulos están desarrollados siguiendo buenas prácticas de programación en Python y Odoo, con énfasis en la escalabilidad, la claridad del código y la compatibilidad entre versiones. Este repositorio está pensado tanto como portafolio profesional como base de trabajo para proyectos de consultoría, personalización e integración de Odoo en entornos empresariales.

Cada módulo incluye su estructura estándar, dependencias y configuración necesaria para su correcta instalación y uso dentro de Odoo.

## Odoo-14

Módulos en la raíz de la rama: fcd, stock_move_line_partner_tree, stock_secondary_unit_stock_quant.

fcd (Fishing Capture Document): 
Gestión del Documento de Captura de Pesca para trazabilidad en el sector pesquero (lotes, zonas FAO/subzonas, buques, QR, etc.).

stock_move_line_partner_tree: 
Muestra el cliente/proveedor (partner) en la vista lista/árbol de movimientos de stock (stock.move.line) para mejorar trazabilidad logística.

stock_secondary_unit_stock_quant: 
Añade soporte para unidad de medida secundaria en quants de stock (stock.quant) para control con múltiples unidades.

## Odoo-15

## Odoo-16

## Odoo-17

Módulos en la raíz de la rama: food_allergens_product, tms.

tms (Transport Management System): 
Gestión de transporte: rutas, solicitudes, viajes, vehículos, conductores, kilometraje y facturación integrado en Odoo.

food_allergens_product: 
Gestión de alérgenos alimentarios asociados a productos para control e información obligatoria.

## Odoo-18

## Odoo-19
 main

