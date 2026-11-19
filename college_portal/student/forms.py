from django import forms
class Studentformdata(forms.Form):
    reg_no1=forms.IntegerField()
    name1=forms.CharField()
    email1=forms.EmailField()