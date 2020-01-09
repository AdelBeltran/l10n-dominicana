
from odoo import models, fields, _


class Partner(models.Model):
    _inherit = 'res.partner'

    _dgii_taxpayer_types = [
        ('fiscal', _('Normal Tax Payer')),
        ('no_fiscal', _('Non Tax Payer')),
        ('special', _('Special Tax Payer')),
        ('governmental', _('Governmental')),
        ('foreigner', _('Foreigner')),
    ]

    l10n_do_dgii_tax_payer_type = fields.Selection(
        selection='dgii_tax_payer_types',
        string='Taxpayer Type',
        index=True,
        help='1 - VAT Affected (1st Category) (Most of the cases)\n'
             '2 - Fees Receipt Issuer (Applies to suppliers who issue fees receipt)\n'
             '3 - End consumer (only receipts)\n'
             '4 - Foreigner')

    l10n_do_expense_type = fields.Selection(
        [('01', '01 - Gastos de Personal'),
         ('02', '02 - Gastos por Trabajo, Suministros y Servicios'),
         ('03', '03 - Arrendamientos'),
         ('04', '04 - Gastos de Activos Fijos'),
         ('05', '05 - Gastos de Representación'),
         ('06', '06 - Otras Deducciones Admitidas'),
         ('07', '07 - Gastos Financieros'),
         ('08', '08 - Gastos Extraordinarios'),
         ('09', '09 - Compras y Gastos que forman parte del Costo de Venta'),
         ('10', '10 - Adquisiciones de Activos'),
         ('11', '11 - Gastos de Seguro'),
         ],
        string="Expense Type",
    )
