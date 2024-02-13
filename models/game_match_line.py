from datetime import datetime
from odoo import models, fields, api

class GameMatchLine(models.Model):
    _name = "game.match.line"

    game_match_id = fields.Many2one(comodel_name="game.match", string="Game Match")
    game_match_line_component_ids = fields.One2many("game.match.line.component", string="Game Match", inverse_name="game_match_line_id")
    player_id = fields.Many2one(comodel_name="player", string="player")
    score = fields.Integer(string="Score")