from odoo import models, fields, api

class KPIModel(models.Model):
    _name = 'kpi.model'
    _description = 'KPI Model'
    _order = 'date desc'

    name = fields.Char(string='KPI Name', required=True)
    value = fields.Float(string='KPI Value', required=True)
    target = fields.Float(string='KPI Target')
    date = fields.Date(string='Date', default=fields.Date.today)
    achieved = fields.Boolean(string='Achieved', compute='_compute_achieved', store=True)

    @api.depends('value', 'target')
    def _compute_achieved(self):
        for record in self:
            record.achieved = record.value >= record.target
