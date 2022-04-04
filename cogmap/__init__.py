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
        dict(name='A', label="Ereignis A"),
        dict(name='B', label="Ereignis B"),
        dict(name='C', label="Ereignis C"),
        dict(name='D', label="Ereignis D"),
        dict(name='E', label="Ereignis E"),
        dict(name='F', label="Ereignis F"),
        dict(name='G', label="Ereignis G"),
        dict(name='H', label="Ereignis H"),
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
        if num_selected < 1:
            return "You must select at least 1 language."
    pass

class CogMap(Page):
    def js_vars(player):
        selection = []
        for i in C.CHOICES:
            y = i.get("name")
            if player.field_maybe_none(y) == True:
                selection.append(y)
        # if player.field_maybe_none('A') == True:
        #     selection.append("english")
        # if player.field_maybe_none('french') == True:
        #     selection.append("french")
        # if player.field_maybe_none('spanish') == True:
        #     selection.append("spanish")
        # if player.field_maybe_none('finnish') == True:
        #     selection.append("finnish")

        return dict(
            selection = selection
        )
    form_model = 'player'
    form_fields = ['json']
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [Survey, Selection,  CogMap]
