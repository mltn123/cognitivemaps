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
    studienbereich_andere = models.StringField(label="Anderer Studienfachbereich", blank=True)
    medien_andere = models.StringField(label="Andere Quelle", blank=True)

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

    studienbereich = models.StringField(
        label = "Wählen Sie bitte Ihren Studienfachbereich",
        choices=["Event, Tourismus & Hotel ", "Gesellschafts- & Sozialwissenschaften", "Gesundheit & Medizin", "Informatik", "Ingenieurwesen & Technik",
                 "Kunst, Musik, Design & Mode", "Lehramt & Pädagogik", "Medien, Kommunikation & Marketing", "Naturwissenschaften & Mathematik",
                 "Psychologie","Recht, Steuern & Verwaltung ", "Sport & Fitness", "Sprach- & Kulturwissenschaft",
                 "Umwelt-, Agrar- & Forstwissenschaft", "Wirtschaft & Management", "Andere"], blank=True
    )

    berufsfeld = models.StringField(
        choices=["Bau, Architektur, Vermessung", "Dienstleistung", "Elektro", "Gesundheit", "IT, Computer",
                 "Kunst, Kultur, Gestaltung", "Landwirtschaft, Natur, Umwelt", "Medien", "Metall, Maschinenbau",
                 "Naturwissenschaften","Produktion, Fertigung", "Soziales, Pädagogik", "Technik, Technologiefelder",
                 "Verkehr, Logistik", "Wirtschaft, Verwaltung", "Andere"], blank=True
    )
    geschlecht = models.StringField(
        label = "Ihr Geschlecht",
        choices=["männlich", "weiblich", "divers"],
        widget=widgets.RadioSelect
    )

    taetigkeit = models.StringField(
        label = "Wählen Sie bitte ihren momentanen Beschäftigungsstatus",
        choices=["Ausbildung", "Studium", "Berufstätig", "Duales / berufsbegleitendes Studium", "keine Tätigkeit / Ruhestand"]
    )

    bildungsgrad = models.StringField(
        label = "Wählen Sie bitte Ihren höchsten Bildungsabschluss",
        choices=["ohne Abschluss", "Hauptschulabschluss", "Realschulabschluss", "Fachabitur", "Abitur", "Bachelorabschluss", "Masterabschluss / Diplom",]
    )


    nachrichten_regional = models.FloatField(blank=True, label="Regionalnachrichten")
    nachrichten_innenpolitik = models.FloatField(blank=True, label="Innenpolitik")
    nachrichten_aussenpolitik = models.FloatField(blank=True, label="Außenpolitik")
    nachrichten_wirtschaft = models.FloatField(blank=True, label="Wirtschaft")
    nachrichten_finanzen = models.FloatField(blank=True, label="Finanzen")
    nachrichten_gesellschaft = models.FloatField(blank=True, label="Gesellschaft")
    nachrichten_wissenschaft = models.FloatField(blank=True, label="Wissenschaft")
    nachrichten_umwelt = models.FloatField(blank=True, label="Umwelt und Nachhaltigkeit")

    medium_zeitschriften = models.FloatField(blank=True, label="Zeitschriften in Papierform")
    medium_radio = models.FloatField(blank=True, label="Radio")
    medium_fernsehen = models.FloatField(blank=True, label="Fernsehen")
    medium_internet = models.FloatField(blank=True, label="Internet")
    medium_sozial = models.FloatField(blank=True, label="Soziale Medien")

    medien_bild = models.FloatField(blank=True, label="Bild / Bild.de")
    medien_focus = models.FloatField(blank=True, label="FOCUS / FOCUS Online")
    medien_faz = models.FloatField(blank=True, label="Frankfurter Allgemeine Zeitung / FAZ.net")
    medien_spiegel = models.FloatField(blank=True, label="Der Spiegel / Spiegel Online")
    medien_stern = models.FloatField(blank=True, label="Der Stern / Stern Online")
    medien_sueddeutsche = models.FloatField(blank=True, label="Süddeutsche Zeitung / sz.de")
    medien_tagesschau = models.FloatField(blank=True, label="Tagesschau / Tagesschau.de")
    medien_tagesspiegel = models.FloatField(blank=True, label="Tagesspiegel / Tagesspiegel.de")
    medien_taz = models.FloatField(blank=True, label="taz / taz.de")
    medien_welt = models.FloatField(blank=True, label="Die Welt / Welt.de")
    medien_zeit = models.FloatField(blank=True, label="Die Zeit / Zeit Online")
    medien_rtl = models.FloatField(blank=True, label="RTL News")
    medien_facebook = models.FloatField(blank=True, label="Facebook")
    medien_twitter = models.FloatField(blank=True, label="Twitter")
    medien_instagram = models.FloatField(blank=True, label="Instagram")
    medien_whatsapp = models.FloatField(blank=True, label="WhatsApp")
    medien_telegram = models.FloatField(blank=True, label="Telegram")
    medien_prosieben = models.FloatField(blank=True, label="ProSieben Newstime")
    medien_linkedin = models.FloatField(blank=True, label="LinkedIn")
    medien_andere_toggle = models.FloatField(blank=True, label="Andere Medien")

    verschw_1 = models.FloatField()
    verschw_2 = models.FloatField()
    verschw_3 = models.FloatField()
    verschw_4 = models.FloatField()
    verschw_5 = models.FloatField()
    verschw_6 = models.FloatField()


    json = models.TextField()
    reihenfolge = models.StringField()
    pass


