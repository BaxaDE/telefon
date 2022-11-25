from pyexpat import model
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from .forms import ContactForms
from .models import TelefonlarModels,XususiyatModels,XarakteristikaModels,Bizhaqimizda,IjtimoitarmoqModels
from django.core.paginator import Paginator
# Create your views here.

def XarakteristikaView(request):
    xarakter = XarakteristikaModels.objects.all()
    print(xarakter)
    return render(request, 'product.html', {'posts': xarakter})


def XususiyatView(request):
    xususiyat = XususiyatModels.objects.all()
    print(xususiyat)
    return render(request, 'product.html', {'lists': xususiyat})


def Telefonlar_view(request):
    telefonlar = TelefonlarModels.objects.all()
    return render(request, "index.html", {"products": telefonlar})


def Telefonlar_detailview(request, pk:int):
    telefonlar = get_object_or_404(TelefonlarModels, pk=pk)
    xarakter = XarakteristikaModels.objects.filter(telefon=telefonlar)
    xususiyat = XususiyatModels.objects.filter(tel=telefonlar)
    context = {
        'product': telefonlar,
        'posts': xarakter,
        'lists': xususiyat,
    }
    return render(request, "product.html",context=context)

# def index_xar(request):
#     if request.method == 'POST':
#         form = Telefonlar_detailview(request.POST)
#         if form.is_valid():
#             dane = form.cleaned_data
#             tlumaczenie=XarakteristikaModels.objects.filter(Tel__tel_text=dane['Searched_tel'])
#             print(tlumaczenie)
#             return render(request,'product.html', {'dane':dane})
#
# def index_xus(request):
#     if request.method == 'POST':
#         form = Telefonlar_detailview(request.POST)
#         if form.is_valid():
#             dane = form.cleaned_data
#             tlumaczenie=XususiyatModels.objects.filter(Tel__tel_text=dane['Searched_tel'])
#             print(tlumaczenie)
#             return render(request,'product.html', {'dane':dane})



class IjtimoitarmogView(ListView):
    class Meta:
        model = IjtimoitarmoqModels
        queryset = IjtimoitarmoqModels.objects.all()
        template_name = 'base.html'
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context
    # context = {
    #     'gets': get
    # }
    # return render(request, 'base.html', context=context)



def BoglanishView(request):
    context = {}
    if request.method == 'POST':
        pass
    else:
        form = ContactForms()
    context['form'] = form
    return render(request,'contact.html',context)

def AboutView(request):
    post = Bizhaqimizda.objects.last()
    return render(request, 'about.html', {'post': post.description})

# # Paginator
# class ContactListView(ListView):
#     paginate_by = 4
#     model = Telefonlar_detailview
    
def listing(request):
    contact_list = Telefonlar_view.objects.all()
    paginator = Paginator(contact_list, 6) # Show 25 contacts per page.

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj
    }
    return render(request, 'index.html', context=context)   