import re
from django import forms

from BlogApp.models import Article


class UpdateEmailForm(forms.Form):
    email = forms.EmailField(max_length=225, widget=forms.TextInput(attrs={'class': 'peer w-full rounded-lg border-none bg-transparent p-4 text-left placeholder-transparent focus:outline-none focus:ring-0'}))


class UpdatePhoneForm(forms.Form):
    phone = forms.CharField(max_length=11, widget=forms.TextInput(attrs={'class': 'peer w-full rounded-lg border-none bg-transparent px-4 py-3 text-left placeholder-transparent focus:outline-none focus:ring-0'}))

    def clean_phone(self):
        phone = self.cleaned_data.get('phone')
        pattern = r'^\d{11}$'
        if re.match(pattern, phone):
            return phone
        else:
            raise forms.ValidationError('ورودی معتبر نیست. لطفا یک شماره تلفن 11 رقمی وارد کنید.')


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'body', 'image', 'category', 'tags', 'status']
