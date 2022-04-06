from otree.api import *
import numpy as np

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'cogmap'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    CHOICES = [
        dict(name='A', label="Die Zentralbank erhöht den Leitzins."),
        dict(name='B', label="Die Inflationsrate steigt"),
        dict(name='C', label="Die Banken erhöhen die Kreditzinsen."),
        dict(name='D', label="Die Löhne stagnieren."),
        dict(name='E', label="Die Gewerkschaft fördert höhere Löhne."),
        dict(name='F', label="Die Renten steigen."),
        dict(name='G', label="Die Automobilhersteller machen Rekordgewinne. "),
        dict(name='H', label="Die Bundesregierung führt eine CO2-Steuer ein"),
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    name = models.StringField()
    age = models.IntegerField()
    A = models.BooleanField(blank=True)
    B = models.BooleanField(blank=True)
    C = models.BooleanField(blank=True)
    D = models.BooleanField(blank=True)
    E = models.BooleanField(blank=True)
    F = models.BooleanField(blank=True)
    G = models.BooleanField(blank=True)
    H = models.BooleanField(blank=True)
    json = models.StringField()
    pass


# PAGES
class Survey(Page):
    form_model = 'player'
    form_fields = ['name','age']

    pass

class Selection(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player: Player):
        return [choice['name'] for choice in C.CHOICES]


    @staticmethod
    def error_message(player: Player, values):
        # print('values is', values)
        num_selected = 0
        for choice in C.CHOICES:
            if values[choice['name']]:
                num_selected += 1
        if num_selected != 4:
            return "You must select precisely 4"
    pass

class CogMap(Page):
    def js_vars(player):
        selection = []
        #connectors = ["Fixed Pie","Good-begets-good","Mangel erhöht die Preise"]
        for i in C.CHOICES:
            y = i.get("name")
            x = i.get("label")
            if player.field_maybe_none(y) == True:
                selection.append(x)
        # if player.field_maybe_none('A') == True:
        #     selection.append("english")
        # if player.field_maybe_none('french') == True:
        #     selection.append("french")
        # if player.field_maybe_none('spanish') == True:
        #     selection.append("spanish")
        # if player.field_maybe_none('finnish') == True:
        #     selection.append("finnish")

        return dict(
            selection = selection,
            #connectors = connectors
        )
    form_model = 'player'
    form_fields = ['json']
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Survey, Selection,  CogMap]
