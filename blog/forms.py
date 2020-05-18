from django import forms
from .models import Article, Inscription 

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    envoyeur = forms.EmailField(label="Votre adresse e-mail")
    renvoi = forms.BooleanField(help_text="cochez si vous souhaitez recevoir une copie du mail envoye.",required=False)

    """def clean_message(self):
        message = self.cleaned_data['message']
        if "betail" or "ferme" in message:
            raise forms.ValidationError("nous ne parlons pas de betail ou ferme ici")
        #renvoyer le contenu du champ traite
        return message
    """
    def clean(self):
        cleaned_data = super(ContactForm, self).clean()
        sujet = cleaned_data.get('sujet')
        message = cleaned_data.get('message')

        if sujet and message: #verifions d'abord si le sujet et le message sont valide
            if "betail" in sujet and "betail" in message:
                self.add_error("sujet",
                    "Nous ne parlons pas de sujet a propos de betail ici"

                )

        return cleaned_data

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        
class InscriptionForm(forms.ModelForm):
    #nom = forms.CharField()
    #adresse = forms.CharField(widget=forms.Textarea)
    #photo = forms.ImageField()
    class Meta:
        model = Inscription
        fields = '__all__'


    
