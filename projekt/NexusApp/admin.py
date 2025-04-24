# ADMIN

from django.contrib import admin

from .models import *

admin.site.register(Postac)
admin.site.register(Pochodzenie)
admin.site.register(RolaPostaci)
admin.site.register(Trudnosc)
admin.site.register(Umiejetnosci)
admin.site.register(StatystykiPostaci)
admin.site.register(Statystyki)
admin.site.register(Wskaznik)
admin.site.register(Runy)
admin.site.register(Mapy)
admin.site.register(Ranga)
admin.site.register(Zasoby)
admin.site.register(Obrazenia)
admin.site.register(Linie)
admin.site.register(UmiejetnosciPostaci)

class RangaAdmin(admin.ModelAdmin):
    list_display = ('nazwa_rangi', 'ilosc_graczy', 'procent_graczy')
    readonly_fields = ('procent_graczy',)
