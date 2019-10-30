from django.forms import ModelForm
from typing import List
from .models import Produtos


class ProdutosForm(ModelForm):
    class Meta:
        model = Produtos
        fields: List[str] = ['descricao','tipo','valor']