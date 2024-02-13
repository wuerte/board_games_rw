from datetime import datetime
from odoo import models, fields, api

class Player(models.Model):
    _name = "player"

    name = fields.Char(string="Name", help="Name of the game match")
    note = fields.Char(string="Note", help="Note of the game match")
    age = fields.Integer(string="Age of player")