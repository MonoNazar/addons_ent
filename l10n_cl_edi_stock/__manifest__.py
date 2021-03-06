{
    "name": """Chile - E-Invoicing Delivery Guide""",
    'version': '1.0.',
    'category': 'Accounting/Localizations/EDI',
    'sequence': 12,
    'author':  'Blanco Martín & Asociados',
    'description': """
    The delivery guide (guia de despacho) is needed as a proof
    that you are sending goods between A and B.  
    
    It is configurable on the partner if prices are needed on the 
    delivery guide and if they need to come from the sale order 
    or the product itself.  
    
    It is only when a delivery order is validated that you can create the delivery 
    guide.  Then it will follow the same flow as for the invoices, sending it to 
    the SII.  
    """,
    'website': 'http://blancomartin.cl',
    'depends': [
        'sale_stock',
        'l10n_cl_edi',
        ],
    'data': [
        'data/l10n_latam.document.type.csv',
        'template/dte_template.xml',
        'template/dd_template.xml',
        'template/email_template.xml',
        'views/dte_caf_view.xml',
        'views/res_partner_view.xml',
        'views/stock_picking_views.xml',
        'views/report_delivery_guide.xml',
        'views/menuitems.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'auto_install': True,
    'application': False,
}
