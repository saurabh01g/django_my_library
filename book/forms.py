from django import forms
from book.models import Book, Employee
# creating a form 

class FeedbackForm(forms.Form):
    name = forms.CharField(max_length = 200)
    feedback = forms.CharField(max_length = 1000)


class BookModelForm(forms.ModelForm):
    # specify the name of model to use
    class Meta:
        model = Book
        fields = ("name", "price",)



STATES = (
    ('', 'Choose...'),
    ('MH', 'Maharashtra'),
    ('MP', 'Madhya Pradesh'),
    ('RJ', 'Rajasthan')
)

class AddressForm(forms.Form):
    Name = forms.CharField(label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Enter your full name here.'}))
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter email id.'}))
    address_1 = forms.CharField(label='Address',widget=forms.TextInput(attrs={'placeholder': 'Enter address here.'}))
    address_2 = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Address line 2'}))
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)


class  ContactForm(forms.Form):
    first_name = forms.CharField(max_length = 200)
    last_name = forms.CharField(max_length = 200)
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter email id.'}))
    comment = forms.CharField(max_length = 1000)


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class EmployeeForm(forms.ModelForm):  
  
    class Meta:  
        model = Employee  
        fields = '__all__'  