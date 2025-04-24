from django.apps import AppConfig
from django.db.models.signals import post_migrate
from django.core.exceptions import ObjectDoesNotExist

def initialize_data(sender, **kwargs):
    from django.apps import apps

    Mapy = apps.get_model('NexusApp', 'Mapy')
    Ranga = apps.get_model('NexusApp', 'Ranga')
    Pochodzenie = apps.get_model('NexusApp', 'Pochodzenie')
    RolaPostaci = apps.get_model('NexusApp', 'RolaPostaci')
    Trudnosc = apps.get_model('NexusApp', 'Trudnosc')
    Zasoby = apps.get_model('NexusApp', 'Zasoby')
    Obrazenia = apps.get_model('NexusApp', 'Obrazenia')
    Runy = apps.get_model('NexusApp', 'Runy')
    Linie = apps.get_model('NexusApp', 'Linie')

    pochodzenia = [
        {"miejsce_urodzenia": "Demacia", "frakcja": "Demacia"},
        {"miejsce_urodzenia": "Noxus", "frakcja": "Noxus"},
        {"miejsce_urodzenia": "Ionia", "frakcja": "Ionia"},
        {"miejsce_urodzenia": "Piltover", "frakcja": "Piltover"},
        {"miejsce_urodzenia": "Zaun", "frakcja": "Zaun"},
        {"miejsce_urodzenia": "Freljord", "frakcja": "Freljord"},
    ]

    for pochodzenie in pochodzenia:
        Pochodzenie.objects.get_or_create(
            miejsce_urodzenia=pochodzenie["miejsce_urodzenia"],
            defaults={
                "frakcja": pochodzenie["frakcja"],
            }
        )
    
    role_postaci = [
        {"naz_roli": "Obrońca"},
        {"naz_roli": "Wojownik"},
        {"naz_roli": "Zabójca"},
        {"naz_roli": "Mag"},
        {"naz_roli": "Strzelec"},
        {"naz_roli": "Wspierający"},
    ]

    for rola in role_postaci:
        RolaPostaci.objects.get_or_create(
            naz_roli=rola["naz_roli"]
        )

    zasoby = [
        {"nazwa": "Mana"},
        {"nazwa": "Energia"},
        {"nazwa": "Inne"},
        {"nazwa": "Bez zasobów"},
    ]

    for zasob in zasoby:
        Zasoby.objects.get_or_create(
            nazwa=zasob["nazwa"]
        )

    obrazenia = [
        {"nazwa": "Magiczne"},
        {"nazwa": "Fizyczne"},
        {"nazwa": "Nieuchronne"},
    ]

    for obrazenie in obrazenia:
        Obrazenia.objects.get_or_create(
            nazwa=obrazenie["nazwa"]
        )

    runy = [
        {"nazwa": "Precyzja", "dzialanie": "Zwiększa obrażenia zadawane w długich walkach, skupiając się na wytrwałości i efektywności autoataków."},
        {"nazwa": "Dominacja", "dzialanie": "Koncentruje się na zadawaniu wysokich obrażeń w krótkim czasie, idealna dla zabójców i postaci zadających obrażenia w wybuchach."},
        {"nazwa": "Czarnoksięstwo", "dzialanie": "Zwiększa siłę umiejętności i zapewnia dodatkowe możliwości zadawania magicznych obrażeń."},
        {"nazwa": "Determinizacja", "dzialanie": "Zapewnia wytrzymałość, leczenie i ochronę, idealna dla obrońców i postaci wspierających."},
        {"nazwa": "Inspiracja", "dzialanie": "Dostarcza unikalnych efektów wspierających kreatywne i nietypowe style gry, takie jak skrócenie czasu odnowienia lub dodatkowe narzędzia strategiczne."},
    ]

    for runa in runy:
        Runy.objects.get_or_create(
            nazwa=runa["nazwa"],
            defaults={
                "dzialanie": runa["dzialanie"]
            }
        )

    linie = [
        {"nazwa": "Top"},
        {"nazwa": "Dżungla"},
        {"nazwa": "Mid"},
        {"nazwa": "Bot"},
    ]

    for linia in linie:
        Linie.objects.get_or_create(
            nazwa=linia["nazwa"]
        )

    ranks = [
        {"nazwa_rangi": "Iron", "ilosc_graczy": 1000},
        {"nazwa_rangi": "Bronze", "ilosc_graczy": 1000000},
        {"nazwa_rangi": "Silver", "ilosc_graczy": 3000000},
        {"nazwa_rangi": "Gold", "ilosc_graczy": 2000000},
        {"nazwa_rangi": "Platinum", "ilosc_graczy": 500000},
        {"nazwa_rangi": "Diamond", "ilosc_graczy": 25000},
        {"nazwa_rangi": "Master", "ilosc_graczy": 2500},
        {"nazwa_rangi": "Grandmaster", "ilosc_graczy": 500},
        {"nazwa_rangi": "Challenger", "ilosc_graczy": 200},
    ]


    
    total_players = sum(rank["ilosc_graczy"] for rank in ranks)

    for rank in ranks:
        procent_graczy = (rank["ilosc_graczy"] / total_players) * 100 if total_players > 0 else 0.0
        Ranga.objects.get_or_create(
            nazwa_rangi=rank["nazwa_rangi"],
            defaults={
                "ilosc_graczy": rank["ilosc_graczy"],
                "procent_graczy": round(procent_graczy, 2),
            }
        )

    trudnosci = [
        {"koszt_be": 450, "stopien_trudnosci": "Łatwy", "nazwa_rangi": "Iron"},
        {"koszt_be": 1350, "stopien_trudnosci": "Średni", "nazwa_rangi": "Bronze"},
        {"koszt_be": 3150, "stopien_trudnosci": "Trudny", "nazwa_rangi": "Silver"},
        {"koszt_be": 4800, "stopien_trudnosci": "Trudny", "nazwa_rangi": "Gold"},
        {"koszt_be": 6300, "stopien_trudnosci": "Ekspert", "nazwa_rangi": "Platinum"},
    ]

    for trudnosc in trudnosci:
        ranga = Ranga.objects.get(nazwa_rangi=trudnosc["nazwa_rangi"])
        Trudnosc.objects.get_or_create(
            koszt_be=trudnosc["koszt_be"],
            defaults={
                "stopien_trudnosci": trudnosc["stopien_trudnosci"],
                "nazwa_rangi": ranga
            }
        )
        
    Mapy.objects.get_or_create(
        nazwa="Howling Abyss",
        ilosc_graczy=5,
        sr_czas_gry=15,
        opis_trybu="Losowi bohaterowie cały czas na jednej linii!!!"
    )
    Mapy.objects.get_or_create(
        nazwa="Summoner`s Rift",
        ilosc_graczy=5,
        sr_czas_gry=25,
        opis_trybu="Kultowa mapa 5 na 5 w League of Legends. Poważna sprawa!"
    )
    Mapy.objects.get_or_create(
        nazwa="Twisted Treeline",
        ilosc_graczy=3,
        sr_czas_gry=15,
        opis_trybu="Kultowa mapa 3 na 3 w League of Legends."
    )
    
class NexusAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'NexusApp'

    def ready(self):
        post_migrate.connect(initialize_data, sender=self)
