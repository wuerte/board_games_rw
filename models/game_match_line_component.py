from datetime import datetime
from odoo import models, fields, api

class GameMatchLineComponent(models.Model):
    _name = "game.match.line.component"

    game_match_id = fields.Many2one(comodel_name="game.match", string="Game Match")
    game_match_line_id = fields.Many2one(comodel_name="game.match.line", string="Game Match Line")
    player_id = fields.Many2one(comodel_name="player", string="player")
    value = fields.Integer(string="Value")