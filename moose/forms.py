from django import forms
from models import *


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['date']

    def clean_shortname(self):
        sname = self.cleaned_data['shortname'].strip()
        try:
            q = Question.objects.get(shortname = sname)
        except:
            q = None
        if q:
            raise forms.ValidationError("duplicate short name found")
        return sname
            

            


class AddFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['date']
