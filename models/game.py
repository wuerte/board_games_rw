from odoo import models, fields


class Game(models.Model):
    _name = "game"

    name = fields.Char(string="Name", help="Name of the game match")
    note = fields.Char(string="Note", help="Note of the game match")
    game_match_ids = fields.One2many('game.match', string="Game Matches", inverse_name="game_id")