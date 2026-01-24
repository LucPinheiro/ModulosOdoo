# Modulos Personalziados Odoo 14

Módulo FDC: Documento de Captura de Pesca
# Fishing Capture Document (FCD)

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

  
Módulo stock_move_line_partner_tree
Extiende Odoo Inventory mostrando el cliente/proveedor en la vista árbol de los movimientos de stock (stock.move.line), facilitando la trazabilidad logística.
Muestra el partner en la vista lista de movimientos de stock en Odoo.


Módulo stock_secondary_unit_stock_quant
Añade soporte de unidad de medida secundaria en los quants de stock, mejorando el control de inventario con múltiples unidades en Odoo.
