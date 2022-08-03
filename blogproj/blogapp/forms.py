from django import forms

class NewPostForm(forms.Form):
    possible_states = (
        ('published', 'Publicar'),
        ('draft', 'Mantener en borradores'),
    )
    post_title = forms.CharField(label='Título', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Escriba un título para su post', 'class' : 'form-control', 'id' : 'titlebox'}))
    post_body = forms.CharField(label='Cuerpo', required=True, widget=forms.Textarea(attrs={'placeholder' : 'Escriba su post', 'class' : 'form-control'}))
    post_action = forms.ChoiceField(label='Acción', required=True, choices=possible_states, widget=forms.Select(attrs={'class' : 'form-control'}))

class AuthForm(forms.Form):
    username = forms.CharField(label='Usuario', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Usuario', 'class' : 'form-control'}))
    password = forms.CharField(label='Contraseña', required=True, max_length=100, widget=forms.PasswordInput(attrs={'placeholder' : 'Contraseña', 'class' : 'form-control', 'type' : 'password'}))

class NewUserForm(forms.Form):
    firstname = forms.CharField(label='Nombre', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Nombre', 'class' : 'form-control'}))
    lastname = forms.CharField(label='Apellido', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Apellido', 'class' : 'form-control'}))
    email = forms.EmailField(label='Email', required=True, max_length=100, widget=forms.EmailInput(attrs={'placeholder' : 'Email', 'class' : 'form-control'}))
    username = forms.CharField(label='Usuario', required=True, max_length=100, widget=forms.TextInput(attrs={'placeholder' : 'Usuario', 'class' : 'form-control'}))
    password = forms.CharField(label='Contraseña', required=True, max_length=100, widget=forms.PasswordInput(attrs={'placeholder' : 'Contraseña', 'class' : 'form-control', 'type' : 'password'}))