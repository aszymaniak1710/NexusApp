from django.db import models

class Pochodzenie(models.Model):
    id_poch = models.AutoField(primary_key=True)
    miejsce_urodzenia = models.CharField(max_length=100)
    frakcja = models.CharField(max_length=100)

    def __str__(self):
        return self.miejsce_urodzenia


class RolaPostaci(models.Model):
    id_r = models.AutoField(primary_key=True)
    naz_roli = models.CharField(max_length=100)

    def __str__(self):
        return self.naz_roli


class Trudnosc(models.Model):
    koszt_be = models.IntegerField(primary_key=True)
    stopien_trudnosci = models.CharField(max_length=100)
    nazwa_rangi = models.ForeignKey("Ranga", on_delete=models.CASCADE)


class Zasoby(models.Model):
    id_zas = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa


class Obrazenia(models.Model):
    id_obr = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa


class Runy(models.Model):
    id_run = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=100)
    dzialanie = models.TextField()

    def __str__(self):
        return self.nazwa


class Linie(models.Model):
    id_lini = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa


class Postac(models.Model):
    id_p = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=100, unique=True)
    rasa = models.CharField(max_length=100)
    wiek = models.IntegerField()
    id_poch = models.ForeignKey(
        Pochodzenie,
        on_delete=models.CASCADE,
    )
    id_r = models.ForeignKey(
        RolaPostaci,
        on_delete=models.CASCADE,
    )
    koszt_be = models.ForeignKey(
        Trudnosc,
        on_delete=models.CASCADE,
    )
    data_wydania = models.DateField()
    id_zas = models.ForeignKey(
        Zasoby,
        on_delete=models.CASCADE,
    )
    id_obr = models.ForeignKey(
        Obrazenia,
        on_delete=models.CASCADE,
    )
    id_run = models.ForeignKey(
        Runy,
        on_delete=models.CASCADE,
    )
    id_lini = models.ForeignKey(
        Linie,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.nazwa


class UmiejetnosciPostaci(models.Model):
    id_p = models.ForeignKey(Postac, on_delete=models.CASCADE)
    id_u = models.AutoField(primary_key=True)
    przycisk = models.CharField(max_length=50)
    
class Umiejetnosci(models.Model):
    id = models.AutoField(primary_key=True)
    id_u = models.ForeignKey(UmiejetnosciPostaci, on_delete=models.CASCADE)
    nazwa = models.CharField(max_length=100)
    opis = models.TextField()

    def __str__(self):
        return self.nazwa



class Statystyki(models.Model):
    id_stat = models.AutoField(primary_key=True)
    nazwa = models.CharField(max_length=100)

    def __str__(self):
        return self.nazwa


class StatystykiPostaci(models.Model):
    id_p = models.ForeignKey(Postac, on_delete=models.CASCADE)
    id_stat = models.ForeignKey(Statystyki, on_delete=models.CASCADE)
    wartosc = models.FloatField()


class Wskaznik(models.Model):
    id_p = models.ForeignKey(Postac, on_delete=models.CASCADE)
    winrate = models.FloatField()
    banrate = models.FloatField()
    pickrate = models.FloatField()
    tier = models.CharField(max_length=50)


class Mapy(models.Model):
    nazwa = models.CharField(max_length=100, unique=True)
    ilosc_graczy = models.IntegerField()
    sr_czas_gry = models.IntegerField()
    opis_trybu = models.TextField()

    def __str__(self):
        return self.nazwa


class Ranga(models.Model):
    nazwa_rangi = models.CharField(max_length=100, primary_key=True)
    ilosc_graczy = models.IntegerField(default=0)
    procent_graczy = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        force_update_procent = kwargs.pop('force_update_procent', False)

        if force_update_procent:
            total_players = Ranga.objects.aggregate(total=models.Sum('ilosc_graczy'))['total'] or 0
            if total_players > 0:
                self.procent_graczy = (self.ilosc_graczy / total_players) * 100
            else:
                self.procent_graczy = 0.0

        super().save(*args, **kwargs)

    def __str__(self):
        return self.nazwa_rangi