# PAGES
class Survey(Page):
    form_model = 'player'
    form_fields = ['alter','geschlecht',"taetigkeit"]
    pass


class Survey2(Page):
    form_model = 'player'
    form_fields = ['berufsfeld','berufsfeld_andere',"studienbereich","studienbereich_andere","bildungsgrad" ]
    @staticmethod
    def vars_for_template(player):
        if player.field_maybe_none("taetigkeit") ==  "Ausbildung":
            return dict(
                berufsfeld_label='Wählen Sie bitte die Branche Ihrer Ausbildung'
            )
        elif player.field_maybe_none("taetigkeit") ==  "Berufstätig":
            return dict(
                berufsfeld_label='Wählen Sie bitte die Branche Ihres Berufes'
            )
        elif player.field_maybe_none("taetigkeit") ==  "Duales / berufsbegleitendes Studium":
            return dict(
                berufsfeld_label='Wählen Sie bitte die Branche Ihres Dualen / berufsbegleitenden Studiums'
            )
        elif player.field_maybe_none("taetigkeit") ==  "keine Tätigkeit / Ruhestand":
            return dict(
                berufsfeld_label='Wählen Sie bitte die Branche Ihres ehemaligen Berufes'
            )
        else:
            return dict(
                berufsfeld_label=''
            )
    @staticmethod
    def error_message(player, values):
        if player.taetigkeit == "Ausbildung":
            if values['berufsfeld']  == "":
                return 'Wählen Sie bitte die Branche Ihrer Ausbildung'
        elif player.taetigkeit == "Studium":
            if values['studienbereich']  == "":
                return 'Wählen Sie bitte Ihren Studienfachbereich'
        elif player.taetigkeit == "Duales / berufsbegleitendes Studium":
            if values['berufsfeld']  == "":
                return 'Wählen Sie bitte die Branche Ihres Dualen / berufsbegleitenden Studiums'
        elif player.taetigkeit == "Berufstätig":
            if values['berufsfeld']  == "":
                return 'Wählen Sie bitte die Branche Ihres Berufes'
        elif player.taetigkeit == "keine Tätigkeit / Ruhestand":
            if values['berufsfeld'] == "":
                return 'Wählen Sie bitte die Branche Ihres ehemaligen Berufes'
    pass

class Survey3(Page):
    form_model = 'player'
    form_fields = ['medium_zeitschriften', 'medium_radio', 'medium_fernsehen', 'medium_internet', 'medium_sozial',
                   'nachrichten_regional','nachrichten_innenpolitik','nachrichten_aussenpolitik','nachrichten_wirtschaft',
                   'nachrichten_finanzen', 'nachrichten_gesellschaft', 'nachrichten_wissenschaft', 'nachrichten_umwelt',
                   'medien_bild','medien_facebook', 'medien_focus','medien_faz','medien_instagram','medien_prosieben','medien_rtl','medien_spiegel','medien_stern','medien_sueddeutsche',
                   'medien_tagesschau','medien_tagesspiegel','medien_taz','medien_telegram','medien_twitter','medien_welt', 'medien_whatsapp','medien_zeit','medien_andere'
    ]
    @staticmethod
    def error_message(player, values):
        for i in ["medium_","nachrichten_","medien_"]:
            filterdict =  dict(filter(lambda item: i in item[0], values.items()))
            if not any(filterdict.values()):
                k = []
                if i == "medium_":
                    k = "ein Medium"
                elif i == "nachrichten_":
                    k = "eine Art von Nachrichten"
                elif i == "medien_":
                    k = "eine Quelle"
                return 'Geben Sie bitte mindestens ' + k + " an."

    pass


class Instructions(Page):
    form_model = 'player'

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
        player.reihenfolge = ','.join(str(e['name']) for e in choices)
        return [choice['name'] for choice in choices]



    @staticmethod
    def error_message(player, values):
       # print('values is', values)
        num_selected = 0
        for choice in C.CHOICES:
            if values[choice['name']]:
                num_selected += 1
        if num_selected < 3:
            return "Wählen Sie mindestens 2 zusätzliche Ereignisse"
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


class Narratives(Page):
    form_model = 'player'
    form_fields = ['verschw_1','verschw_2','verschw_3','verschw_4','verschw_5','verschw_6']
    pass

class ResultsWaitPage(WaitPage):
    pass


class Results(Page):
    pass

#page_sequence = [Narratives]
page_sequence = [Survey, Survey2, Survey3, Instructions, Selection, CogMap, Narratives]
