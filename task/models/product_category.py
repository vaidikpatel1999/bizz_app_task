from odoo import models, fields,exceptions,api

# Category should have unique name.
class ProductCategory(models.Model):
    _inherit = 'product.category'

    @api.model
    def create(self, vals):
        if 'name' in vals:
            existing_category = self.search([('name', '=ilike', vals['name'])])
            if existing_category:
                raise exceptions.UserError("A Category with the same name already exists.")

        return super(ProductCategory, self).create(vals)

    def write(self, vals):
        if 'name' in vals:
            existing_category = self.search([('name', '=ilike', vals['name'])])
            if existing_category:
                raise exceptions.UserError("A Category with the same name already exists.")

        return super(ProductCategory, self).write(vals)