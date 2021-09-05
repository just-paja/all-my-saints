from django.db.models import Sum
from django.contrib import admin
from .models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'member_count', 'indulgence_count', 'compro_count')

    def indulgence_count(self, inst):
        res = inst.indulgences.aggregate(Sum('value'))
        return res['value__sum']

    def compro_count(self, inst):
        return inst.compro_items.count()

    def member_count(self, inst):
        return inst.members.count()

    compro_count.short_description = 'Compro'
    indulgence_count.short_description = 'Indulgences'
    member_count.short_description = 'Members'
