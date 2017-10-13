from django.contrib import admin
from .models import *


# Register your models here.

class BiodataAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'phone', 'marital_status', 'residence', 'state', 'email', 'gender')
    search_fields = ('full_name', 'state', 'lga', 'phone')
    fields = ['full_name', 'phone', 'marital_status', 'residence', 'state', 'lga', 'town', 'email', 'gender',
              'name_of_next_of_kin', 'address_of_next_of_kin', 'relation_with_next_of_kin']


admin.site.register(BioData, BiodataAdmin)


class SpecializationAdmin(admin.ModelAdmin):
    list_display = ('occupation', 'business_address', 'skills', 'sports')
    search_fields = ('occupation', 'skills', 'sports')
    fields = ['occupation', 'business_address', 'skills', 'sports']


admin.site.register(Specialization, SpecializationAdmin)


class SpiritualDataAdmin(admin.ModelAdmin):
    list_display = (
        'are_you_a_baptized_catholic', 'not_baptized', 'are_you_a_communicant', 'not_communicant', 'are_you_confirmed',
        'not_confirmed')
    search_fields = ('belongs_to_any_organ_in_church', 'member_of_any_pius_society', 'any_tribal_community')
    fields = ['are_you_a_baptized_catholic', 'not_baptized', 'are_wedded_in_the_church', 'not_wedded',
              'any_tribal_community', 'not_in_tribal_community', 'in_tribal_community', 'member_of_any_pius_society',
              'not_in_pius_society', 'yes_In_pius_society', 'belongs_to_any_organ_in_church', 'dont_belong_to',
              'yes_belong_to']


admin.site.register(SpiritualData, SpiritualDataAdmin)

class ChurchWorkHistoryAdmin(admin.ModelAdmin):
    list_display = ('catechetical_work', 'liturgical_work', 'security_work', 'environmental_work', 'health_work', 'sports', 'other_work')
    fields = ['catechetical_work', 'liturgical_work', 'security_work', 'environmental_work', 'health_work', 'sports', 'other_work']
admin.site.register(ChurchWorkHistory, ChurchWorkHistoryAdmin)

class PersonModelForm(admin.ModelAdmin):
    list_display = ('get_biodata', 'specialization', 'spiritual_data', 'church_work_history')
    fields = ['bio_data', 'specialization', 'spiritual_data', 'church_work_history']
    def get_biodata(self, obj):
        return obj.bio_data.full_name, obj.bio_data.gender
admin.site.register(Person, PersonModelForm)

