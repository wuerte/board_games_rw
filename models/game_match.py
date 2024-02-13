from datetime import datetime
from odoo import models, fields, api

class GameMatch(models.Model):
    _name = "game.match"

    name = fields.Char(string="Name", help="Name of the game match")
    note = fields.Char(string="Note", help="Note of the game match")
    date = fields.Datetime(string="Date", help="Date of the game match", default=datetime.now())
    game_id = fields.Many2one(comodel_name="game", string="Game")
    game_match_line_id = fields.One2many(comodel_name="game.match.line", string="Game Match Line", inverse_name="game_match_id")
    # game_match_line_components_ids = fields.Many2many(comodel_name="game.match.line", string="Game Match Line")