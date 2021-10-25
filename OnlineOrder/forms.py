from .models import OnlineContact, OnlineOrders
from django import forms

class messageform(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-name', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
        }
    ))
    surname = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-sec-name', 
            'type': 'text',
            'name': 'sec-name',
            'data-constraints': '@Required',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-email', 
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Email @Required',
        }
    ))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-phone', 
            'type': 'text',
            'name': 'phone',
            'data-constraints': '@Numeric @Required',
        }
    ))
    message = forms.CharField(max_length=1000, widget=forms.Textarea(
        attrs = {
            'class': 'form-input',
            'id': 'contact-message', 
            'type': 'text',
            'name': 'message',
            'data-constraints': '@Required',
        }
    ))
    class Meta:
        model = OnlineContact
        fields = '__all__'

products = [
    ('Coffee in the Morning Body Exfoliant', 'Coffee in the Morning Body Exfoliant'),
    ('Hello Sunshine Body Exfoliant', 'Hello Sunshine Body Exfoliant'),
    ('Botanical Gardens Bath Soak', 'Botanical Gardens Bath Soak'),
    ('Spicy Oatmeal Latte Bath Soak', 'Spicy Oatmeal Latte Bath Soak'),
    ('Soft Linen Luxury Hand & Body Cream', 'Soft Linen Luxury Hand & Body Cream'),
    ('Hello Sunshine Handcrafted soaps', 'Hello Sunshine Handcrafted soaps'),
    ('Oatmeal & Rooibos Latte Handcrafted Soapm', 'Oatmeal & Rooibos Latte Handcrafted Soapm'),
    ('Fluffy Clouds Luxury Hand & Body Cream', 'Fluffy Clouds Luxury Hand & Body Cream'),
]

class orderform(forms.ModelForm):
    name = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-name', 
            'type': 'text',
            'name': 'name',
            'data-constraints': '@Required',
        }
    ))
    surname = forms.CharField(max_length=50, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-sec-name', 
            'type': 'text',
            'name': 'sec-name',
            'data-constraints': '@Required',
        }
    ))
    email = forms.EmailField(widget=forms.EmailInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-email', 
            'type': 'email',
            'name': 'email',
            'data-constraints': '@Email @Required',
        }
    ))
    phone = forms.CharField(max_length=10, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-phone', 
            'type': 'text',
            'name': 'phone',
            'data-constraints': '@Numeric @Required',
        }
    ))
    address = forms.CharField(max_length=200, widget=forms.TextInput(
        attrs = {
            'class': 'form-input',
            'id': 'contact-address', 
            'type': 'text',
            'name': 'address',
            'data-constraints': '@Required',
        }
    ))
    products_selection = forms.MultipleChoiceField(choices=products, widget=forms.CheckboxSelectMultiple, required=True)
    class Meta:
        model = OnlineOrders
        fields = '__all__'