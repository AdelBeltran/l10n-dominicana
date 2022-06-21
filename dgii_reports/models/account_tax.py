# -*- coding: utf-8 -*-
##############################################################################
#
#    MoviTrack
#    Copyright (C) 2020-TODAY MoviTrack.
#    You can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
from odoo import api, fields, models


class AccountTax(models.Model):
    _inherit = 'account.tax'

    @api.model
    def _get_isr_retention_type(self):
        return [('01', 'Alquileres'),
                ('02', 'Honorarios por Servicios'),
                ('03', 'Otras Rentas'),
                ('04', 'Rentas Presuntas'),
                ('05', u'Intereses Pagados a Personas Jurídicas'),
                ('06', u'Intereses Pagados a Personas Físicas'),
                ('07', u'Retención por Proveedores del Estado'),
                ('08', u'Juegos Telefónicos')]

    purchase_tax_type = fields.Selection(
        [('itbis', 'ITBIS Pagado'),
         ('ritbis', 'ITBIS Retenido'),
         ('isr', 'ISR Retenido'),
         ('rext', 'Pagos al Exterior (Ley 253-12)'),
         ('none', 'No Deducible')],
        default="none",
        string="Tipo de Impuesto en Compra")

    isr_retention_type = fields.Selection(
        selection=_get_isr_retention_type,
        string="Tipo de Retención en ISR")