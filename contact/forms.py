from django import forms

from contact.models import EmployerApplication, TouristApplication


class TouristApplicationForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Введите ваш e-mail'})
        self.fields['email'].label = 'Ваш e-mail'
        self.fields['health'].widget.attrs.update({
            'class': 'form-text',
            'placeholder': 'Расскажите о вашем здоровье, возможно, о каких-либо ограничениях'
        })
        self.fields['health'].label = 'Расскажите о вашем здоровье'
        self.fields['description'].widget.attrs.update({'class': 'form-text', 'placeholder': 'Расскажите о себе'})
        self.fields['description'].label = 'Расскажите о себе'
        self.fields['comment'].widget.attrs.update({'class': 'form-text', 'style': 'height: 150px;'})
        self.fields['comment'].label = 'Ваш коментарий'
    
    class Meta:
        model = TouristApplication
        fields = '__all__'


class EmployerApplicationForm(forms.ModelForm):

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class': 'form-input', 'placeholder': 'Введите ваш e-mail'})
        self.fields['email'].label = 'Ваш e-mail'
        self.fields['provision_kind'].widget.attrs.update({'class': 'form-select'})
        self.fields['provision_kind'].label = 'Что вы можете предоставить?'
        self.fields['description'].widget.attrs.update({
            'class': 'form-text',
            'placeholder': 'Расскажите о том, чем у вас будут заниматься туристы'
        })
        self.fields['comment'].widget.attrs.update({'class': 'form-text', 'style': 'height: 150px;'})
        self.fields['comment'].label = 'Ваш коментарий'
    
    class Meta:
        model = EmployerApplication
        fields = '__all__'
