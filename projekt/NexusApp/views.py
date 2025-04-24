
from django.shortcuts import render, get_object_or_404, redirect
from .models import *


def character_details(request, id_p):
    character = get_object_or_404(Postac, pk=id_p)
    umiejetnosci_postaci = UmiejetnosciPostaci.objects.filter(id_p=character)
    statystyki = StatystykiPostaci.objects.filter(id_p=character)
    umiejetnosci = []
    for up in umiejetnosci_postaci:
        umiejetnosc = Umiejetnosci.objects.filter(id_u=up.id_u).first()
        umiejetnosci.append({
            'przycisk': up.przycisk,
            'nazwa': umiejetnosc.nazwa,
            'opis': umiejetnosc.opis,
        })
    return render(request, 'character_details.html', {
        'character': character,
        'umiejetnosci': umiejetnosci,
        'statystyki': statystyki,
    })
    
def delete_character(request, id_p):
    character = get_object_or_404(Postac, pk=id_p)
    character.delete()
    return redirect('display_characters')

def add_character(request):
    if request.method == 'POST':
        nazwa = request.POST.get('nazwa')
        rasa = request.POST.get('rasa')
        wiek = request.POST.get('wiek')
        id_poch = request.POST.get('id_poch')
        id_r = request.POST.get('id_r')
        koszt_be = request.POST.get('koszt_be')
        data_wydania = request.POST.get('data_wydania')
        id_zas = request.POST.get('id_zas')
        id_obr = request.POST.get('id_obr')
        id_run = request.POST.get('id_run')
        id_lini = request.POST.get('id_lini')

        umiejetnosci = [
            {'nazwa': request.POST.get('umiejetnosc_q_nazwa'), 'opis': request.POST.get('umiejetnosc_q_opis')},
            {'nazwa': request.POST.get('umiejetnosc_w_nazwa'), 'opis': request.POST.get('umiejetnosc_w_opis')},
            {'nazwa': request.POST.get('umiejetnosc_e_nazwa'), 'opis': request.POST.get('umiejetnosc_e_opis')},
            {'nazwa': request.POST.get('umiejetnosc_r_nazwa'), 'opis': request.POST.get('umiejetnosc_r_opis')}
        ]

        statystyki = [
            {'nazwa': 'HP', 'wartosc': request.POST.get('stat_hp')},
            {'nazwa': 'Mana', 'wartosc': request.POST.get('stat_mana')},
            {'nazwa': 'AD', 'wartosc': request.POST.get('stat_ad')},
            {'nazwa': 'AP', 'wartosc': request.POST.get('stat_ap')}
        ]

        postac = Postac.objects.create(
            nazwa=nazwa,
            rasa=rasa,
            wiek=int(wiek),
            id_poch=get_object_or_404(Pochodzenie, pk=id_poch),
            id_r=get_object_or_404(RolaPostaci, pk=id_r),
            koszt_be=get_object_or_404(Trudnosc, pk=koszt_be),
            data_wydania=data_wydania,
            id_zas=get_object_or_404(Zasoby, pk=id_zas),
            id_obr=get_object_or_404(Obrazenia, pk=id_obr),
            id_run=get_object_or_404(Runy, pk=id_run),
            id_lini=get_object_or_404(Linie, pk=id_lini)
        )

        przyciski = ['Q', 'W', 'E', 'R']
        for idx, przycisk in enumerate(przyciski):
            umiejetnosc_postaci = UmiejetnosciPostaci.objects.create(
                id_p=postac,
                przycisk=przycisk
            )
            Umiejetnosci.objects.create(
                id_u=umiejetnosc_postaci,
                nazwa=umiejetnosci[idx]['nazwa'],
                opis=umiejetnosci[idx]['opis']
            )
        for stat in statystyki:
            statystyka = Statystyki.objects.get_or_create(nazwa=stat['nazwa'])[0]
            StatystykiPostaci.objects.create(
                id_p=postac,
                id_stat=statystyka,
                wartosc=stat['wartosc']
            )

        return redirect('display_characters')

    return render(request, 'add_character.html', {
        'pochodenia': Pochodzenie.objects.all(),
        'role': RolaPostaci.objects.all(),
        'trudnosci': Trudnosc.objects.all(),
        'zasoby': Zasoby.objects.all(),
        'obrazenia': Obrazenia.objects.all(),
        'runy': Runy.objects.all(),
        'linie': Linie.objects.all(),
    })

