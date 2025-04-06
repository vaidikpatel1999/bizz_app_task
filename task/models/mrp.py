# Manufacturing orders created from sale order should not allowed to change the qty after the confirmation.

from odoo import models,fields,api
from odoo.exceptions import UserError

class MrpProduction(models.Model):
    _inherit = 'mrp.production'

    @api.model
    def write(self, vals):
        for record in self:
            if record.origin and 'product_qty' in vals:
                sale_order = self.env['sale.order'].search([('name', '=', record.origin)], limit=1)
                if sale_order and record.state not in ['draft','cancel']:
                    raise UserError("You cannot change the quantity after the Manufacturing Order is confirmed.")
        return super(MrpProduction, self).write(vals)

    @api.onchange('qty_producing')
    def stop_change_qty(self):
        if self.origin:
            sale_order = self.env['sale.order'].search([('name', '=', self.origin)], limit=1)
            if sale_order:
                if self.qty_producing != self.product_qty:
                    if self.state not in ['draft', 'cancel']:
                        raise UserError("You cannot allow to  set differ the Producing quantity after the Manufacturing Order is confirmed")
