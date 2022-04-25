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
        dict(name='Inflationsrate_steigt', label="Die Inflationsrate steigt"),
        dict(name='Leitzins_erhoeht', label="Die Zentralbank erhöht den Leitzins."),
        dict(name='Kreditzinsen', label="Die Banken erhöhen die Kreditzinsen."),
        dict(name='Loehne_stagnieren', label="Die Löhne stagnieren."),
        dict(name='Loehne_Gewerkschaft', label="Die Gewerkschaft fördert höhere Löhne."),
        dict(name='Renten_steigen', label="Die Renten steigen."),
        dict(name='Automobil_rekordgewinne', label="Die Automobilhersteller machen Rekordgewinne."),
        dict(name='CO2Steuer_einfuehrung', label="Die Bundesregierung führt eine CO2-Steuer ein"),
        dict(name='Lebensmittelpreise_steigen', label="Die Lebensmittelpreise steigen."),
        dict(name='Energiepreise_steigen', label="Die Energiepreise steigen"),
        dict(name='Corona_gespart', label="Die Menschen haben in der Coronazeit viel gespart."),
        dict(name='Arbeitslosigkeit_steigt', label="Die Arbeitslosigkeit ist gestiegen."),
        dict(name='Arbeitslosengeld_erhoeht', label="Die Regierung erhöht das Arbeitslosengeld."),
        dict(name='Managergehälter_steigen', label="Die Managergehälter sind gestiegen."),
        dict(name='Verteidigungsetat_erhoeht', label="Die Regierung hat angekündigt, den Verteidigungsetat zu erhöhen"),
        dict(name='Geld_verliert', label="Das Geld verliert an Wert."),
        dict(name='Dollarkurs_steigt', label="Der Dollarkurs ist gestiegen."),
        dict(name='Unwetter_schaden', label="Die Unwetter im Ahrtal haben Milliardenschäden verursacht."),
        dict(name='Borkenkaefer', label="Die Borkenkäferplage hat große Teile des Waldes vernichtet."),
        dict(name='Staatsverschuldung_steigt', label="Die Staatsverschuldung ist gestiegen."),
        dict(name='EU_greendeal', label="Die EU investiert Milliarden in den Green Deal."),
        dict(name='Fluechtlinge', label="Es kommen immer mehr Flüchtlinge nach Deutschland."),
        dict(name='Entsalzung', label="Deutschland investiert in eine Meerwasserentsalzungsanlage in Ägypten."),
        dict(name='Dax_steigt', label="Der Dax ist gestiegen."),
        dict(name='Diaeten', label="Der Bundestag erhöht die Diäten."),
        dict(name='Rohstoffe', label="In Zukunft werden Rohstoffe knapp."),
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    berufsfeld_andere = models.StringField(label="Andere Branche", blank=True)
    alter = models.IntegerField(label="Ihr Alter")
    Leitzins_erhoeht = models.BooleanField(blank=True, label= "Die Zentralbank erhöht den Leitzins.")
    Inflationsrate_steigt = models.BooleanField(blank=True, label="Die Inflationsrate steigt")
    Kreditzinsen = models.BooleanField(blank=True, label="Die Banken erhöhen die Kreditzinsen.")
    Loehne_stagnieren = models.BooleanField(blank=True, label="Die Löhne stagnieren.")
    Loehne_Gewerkschaft = models.BooleanField(blank=True, label="Die Gewerkschaft fördert höhere Löhne.")
    Renten_steigen = models.BooleanField(blank=True, label="Die Renten steigen.")
    Automobil_rekordgewinne = models.BooleanField(blank=True, label="Die Automobilhersteller machen Rekordgewinne.")
    CO2Steuer_einfuehrung = models.BooleanField(blank=True, label="Die Bundesregierung führt eine CO2-Steuer ein")
    Lebensmittelpreise_steigen = models.BooleanField(blank=True, label="Die Lebensmittelpreise steigen.")

    Energiepreise_steigen = models.BooleanField(blank=True, label="Die Energiepreise steigen")
    Corona_gespart  = models.BooleanField(blank=True, label="Die Menschen haben in der Coronazeit viel gespart.")
    Arbeitslosigkeit_steigt = models.BooleanField(blank=True, label="Die Arbeitslosigkeit ist gestiegen.")
    Arbeitslosengeld_erhoeht = models.BooleanField(blank=True, label="Die Regierung erhöht das Arbeitslosengeld.")
    Managergehälter_steigen = models.BooleanField(blank=True, label="Die Managergehälter sind gestiegen.")
    Verteidigungsetat_erhoeht = models.BooleanField(blank=True, label="Die Regierung hat angekündigt, den Verteidigungsetat zu erhöhen")
    Geld_verliert = models.BooleanField(blank=True, label="Das Geld verliert an Wert.")
    Dollarkurs_steigt = models.BooleanField(blank=True, label="Der Dollarkurs ist gestiegen.")
    Unwetter_schaden = models.BooleanField(blank=True, label="Die Unwetter im Ahrtal haben Milliardenschäden verursacht.")


    Borkenkaefer = models.BooleanField(blank=True, label="Die Borkenkäferplage hat große Teile des Waldes vernichtet.")
    Staatsverschuldung_steigt  = models.BooleanField(blank=True, label="Die Staatsverschuldung ist gestiegen.")
    EU_greendeal = models.BooleanField(blank=True, label="Die EU investiert Milliarden in den Green Deal.")
    Fluechtlinge = models.BooleanField(blank=True, label="Es kommen immer mehr Flüchtlinge nach Deutschland.")
    Entsalzung = models.BooleanField(blank=True, label="Deutschland investiert in eine Meerwasserentsalzungsanlage in Ägypten.")
    Dax_steigt = models.BooleanField(blank=True, label="Der Dax ist gestiegen.")
    Diaeten = models.BooleanField(blank=True, label="Der Bundestag erhöht die Diäten.")
    Rohstoffe = models.BooleanField(blank=True, label="In Zukunft werden Rohstoffe knapp.")

    berufsfeld = models.StringField(
        label = "Wählen Sie bitte die Branche Ihres Berufes / Ihres Studiums",
        choices=["Bau, Architektur, Vermessung", "Dienstleistung", "Elektro", "Gesundheit", "IT, Computer",
                 "Kunst, Kultur, Gestaltung", "Landwirtschaft, Natur, Umwelt", "Medien", "Metall, Maschinenbau",
                 "Naturwissenschaften","Produktion, Fertigung", "Soziales, Pädagogik", "Technik, Technologiefelder",
                 "Verkehr, Logistik", "Wirtschaft, Verwaltung", "Andere"]
    )
    geschlecht = models.StringField(
        label = "Ihr Geschlecht",
        choices=["männlich", "weiblich", "divers"],
        widget=widgets.RadioSelect
    )

    json = models.StringField()
    pass


# PAGES
class Survey(Page):
    form_model = 'player'
    form_fields = ['berufsfeld','berufsfeld_andere','alter','geschlecht']

    pass

class Selection(Page):
    form_model = 'player'



    @staticmethod
    def get_form_fields(player):
        import random
        choices = C.CHOICES.copy()
        rest = choices[1:]
        random.shuffle(rest)
        choices = [choices[0]] + rest
        return [choice['name'] for choice in choices]



    @staticmethod
    def error_message(player, values):
       # print('values is', values)
        num_selected = 0
        for choice in C.CHOICES:
            if values[choice['name']]:
                num_selected += 1
        if num_selected > 8:
            return "Wählen Sie bis zu 8 Ereignissen"
        if num_selected < 3:
            return "Wählen Sie mindestens 3 Ereignisse"
    pass

class CogMap(Page):
    def js_vars(player):
        selection = []
        for i in C.CHOICES:
            y = i.get("name")
            x = i.get("label")
            if player.field_maybe_none(y) == True:
                selection.append(x)

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
