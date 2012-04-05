from django import forms
from models import *


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        exclude = ['user', 'date']

    def clean_shortname(self):
         sname = self.cleaned_data['shortname'].strip()
         if not SHORTNAME_REGEX.match(sname):
             raise forms.ValidationError("We only allow lowercase letters, numbers, -, and _ in our URLs.")
         try:
             q = Question.objects.get(shortname = sname)
         except:
             q = None
         if q:
             raise forms.ValidationError("That name is already in use.  Try another?")
         return sname
            


class AddFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['date', 'sender']

class AddSenderForm(forms.ModelForm):
    class Meta:
        model = Sender

    def clean(self):
        cd = super(AddSenderForm, self).clean()

        email = cd['email'].strip()
        if email:
            try:
                u = User.objects.get(email=email)
                cd['user'] = u
                cd['status'] = 'user'
            except:
                pass
            cd['email'] = email
            cd['status'] = 'email'
        else:
            cd['email'] = None
            cd['status'] = 'anon'
        
        return cd

class AddMessageForm(forms.ModelForm):
    class Meta:
        model = Message
        exclude = ['date']
