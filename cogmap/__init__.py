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
        dict(name='ev_Inflationsrate_steigt', label="Die Inflationsrate steigt"),
        dict(name='ev_Leitzins_erhoeht', label="Die Zentralbank erhöht den Leitzins."),
        dict(name='ev_Kreditzinsen', label="Die Banken erhöhen die Kreditzinsen."),
        dict(name='ev_Loehne_stagnieren', label="Die Löhne stagnieren."),
        dict(name='ev_Loehne_Gewerkschaft', label="Die Gewerkschaft fördert höhere Löhne."),
        dict(name='ev_Renten_steigen', label="Die Renten steigen."),
        dict(name='ev_mineraloel_rekordgewinne', label="Die Mineralölkonzerne machen Rekordgewinne."),
        dict(name='ev_CO2Steuer_einfuehrung', label="Die Bundesregierung führt eine CO2-Steuer ein"),
        dict(name='ev_Lebensmittelpreise_steigen', label="Die Lebensmittelpreise steigen."),
        dict(name='ev_Energiepreise_steigen', label="Die Energiepreise steigen"),
        dict(name='ev_Corona_gespart', label="Die Menschen haben in der Coronazeit viel gespart."),
        dict(name='ev_Arbeitslosigkeit_steigt', label="Die Arbeitslosigkeit ist gestiegen."),
        dict(name='ev_Arbeitslosengeld_erhoeht', label="Die Regierung erhöht das Arbeitslosengeld."),
        dict(name='ev_Managergehälter_steigen', label="Die Managergehälter sind gestiegen."),
        dict(name='ev_Verteidigungsetat_erhoeht', label="Die Regierung hat angekündigt, den Verteidigungsetat zu erhöhen"),
        dict(name='ev_Geld_verliert', label="Das Geld verliert an Wert."),
        dict(name='ev_Dollarkurs_steigt', label="Der Dollarkurs ist gestiegen."),
        dict(name='ev_Unwetter_schaden', label="Die Unwetter im Ahrtal haben Milliardenschäden verursacht."),
        dict(name='ev_Borkenkaefer', label="Die Borkenkäferplage hat große Teile des Waldes vernichtet."),
        dict(name='ev_Staatsverschuldung_steigt', label="Die Staatsverschuldung ist gestiegen."),
        dict(name='ev_EU_greendeal', label="Die EU investiert Milliarden in den Green Deal."),
        dict(name='ev_Fluechtlinge', label="Es kommen immer mehr Flüchtlinge nach Deutschland."),
        dict(name='ev_Entsalzung', label="Deutschland investiert in eine Meerwasserentsalzungsanlage in Ägypten."),
        dict(name='ev_Dax_steigt', label="Der Dax ist gestiegen."),
        dict(name='ev_Diaeten', label="Der Bundestag erhöht die Diäten."),
        dict(name='ev_Rohstoffe', label="In Zukunft werden Rohstoffe knapp."),
        dict(name='ev_Mieten', label="Die Mieten steigen."),
        dict(name='ev_GasEmbargo', label="Die Bundesregierung beschließt ein russisches Gas-Embargo."),
        dict(name='ev_RusUkrKonflikt', label="Der Russland Ukraine Konflikt verschärft sich."),
        dict(name='ev_Lockdown', label="Die Bundesregierung beschließt einen weiteren Lockdown (Affenpocken / COVID-19)."),
        dict(name='ev_mikrochip',label="Eine Fabrik zur Herstellung von Mikrochips brennt nieder."),
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
    ev_Leitzins_erhoeht = models.BooleanField(blank=True, label= "Die Zentralbank erhöht den Leitzins.")
    ev_Inflationsrate_steigt = models.BooleanField(blank=True, label="Die Inflationsrate steigt.")
    ev_Kreditzinsen = models.BooleanField(blank=True, label="Die Banken erhöhen die Kreditzinsen.")
    ev_Loehne_stagnieren = models.BooleanField(blank=True, label="Die Löhne stagnieren.")
    ev_Loehne_Gewerkschaft = models.BooleanField(blank=True, label="Die Gewerkschaft fördert höhere Löhne.")
    ev_Renten_steigen = models.BooleanField(blank=True, label="Die Renten steigen.")
    ev_mineraloel_rekordgewinne = models.BooleanField(blank=True, label="Die Mineralölkonzerne machen Rekordgewinne.")
    ev_CO2Steuer_einfuehrung = models.BooleanField(blank=True, label="Die Bundesregierung führt eine CO2-Steuer ein.")
    ev_Lebensmittelpreise_steigen = models.BooleanField(blank=True, label="Die Lebensmittelpreise steigen.")

    ev_Energiepreise_steigen = models.BooleanField(blank=True, label="Die Energiepreise steigen.")
    ev_Corona_gespart  = models.BooleanField(blank=True, label="Die Menschen haben in der Coronazeit viel gespart.")
    ev_Arbeitslosigkeit_steigt = models.BooleanField(blank=True, label="Die Arbeitslosigkeit steigt.")
    ev_Arbeitslosengeld_erhoeht = models.BooleanField(blank=True, label="Die Regierung erhöht das Arbeitslosengeld.")
    ev_Managergehälter_steigen = models.BooleanField(blank=True, label="Die Managergehälter steigen.")
    ev_Verteidigungsetat_erhoeht = models.BooleanField(blank=True, label="Die Regierung hat angekündigt, den Verteidigungsetat zu erhöhen.")
    ev_Geld_verliert = models.BooleanField(blank=True, label="Das Geld verliert an Wert.")
    ev_Dollarkurs_steigt = models.BooleanField(blank=True, label="Der Dollarkurs steigt.")
    ev_Unwetter_schaden = models.BooleanField(blank=True, label="Die Unwetter im Ahrtal haben Milliardenschäden verursacht.")


    ev_Borkenkaefer = models.BooleanField(blank=True, label="Die Borkenkäferplage hat große Teile des Waldes vernichtet.")
    ev_Staatsverschuldung_steigt  = models.BooleanField(blank=True, label="Die Staatsverschuldung steigt.")
    ev_EU_greendeal = models.BooleanField(blank=True, label="Die EU investiert Milliarden in den Green Deal.")
    ev_Fluechtlinge = models.BooleanField(blank=True, label="Es kommen immer mehr Flüchtlinge nach Deutschland.")
    ev_Entsalzung = models.BooleanField(blank=True, label="Deutschland investiert in eine Meerwasserentsalzungsanlage in Ägypten.")
    ev_Dax_steigt = models.BooleanField(blank=True, label="Der Dax steigt.")
    ev_Diaeten = models.BooleanField(blank=True, label="Der Bundestag erhöht die Diäten.")
    ev_Rohstoffe = models.BooleanField(blank=True, label="In Zukunft werden Rohstoffe knapp.")

    ev_Mieten = models.BooleanField(blank=True, label="Die Mieten steigen.")
    ev_GasEmbargo = models.BooleanField(blank=True, label="Die Bundesregierung beschließt ein russisches Gas-Embargo.")
    ev_RusUkrKonflikt = models.BooleanField(blank=True, label="Der Russland Ukraine Konflikt verschärft sich.")
    ev_Lockdown = models.BooleanField(blank=True, label="Die Bundesregierung beschließt einen weiteren Lockdown (Affenpocken / COVID-19).")
    ev_mikrochip = models.BooleanField(blank=True, label="Eine Fabrik zur Herstellung von Mikrochips brennt nieder.")

    studienbereich = models.StringField(
        label = "Wählen Sie bitte Ihren Studienfachbereich",
        choices=["Event, Tourismus & Hotel ", "Gesellschafts- & Sozialwissenschaften", "Gesundheit & Medizin", "Informatik", "Ingenieurwesen & Technik",
                 "Kunst, Musik, Design & Mode", "Lehramt & Pädagogik", "Medien, Kommunikation & Marketing", "Naturwissenschaften & Mathematik",
                 "Psychologie","Recht, Steuern & Verwaltung ", "Sport & Fitness", "Sprach- & Kulturwissenschaft",
                 "Umwelt-, Agrar- & Forstwissenschaft", "Wirtschaft & Management", "Andere"], blank=True
    )

    berufsfeld = models.StringField(
        choices=["Bauwesen, Architektur, Vermessung", "Dienstleistung", "Elektro","Forschung", "Gesundheit", "IT, Computer",
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
        choices=["Ausbildung", "Studium", "Berufstätig", "Duales / berufsbegleitendes Studium", "keine Tätigkeit", "Ruhestand"]
    )

    bildungsgrad = models.StringField(
        label = "Wählen Sie bitte Ihren höchsten Bildungsabschluss",
        choices=["ohne Abschluss", "Hauptschulabschluss", "Realschulabschluss", "Fachabitur", "Abitur", "Bachelorabschluss", "Masterabschluss / Diplom", "Promotion"]
    )


    nachrichten_regional = models.FloatField(blank=True, label="Regionalnachrichten / Lokalnachrichten")
    nachrichten_innenpolitik = models.FloatField(blank=True, label="Innenpolitik")
    nachrichten_aussenpolitik = models.FloatField(blank=True, label="Außenpolitik")
    nachrichten_wirtschaft = models.FloatField(blank=True, label="Wirtschaft")
    nachrichten_finanzen = models.FloatField(blank=True, label="Finanzen")
    nachrichten_gesellschaft = models.FloatField(blank=True, label="Gesellschaft")
    nachrichten_wissenschaft = models.FloatField(blank=True, label="Wissenschaft")
    nachrichten_umwelt = models.FloatField(blank=True, label="Umwelt und Nachhaltigkeit")


    medium_zeitschriften = models.FloatField(blank=True, label="Printmedien (Zeitungen / Zeitschriften in Papierform)")
    medium_onlinezeitschriften = models.FloatField(blank=True, label="Online Zeitungen / Zeitschriften")
    medium_radio = models.FloatField(blank=True, label="Radio")
    medium_fernsehen = models.FloatField(blank=True, label="Fernsehen")
    medium_internet = models.FloatField(blank=True, label="Internet")
    medium_sozial = models.FloatField(blank=True, label="Soziale Medien")

    medien_bild = models.FloatField(blank=True, label="Bild / Bild.de / Bild TV")
    medien_focus = models.FloatField(blank=True, label="FOCUS / FOCUS Online")
    medien_faz = models.FloatField(blank=True, label="Frankfurter Allgemeine Zeitung / FAZ.net")
    medien_spiegel = models.FloatField(blank=True, label="Der Spiegel / Spiegel Online")
    medien_sueddeutsche = models.FloatField(blank=True, label="Süddeutsche Zeitung / sz.de")
    medien_tagesschau = models.FloatField(blank=True, label="Tagesschau / Tagesschau.de")
    medien_taz = models.FloatField(blank=True, label="taz / taz.de")
    medien_welt = models.FloatField(blank=True, label="Die Welt / Welt.de")
    medien_zeit = models.FloatField(blank=True, label="Die Zeit / Zeit Online")
    medien_rtl = models.FloatField(blank=True, label="RTL News")
    medien_socialmedia = models.FloatField(blank=True, label="Facebook / Instagram / LinkedIn / Twitter")
    medien_messenger = models.FloatField(blank=True, label="WhatsApp / Telegram / Signal")
    medien_prosieben = models.FloatField(blank=True, label="ProSieben Newstime")
    medien_andere_toggle = models.FloatField(blank=True, label="Andere Medien")

    verschw_1 = models.FloatField()
    verschw_2 = models.FloatField()
    verschw_3 = models.FloatField()
    verschw_4 = models.FloatField()
    verschw_5 = models.FloatField()
    verschw_6 = models.FloatField()
    wiss_1 = models.FloatField()
    wiss_2 = models.FloatField()
    wiss_3 = models.FloatField()

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
        elif player.field_maybe_none("taetigkeit") ==  "keine Tätigkeit" or player.field_maybe_none("taetigkeit") == "Ruhestand":
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
        elif player.taetigkeit == "keine Tätigkeit" or  player.taetigkeit == "Ruhestand" :
            if values['berufsfeld'] == "":
                return 'Wählen Sie bitte die Branche Ihres ehemaligen Berufes'
    pass



class Survey3(Page):
    form_model = 'player'
    form_fields = ['medium_fernsehen','medium_internet','medium_radio', 'medium_sozial','medium_zeitschriften',"medium_onlinezeitschriften",
                   'nachrichten_aussenpolitik','nachrichten_finanzen', 'nachrichten_gesellschaft','nachrichten_innenpolitik',
                   'nachrichten_regional','nachrichten_umwelt','nachrichten_wirtschaft', 'nachrichten_wissenschaft',
                   'medien_bild','medien_faz','medien_focus','medien_spiegel','medien_sueddeutsche','medien_taz','medien_welt','medien_zeit',
                   'medien_prosieben','medien_rtl','medien_tagesschau','medien_messenger','medien_socialmedia','medien_andere'
    ]
    @staticmethod
    def error_message(player, values):
        for i in ["medium_","nachrichten_"]:
            filterdict =  dict(filter(lambda item: i in item[0], values.items()))
            if not any(filterdict.values()):
                k = []
                if i == "medium_":
                    k = "ein Medium"
                elif i == "nachrichten_":
                    k = "eine Art von Nachrichten"
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

class newCogMap(Page):
    form_model = 'player'
    form_fields = ['json']


    @staticmethod
    def get_form_fields(player):
        import random
        choices = C.CHOICES.copy()
        rest = choices[1:]
        random.shuffle(rest)
        choices = [choices[0]] + rest
        choices.append({'name': 'json', 'label': 'json'})
        player.reihenfolge = ','.join(str(e['name']) for e in choices[:-1])
        return [choice['name'] for choice in choices]



    @staticmethod
    def error_message(player, values):
       # print('values is', values)
        num_selected = 0
        for choice in C.CHOICES:
            if values[choice['name']]:
                num_selected += 1
        if num_selected < 3:
            return "Wählen Sie mindestens 3 zusätzliche Ereignisse"
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
    form_fields = ['verschw_1','verschw_2','verschw_3','verschw_4','verschw_5','verschw_6','wiss_1','wiss_2','wiss_3']
    pass

class ResultsWaitPage(WaitPage):
    pass


class Danke(Page):
    pass

class Einfuehrung(Page):
    pass

#page_sequence = [Narratives]
page_sequence = [Einfuehrung, Survey, Survey2, Survey3, Instructions,newCogMap, Narratives,Danke]
