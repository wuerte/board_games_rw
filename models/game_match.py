from datetime import datetime
from odoo import models, fields, api

class GameMatch(models.Model):
    _name = "game.match"


    name = fields.Char(string="Name", help="Name of the game match")
    note = fields.Char(string="Note", help="Note of the game match")
    date = fields.Datetime(string="Date", help="Date of the game match", default=datetime.now())
    game_id = fields.Many2one(comodel_name="game", string="Game")
    game_match_line_ids = fields.One2many(comodel_name="game.match.line", string="Game Match Line", inverse_name="game_match_id")
    # game_match_line_components_ids = fields.Many2many(comodel_name="game.match.line", string="Game Match Line")
    winner_id = fields.Many2one(comodel_name="player", string="Winner of the game match", compute='_compute_winner_id')


    @api.depends("game_match_line_ids")
    def _compute_winner_id(self):
        """
        Compute the winner ID based on the game match lines.

        :return: None if there are no match lines, otherwise the ID of the player with the highest score.
        """
        sorted_match_line_ids = self.game_match_line_ids.sorted(key=lambda line: line.score, reverse=True)
        self.winner_id = sorted_match_line_ids[0].player_id if sorted_match_line_ids else None

