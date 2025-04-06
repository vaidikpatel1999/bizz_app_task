# Partner should be search on the Ref field from all Many2one widgets.
# In Many2one field of partner, it should include Ref in the format PARTNER NAME [REF].
from odoo import models,fields,api
from odoo.osv import expression

class ResPartner(models.Model):
    _inherit = 'res.partner'

    def name_get(self):
        result = []
        for partner in self:
            name = partner.name or ''
            if partner.ref:
                name = f"{name} [{partner.ref}]"
            result.append((partner.id, name))
        return result

    @api.model
    def name_search(self, name='', args=None, operator='ilike', limit=100, name_get_uid=None):
        args = args or []
        domain = []

        if name:
            domain = ['|', ('name', operator, name), ('ref', operator, name)]

        partners = self.search(expression.AND([args, domain]), limit=limit)
        return partners.name_get()