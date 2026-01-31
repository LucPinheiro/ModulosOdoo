# -*- coding: utf-8 -*-
{
    "name": "TMS - Transport Management System (Community)",
    "version": "17.0.1.0.0",
    "category": "Operations",
    "summary": "Rutas, solicitudes, viajes, facturación, portal conductor (sin Fleet)",
    "author": "Tu Empresa",
    "depends": [
        "base",
        "mail",
        "sale_management",
        "account",
        "portal",
        "website",
    ],
    "data": [
        "security/security.xml",
        "security/ir.model.access.csv",
        "data/sequence.xml",
        "views/tms_vehicle_views.xml",
        "views/tms_route_views.xml",
        "views/tms_request_views.xml",
        "views/tms_trip_views.xml",
        "views/tms_mileage_views.xml",
        "views/sale_order_views.xml",
        "views/tms_menus.xml"
    ],
    "qweb": [
    "portal/templates.xml"
    ],
    "application": True,
    "license": "LGPL-3",
}
