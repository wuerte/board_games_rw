from odoo import models, fields, api, _


class Game(models.Model):
    _name = "game"

    name = fields.Char(string="Name", help="Name of the game match")
    note = fields.Char(string="Note", help="Note of the game match")
    game_match_ids = fields.One2many('game.match', string="Game Matches", inverse_name="game_id")
    game_match_line_ids = fields.One2many('game.match.line', string="Game Matche Line", inverse_name="game_id", related="game_match_ids.game_match_line_ids")
    avg_score = fields.Float(string='Average Score', compute='_compute_avg_score')

    #TODO add form view with readolny game_match_ids!!
    #TODO add game_match_line_ids and also to Form View.

    @api.depends("game_match_line_ids")
    def _compute_avg_score(self):
        scores = self.game_match_line_ids.mapped('score')
        self.avg_score = sum(scores) / len(scores)
