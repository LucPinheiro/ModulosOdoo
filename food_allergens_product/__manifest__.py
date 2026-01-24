# © 2024 Forgar (<https://fogardosantiso.es/>)
# License LGPL-3 - See http://www.gnu.org/licenses/lgpl-3.0.html

{
    "name": "Food Allergens",
    "summary": """
        Add food allergens in product and Manufacturing Orders form view
    """,
    "author": "Fogar Consultores, S.L.",
    "license": "LGPL-3",
    "version": "17.0.1.0.0",
    "category": "Stock/Stock",
    "website": "https://fogardosantiso.es/",
    "depends": [
        "stock","account","mrp"],
    "data": [
        "security/ir.model.access.csv",
        "views/product_views.xml",
        "views/mrp_production_views.xml",
        "views/food_allergens_views.xml",
        "views/menu.xml",
    ],
    'installable': True,
}
