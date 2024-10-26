from django import forms
from django.contrib.auth.models import User, Group
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class GerenteCadastroForm(UserCreationForm):
    groups = forms.ModelMultipleChoiceField(
        queryset=Group.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required= False
    )
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields= ['username','email','password1','password2','groups']
    
    def save(self, commit=True):
        user = super(GerenteCadastroForm, self).save(commit=False)
        if commit:
            user.save()
            # Após salvar o usuário, crie o perfil e defina must_change_password como True
            profile = Profile.objects.create(user=user)
            user.groups.set(self.cleaned_data['groups'])
            profile.must_change_password = True
            profile.save()
        return user

class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']