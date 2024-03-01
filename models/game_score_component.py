from odoo import models, fields, api, _


class GameScoreComponent(models.Model):
    _name = "game.score.component"

    name = fields.Char(string="Name", help="Name of the Game Score Component")
    game_id = fields.Many2one(comodel_name="game", string="Game")