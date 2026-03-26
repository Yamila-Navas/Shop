from django import forms
from localflavor.us.forms import USZipCodeField
from django.utils.translation import gettext_lazy as _
from .models import Order


class OrderCreateForm(forms.ModelForm):
    postal_code = USZipCodeField(label=_('Postal code'))

    class Meta:
        model = Order
        fields = ['first_name', 'last_name', 'email', 'address', 'postal_code', 'city']
        labels = {
            'first_name': _('First name'),
            'last_name': _('Last name'),
            'email': _('Email'),
            'address': _('Address'),
            'city': _('City'),
        }
