from django import forms

from .models import Product, Usuario, Seguradora


class UsuarioForm(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['name', 'username', 'password',]


class UpdateSaldo(forms.ModelForm):
    
    class Meta:
        model = Usuario
        fields = ['saldo_num','products',]


class ProductForm(forms.ModelForm):
    name= forms.CharField(widget=forms.Textarea(attrs={'rows':1,'size':40,'placeholder':'Nome do Produto'}),max_length=100)
    product_desc = forms.CharField(
    widget=forms.Textarea(
            attrs={'rows': 8, 'placeholder': 'Qual vai ser a Descrição do seu produto?'}
        ),
        max_length=5000
    )

    class Meta:
        model = Product
        fields = ['name','product_desc', 'contract_num', 'sinistro_num', 'access_num' ,'gps_location','map_structure','timer_disposal','preco_display','preco_total','belongs_to',]





