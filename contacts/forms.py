from django import forms
from .models import Contact
# , AddNote


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = [
            'name',
            'company_name',
            'address_1',
            'address_2',
            'city',
            'state',
            'zip_code',
            'phone_number',
            'email',
            'birthday',
            'add_note',
        ]

    # class AddNote(forms.ModelForm):
    #     class Meta:
    #         model = AddNote
    #         fields = [
    #         'add_note',
    #     ]