def modify_character(request, id_p):
    character = get_object_or_404(Postac, pk=id_p)
    umiejetnosci_postaci = UmiejetnosciPostaci.objects.filter(id_p=character)
    statystyki = StatystykiPostaci.objects.filter(id_p=character)
    umiejetnosci = []
    for up in umiejetnosci_postaci:
        umiejetnosc = Umiejetnosci.objects.filter(id_u=up.id_u).first()
        umiejetnosci.append({
            'przycisk': up.przycisk,
            'nazwa': umiejetnosc.nazwa,
            'opis': umiejetnosc.opis,
        })
    if request.method == 'POST':
        
        character.nazwa = request.POST.get('nazwa', character.nazwa)
        character.rasa = request.POST.get('rasa', character.rasa)
        character.wiek = int(request.POST.get('wiek', character.wiek))
        character.id_poch_id = request.POST.get('id_poch', character.id_poch.id_poch)
        character.id_r_id = request.POST.get('id_r', character.id_r.id_r)
        character.koszt_be_id = request.POST.get('koszt_be', character.koszt_be.koszt_be)
        character.data_wydania = request.POST.get('data_wydania', character.data_wydania)
        character.id_zas_id = request.POST.get('id_zas', character.id_zas.id_zas)
        character.id_obr_id = request.POST.get('id_obr', character.id_obr.id_obr)
        character.id_run_id = request.POST.get('id_run', character.id_run.id_run)
        character.id_lini_id = request.POST.get('id_lini', character.id_lini.id_lini)
        character.save()

        for umiejetnosc_postaci in umiejetnosci_postaci:
            print(umiejetnosc_postaci.id_u)
            umiejetnosc = Umiejetnosci.objects.filter(id_u=umiejetnosc_postaci.id_u).first()
            print(umiejetnosc.id_u)
            umiejetnosc.nazwa = request.POST.get(f'umiejetnosc_{umiejetnosc_postaci.przycisk.lower()}_nazwa', umiejetnosc.nazwa)
            umiejetnosc.opis = request.POST.get(f'umiejetnosc_{umiejetnosc_postaci.przycisk.lower()}_opis', umiejetnosc.opis)
            print(umiejetnosc.nazwa)
            umiejetnosc.save()

        statystyki_nazwy = ['HP', 'Mana', 'AD', 'AP']
        for idx, statystyka_postaci in enumerate(statystyki):
            statystyka_postaci.wartosc = request.POST.get(f'stat_{statystyki_nazwy[idx].lower()}', statystyka_postaci.wartosc)
            statystyka_postaci.save()

        return redirect('character_details', id_p=character.id_p)

    return render(request, 'modify_character.html', {
        'character': character,
        'umiejetnosci': umiejetnosci,
        'statystyki': statystyki,
        'pochodenia': Pochodzenie.objects.all(),
        'role': RolaPostaci.objects.all(),
        'trudnosci': Trudnosc.objects.all(),
        'zasoby': Zasoby.objects.all(),
        'obrazenia': Obrazenia.objects.all(),
        'runy': Runy.objects.all(),
        'linie': Linie.objects.all(),
    })

# Modyfikowanie mapy
def modify_map(request, id_map):
    map_instance = get_object_or_404(Mapy, pk=id_map)
    if request.method == 'POST':
        map_instance.nazwa = request.POST['nazwa']
        map_instance.ilosc_graczy = request.POST['ilosc_graczy']
        map_instance.sr_czas_gry = request.POST['sr_czas_gry']
        map_instance.opis_trybu = request.POST['opis_trybu']
        map_instance.save()
        return redirect('display_maps')
    return render(request, 'modify_map.html', {'map': map_instance})


def przelicz_procenty():
    from .models import Ranga
    total_players = Ranga.objects.aggregate(total=models.Sum('ilosc_graczy'))['total'] or 0

    if total_players > 0:
        for rank in Ranga.objects.all():
            rank.procent_graczy = (rank.ilosc_graczy / total_players) * 100
            rank.save(force_update_procent=False)

def home(request):
    return render(request, 'home.html')


def display_characters(request):
    characters = Postac.objects.all()
    return render(request, 'characters.html', {'characters': characters})


def display_maps(request):
    maps = Mapy.objects.all()
    return render(request, 'maps.html', {'maps': maps})


def display_ranks(request):
    if request.method == "POST" and "update_rank" in request.POST:
        nazwa_rangi = request.POST["update_rank"]
        ilosc_graczy = int(request.POST.get(f"ilosc_graczy_{nazwa_rangi}"))
        rank = Ranga.objects.get(nazwa_rangi=nazwa_rangi)
        rank.ilosc_graczy = ilosc_graczy
        rank.save(force_update_procent=False)
        przelicz_procenty()
        return redirect("display_ranks")

    ranks = Ranga.objects.all()
    return render(request, "ranks.html", {"ranks": ranks})


def display_roles(request):
    roles = RolaPostaci.objects.all()
    return render(request, 'roles.html', {'roles': roles})


def delete_role(request, id_r):
    role = get_object_or_404(RolaPostaci, pk=id_r)
    role.delete()
    return redirect('display_roles')


def add_role(request):
    if request.method == 'POST':
        naz_roli = request.POST.get('naz_roli')
        if naz_roli:
            RolaPostaci.objects.create(naz_roli=naz_roli)
    return redirect('display_roles')