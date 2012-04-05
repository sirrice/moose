from django import forms
from models import *


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['user', 'date']

    def clean_shortname(self):
         sname = self.cleaned_data['shortname'].strip()
         try:
             q = Question.objects.get(shortname = sname)
         except:
             q = None
         if not q:
             raise forms.ValidationError("That name is already in use.  Try another?")
         return sname
            

            


class AddFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['date', 'sender']
