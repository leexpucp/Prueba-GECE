from .. import models
import otree.api
from otree.api import Currency as c, currency_range

class Page(otree.api.Page):

    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.group = models.Group()
        self.player = models.Player()


class WaitPage(otree.api.WaitPage):


    def z_autocomplete(self):
        self.subsession = models.Subsession()
        self.group = models.Group()
