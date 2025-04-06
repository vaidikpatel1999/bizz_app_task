from odoo import models, fields,exceptions,api

# Copy all the tags from sale order to Delivery orders created from sale order.
class StockPicking(models.Model):
    _inherit = 'stock.picking'

    sale_order_tags = fields.Many2many(
        'crm.tag', string="Sale Tags", compute="tag_from_sale",
        help="Tags copied from the Sale Order"
    )

    @api.depends('sale_id')
    def tag_from_sale(self):
        for picking in self:
            if picking.sale_id:
                picking.sale_order_tags = picking.sale_id.tag_ids
            else:
                picking.sale_order_tags = [(5, 0, 0)]


