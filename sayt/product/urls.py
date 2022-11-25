from django.urls import path
from .views import Telefonlar_view, Telefonlar_detailview,AboutView,BoglanishView



urlpatterns = [
    path('', Telefonlar_view, name='Bosh_sahifa'),
    path('biz/',AboutView, name='bizxaqimizda'),
    path('bog/',BoglanishView,name='Boglanish'),
    path('xar1/<int:pk>/', Telefonlar_detailview, name='Xarakter2'),
]