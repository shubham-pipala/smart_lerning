from django import forms
from . models import *
##### crete a form for note page like create a note to use this functions
class noteform(forms.ModelForm):

    ###The Meta inner class is used to provide additional settings 
    # for the form, such as which model to use and which fields to include.
    class Meta:
        model = notes
        fields = ['title','dis']
    ####This specifies which fields from the notes model should be included in the form.
    #Only title and dis fields will appear in the form.

### pip install django-crispy-forms ## for dirrfent form create elemet
class DateInput(forms.DateInput):
    input_type = 'date'


class workpage(forms.ModelForm):

    ###The Meta inner class is used to provide additional settings 
    # for the form, such as which model to use and which fields to include.
    class Meta:
        model = work
        widgets = {'due':DateInput()}
        fields = ['user','title','dis','due','subject','is_finished']

class todopage(forms.ModelForm):

    class Meta:
        model = todoo
        widgets = {'due':DateInput()}
        fields = ['user','title','is_finished']

class dashbord(forms.Form):  ## for youtube lable 
    ## jyaare table na banavtu hoy tyare forms.Form use thai che
    text = forms.CharField(max_length=50,label="enter youur serch : ")

# class dashbord(forms.Form):  ## for youtube lable 
#     ## jyaare table na banavtu hoy tyare forms.Form use thai che
#     text = forms.CharField(max_length=50,label="enter youur serch : ")