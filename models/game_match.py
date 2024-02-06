from datetime import datetime
from odoo import models, fields, api

class GameMatch(models.Model):
    _name = "game.match"

    name = fields.Char(string="Name", help="Name of the game match")
    note = fields.Char(string="Note", help="Note of the game match")
    date = fields.Datetime(string="Date", help="Date of the game match", default=datetime.now())
    game_id = fields.Many2one(comodel_name="game", string="Game")