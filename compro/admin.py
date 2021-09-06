from django.db.models import Sum
from django.contrib import admin

from . import models


class TeamMemberAdmin(admin.StackedInline):
    model = models.TeamMember


@admin.register(models.Team)
class TeamAdmin(admin.ModelAdmin):
    inlines = [TeamMemberAdmin]
    list_display = ('name', 'member_count', 'indulgence_count',
                    'self_compro_count', 'acquired_compro_count')

    def acquired_compro_count(self, inst):
        res = inst.compro_acquisitions.aggregate(Sum('compro__value'))
        return res['compro__value__sum']

    def indulgence_count(self, inst):
        res = inst.indulgences.aggregate(Sum('value'))
        return res['value__sum']

    def member_count(self, inst):
        return inst.members.count()

    def self_compro_count(self, inst):
        return inst.documentation_items.count()

    acquired_compro_count.short_description = 'Acquired Documentation'
    indulgence_count.short_description = 'Indulgences'
    member_count.short_description = 'Members'
    self_compro_count.short_description = 'Self Documentation'


@admin.register(models.Indulgence)
class IndulgenceAdmin(admin.ModelAdmin):
    list_display = ('team', 'value', 'comment')


class DocumentationMediaAdmin(admin.TabularInline):
    model = models.DocumentationMedia


@admin.register(models.Documentation)
class TeamComproAdmin(admin.ModelAdmin):
    list_display = ('team', 'title', 'media_count')
    inlines = [DocumentationMediaAdmin]

    def media_count(self, inst):
        return inst.media.count()


@admin.register(models.HollyCompro)
class HollyComproAdmin(admin.ModelAdmin):
    list_display = ('title', 'value', 'lat', 'lng', 'acquisition_count')
    prepopulated_fields = {'slug': ('title', )}

    def acquisition_count(self, inst):
        return inst.acquisitions.count()


@admin.register(models.HollyComproAcquisition)
class HollyComproAcquisitionAdmin(admin.ModelAdmin):
    list_display = ('compro', 'team', 'value')

    def value(self, inst):
        return inst.compro.value
