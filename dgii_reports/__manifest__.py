{
    'name': "Declaraciones DGII",

    'summary': """
        Este módulo extiende las funcionalidades del do_accounting,
        integrando los reportes de declaraciones fiscales""",

    'author': "Adel Networks S,R,L",
    'license': 'LGPL-3',
    'category': 'Accounting',
    'version': '14.0.0.0.2',
    'depends': ['base', 'l10n_do_accounting'],
    'data': [
        'data/invoice_service_type_detail_data.xml',
        'security/ir.model.access.csv',
        'security/ir_rule.xml',
        'views/res_partner_views.xml',
        'views/account_tax_views.xml',
        'views/account_account_views.xml',
        'views/account_invoice_views.xml',
        'views/dgii_report_views.xml',
        'views/dgii_report_templates.xml',
        'wizard/dgii_report_regenerate_wizard_views.xml',
    ],
    'external_dependencies': {
        'python': ['pycountry']
    },
}
