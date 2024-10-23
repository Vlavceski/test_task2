{
    'name': 'Vendor Product Prices',
    'version': '17.0.1.0.0',
    'depends': ['purchase'],
    'category': 'Purchases',
    'summary': 'Lists all vendor products and their prices in one menu',
    'description': """
        This module allows users to view all vendor product prices from a single menu
        under the "Configuration" menu of the Purchase app.
    """,
    'author': 'Your Name',
    'data': [
        'views/vendor_product_price_view.xml',
    ],
    'installable': True,
    'application': False,
}
