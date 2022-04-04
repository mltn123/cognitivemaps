from otree.api import *
import numpy as np

doc = """
Your app description
"""


class C(BaseConstants):
    NAME_IN_URL = 'cogmap'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    LANGUAGES = [
        dict(name='english', label="I speak English"),
        dict(name='french', label="Je parle français"),
        dict(name='spanish', label="Hablo español"),
        dict(name='finnish', label="Puhun suomea"),
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
    name = models.StringField()
    age = models.IntegerField()
    english = models.BooleanField(blank=True)
    french = models.BooleanField(blank=True)
    spanish = models.BooleanField(blank=True)
    finnish = models.BooleanField(blank=True)
    json = models.StringField()
    pass


# PAGES
class MyPage(Page):

    form_model = 'player'
    form_fields = ['name', 'age', 'checklist']
    @staticmethod
    def get_form_fields(player: Player):
        return [lang['name'] for lang in C.LANGUAGES]


    @staticmethod
    def error_message(player: Player, values):
        # print('values is', values)
        num_selected = 0
        for lang in C.LANGUAGES:
            if values[lang['name']]:
                num_selected += 1
        if num_selected < 1:
            return "You must select at least 1 language."
    pass

class CogMap(Page):
    def js_vars(player):
        selection = []
        if player.field_maybe_none('english') == True:
            selection.append("english")
        if player.field_maybe_none('french') == True:
            selection.append("french")
        if player.field_maybe_none('spanish') == True:
            selection.append("spanish")
        if player.field_maybe_none('finnish') == True:
            selection.append("finnish")

        return dict(
            english = player.field_maybe_none('english'),
            french = player.field_maybe_none('french'),
            spanish = player.field_maybe_none('spanish'),
            finnish = player.field_maybe_none('finnish'),
            selection = selection
        )
    form_model = 'player'
    form_fields = ['json']
    pass


class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass


page_sequence = [MyPage,  CogMap]
