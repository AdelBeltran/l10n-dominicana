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

from werkzeug.utils import redirect
from odoo.http import request, Controller, route


class DgiiReportsControllers(Controller):

    @route(['/dgii_reports/<ncf_rnc>'], type='http', auth='user')
    def redirect_link(self, ncf_rnc):

        env = request.env
        base_url = env['ir.config_parameter'].sudo().get_param('web.base.url')

        if str(ncf_rnc)[:1] == 'B':
            invoice_id = env['account.move'].search([
                ('reference', '=', ncf_rnc)
                ], limit=1)
            if invoice_id:
                # Get action depending on invoice type
                action_map = {
                    'out_invoice': request.env.ref(
                        'account.action_invoice_tree1'
                        ),
                    'in_invoice': request.env.ref(
                        'account.action_vendor_bill_template'
                        ),
                    'out_refund': request.env.ref(
                        'account.action_invoice_out_refund'
                        ),
                    'in_refund': request.env.ref(
                        'account.action_invoice_in_refund'
                        )
                }
                action = action_map[invoice_id.type]
                url = "%s/web#id=%s&action=%s&model=account.move&view" \
                      "_type=form" % (base_url, invoice_id.id, action.id)

                return redirect(url)  # Returns invoice form view

            return redirect(base_url)

        else:
            partner_id = env['res.partner'].search([('vat', '=', ncf_rnc)],
                                                   limit=1)
            if partner_id:
                url = "%s/web#id=%s&model=res.partner&view_type=form" % (
                    base_url, partner_id.id)
                return redirect(url)  # Returns partner form view

            return redirect(base_url)
