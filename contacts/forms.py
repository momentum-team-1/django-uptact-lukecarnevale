from django import forms
from .models import Contact, Note


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

    class NoteForm(forms.ModelForm):
        class Meta:
            model = Note
            fields = [
            'text',
        ]
