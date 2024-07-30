{
    'name': 'KPI Module',
    'version': '1.1',
    'category': 'Performance',
    'summary': 'Track and manage Key Performance Indicators',
    'description': """
        This module allows users to create, track, and manage Key Performance Indicators (KPIs) within Odoo.
        Features:
        - KPI creation and management
        - Customizable KPI dashboards
        - KPI tracking and reporting
    """,
    'author': 'Yusuf Bender',
    'website': 'https://github.com/yusufbender',
    'depends': ['base', 'web'],
    'data': [
        'security/kpi_security.xml',
        'security/ir.model.access.csv',
        'views/kpi_views.xml',
        'views/kpi_templates.xml',
        'data/kpi_data.xml',
    ],
    'qweb': [],
    'installable': True,
    'application': True,
}
