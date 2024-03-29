from datetime import datetime
from odoo import models, fields, api

class GameMatch(models.Model):
    _name = "game.match"


    name = fields.Char(string="Name", help="Name of the game match")
    note = fields.Char(string="Note", help="Note of the game match")
    date = fields.Datetime(string="Date", help="Date of the game match", default=datetime.now())
    game_id = fields.Many2one(comodel_name="game", string="Game")
    game_match_line_ids = fields.One2many(comodel_name="game.match.line", string="Game Match Line", inverse_name="game_match_id")
    game_match_line_component_ids = fields.One2many(comodel_name="game.match.line.component", string="Game Match Line", inverse_name="game_match_id")
    winner_id = fields.Many2one(comodel_name="player", string="Winner of the game match", compute='_compute_winner_id', store=True)
    highest_score = fields.Integer(string="Highest Score", compute='_compute_highest_score')
    avg_score = fields.Float(string="Average Score", compute='_compute_avg_score', store=True)


    @api.depends("game_match_line_ids")
    def _compute_winner_id(self):
        """
        Compute the winner ID based on the game match lines.

        :return: None if there are no match lines, otherwise the ID of the player with the highest score.
        """
        sorted_match_line_ids = self.game_match_line_ids.sorted(key=lambda line: line.score, reverse=True)
        self.winner_id = sorted_match_line_ids[0].player_id if sorted_match_line_ids else None


    @api.depends("avg_score")
    def _compute_highest_score(self):
        for game_match in self:
            game_match.highest_score = 0
            if game_match.winner_id:
                winner = game_match.game_match_line_ids.filtered(lambda line: line.player_id == game_match.winner_id)
                if winner:
                    game_match.highest_score = winner[0].score


    @api.depends("game_match_line_ids")
    def _compute_avg_score(self):
        if self.game_match_line_ids:
            scores = self.game_match_line_ids.mapped('score')
            self.avg_score = sum(scores) / len(scores)
        else:
            self.avg_score = 0