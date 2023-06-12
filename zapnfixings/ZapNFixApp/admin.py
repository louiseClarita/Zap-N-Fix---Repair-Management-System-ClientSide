from django.contrib import admin
from django.forms import inlineformset_factory
from django import forms
from django.forms.models import BaseInlineFormSet

from . import models
from .models import Repair, User, Type, Brand, Component, Problem

# Register your models here.
admin.site.register(Repair)
admin.site.register(User)
admin.site.register(Type)
# admin.site.register(Brand)
admin.site.register(Component)
admin.site.register(Problem)

from django import forms
from .models import Brand, Type

from django import forms
from .models import Brand


class BrandForm(forms.ModelForm):
    type_desc = forms.ModelChoiceField(queryset=Type.objects.all(), empty_label=None, to_field_name='desc',
                                       label='Type')

    class Meta:
        model = Brand
        fields = ['desc', 'type_desc']

    def save(self, commit=True):
        brand = super().save(commit=False)
        type_desc = self.cleaned_data['type_desc']
        # Create or get the Type instance based on the selected type_desc
        type_instance, _ = Type.objects.get_or_create(desc=type_desc)
        brand.type_id = type_instance
        if commit:
            brand.save()
        return brand


class BrandAdmin(admin.ModelAdmin):
    form = BrandForm


admin.site.register(Brand, BrandAdmin)
