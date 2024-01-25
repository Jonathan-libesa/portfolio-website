# forms.py
from django import forms
from .models import*

class QuotationForm(forms.ModelForm):
    class Meta:
        model = Quotation
        fields = [ 'customer_name', 'customer_email','customer_Phone','message']


class QuotationForm1(forms.ModelForm):
    class Meta:
        model = Quotation1
        fields = [ 'customer_name', 'customer_email','customer_Phone','message']



class QuotationForm2(forms.ModelForm):
    class Meta:
        model = Quotation2
        fields = [ 'customer_name', 'customer_email','customer_Phone','message']