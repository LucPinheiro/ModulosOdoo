
{
    "name": "Vitosec Website RMA",
    "sumary": """
        Vitosec Website RMA
    """,
    "author": "Sinerkia iD",
    "license": "AGPL-3",
    "version": "17.0.1.0.0",
    "category": "Website",
    "website": "https://www.sinerkia.com",
    "application": False,
    "installable": True,
    "depends": ["web","rma", "website","sale", "stock"],
    "data": [
        "views/templates.xml",
        "views/rma_views.xml",
        "views/website_rma_portal_templates.xml",
        "data/website_data.xml",


        ],
    'assets': {
        'web.assets_frontend': [
            'owl_website_rma/static/src/components/item/item.js',
            'owl_website_rma/static/src/components/item/item.xml',
            'owl_website_rma/static/src/scss/item_style.scss',
      
        ],
    },

}

