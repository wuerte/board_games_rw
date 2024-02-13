{
    'name': "Board Game Recorder",
    'version': '1.0',
    'depends': ['base'],
    'author': "Radosław Wierzgała",
    'category': 'Board Games',
    'description': """
    Board Game Recorder for Odoo.
    """,

    'data': [
        'security/ir.model.access.csv',
        'views/game_menus.xml',
        'views/game_match_views.xml',
    ],
    'installable': True,
    'application': True,
}