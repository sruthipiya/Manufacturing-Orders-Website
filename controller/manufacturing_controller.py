from odoo import http
from odoo.http import request
from odoo.addons.portal.controllers.portal import CustomerPortal


class ManufacturingCount(CustomerPortal):
    def _prepare_home_portal_values(self, counters):
        vals = super()._prepare_home_portal_values(counters)
        if 'mo_count' in counters:
            vals['mo_count'] = request.env[
                'mrp.production'].sudo().search_count(
                [('customer_id', '=', request.env.user.partner_id.id)])
        print(vals)
        return vals


class ManufacturingController(http.Controller):
    @http.route('/my/mo', type='http', auth='user', website=True)
    def my_mo_views(self):
        my_mo = request.env['mrp.production'].sudo().search(
            [('customer_id', '=', request.env.user.partner_id.id)])
        values = {'orders': my_mo}
        return request.render(
            "manufacturing_orders.portal_my_manufacturing_orders", values)
