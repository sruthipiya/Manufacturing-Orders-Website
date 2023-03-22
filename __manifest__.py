{
    'name': 'Manufacturing Orders',
    'description': 'Manufacturing orders in website',
    'sequence': 0,
    'installable': True,
    'application': True,
    'depends': ['base', 'mrp', 'contacts', 'website'],
    'data': ['views/manufacturing_orders.xml',
             'views/portal_view.xml',
             ]
}
