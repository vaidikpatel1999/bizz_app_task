from odoo import models, fields
from collections import defaultdict


class ProcurementGroup(models.Model):
    _inherit = 'procurement.group'

    def _prepare_purchase_order(self, company, supplier, values, po_lines):
        """Add category to values dict to differentiate."""
        category_id = values.get('product_category_id')
        res = super()._prepare_purchase_order(company, supplier, values, po_lines)
        res.update({
            'product_category_id': category_id,
        })
        return res

    def _run_buy(self, procurements):
        """Override to split by product category."""
        # Group procurements by (supplier, product_category_id)
        grouped_procurements = defaultdict(list)

        for procurement in procurements:
            supplier = procurement.rule_id._get_supplier(procurement.product_id, procurement.company_id, procurement.values.get('date_planned'))
            if not supplier:
                continue

            category = procurement.product_id.categ_id
            key = (supplier.id, category.id)
            procurement.values.update({
                'product_category_id': category.id,
            })
            grouped_procurements[key].append(procurement)

        # Run original logic per group
        for (supplier_id, category_id), group in grouped_procurements.items():
            super(ProcurementGroup, self)._run_buy(group)


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    product_category_id = fields.Many2one('product.category', string="Product Category", readonly=True)

    def _prepare_invoice(self):
        res = super()._prepare_invoice()
        res.update({
            'product_category_id': self.product_category_id.id,
        })
        return res