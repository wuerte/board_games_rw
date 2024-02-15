from datetime import datetime
from odoo import models, fields, api

class GameMatchLine(models.Model):
    _name = "game.match.line"

    game_match_id = fields.Many2one(comodel_name="game.match", string="Game Match")
    game_match_line_component_ids = fields.One2many("game.match.line.component", string="Game Match Line Component", inverse_name="game_match_line_id")
    player_id = fields.Many2one(comodel_name="player", string="Player")
    score = fields.Integer(string="Score")
    game_id = fields.Many2one(model="game", related="game_match_id.game_id", string="Game")
    date = fields.Datetime(string="Date", help="Date of the game match line", related="game_match_id.date")