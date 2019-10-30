from django.shortcuts import render
from .forms import ProdutosForm
from django.utils.html import format_html

# Create your views here.
def index(request):
    return render(request,'index.html')

def new_produto(request):
    if request.method == "POST":
        form = ProdutosForm(request.POST)
        if form.is_valid():
            form.save()
            command = format_html("<h1>Cadastro OK</h1>")
            context = {'form': form, 'alert':command}
            return render(request, 'cadprod.html',{'form':form})
    else:
        form = ProdutosForm()
    return render(request, 'cadprod.html', {'form':form})
