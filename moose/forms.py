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
         except: # XXX: should only catch itemnotfound exceptions
             q = None
         if q:
             raise forms.ValidationError("That name is already in use.  Try another?")
         return sname
            


class AddFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = ['date', 'sender']

class AddSenderForm(forms.ModelForm):
    email = forms.EmailField(required=False)
    status = forms.CharField(required=False)
    
    class Meta:
        model = Sender

    def save(self):
        print "save!", self.cleaned_data
        cd = self.cleaned_data
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
    feedback = forms.ModelChoiceField(queryset=Feedback.objects.all(),
                                      widget=forms.HiddenInput(), required=False,
                                      validators=[])
    
    class Meta:
        model = Message
        exclude = ['date']
