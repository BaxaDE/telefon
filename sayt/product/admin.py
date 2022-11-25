from django.contrib import admin
# from django.contrib.admin import ModelAdmin
# from django.forms import ModelForm

from .models import TelefonlarModels, XarakteristikaModels,Chegirmalar, Tel_Rasmlari,IjtimoitarmoqModels,Bizhaqimizda,XususiyatModels

admin.site.site_header = 'TexnoUp'
admin.site.site_title = 'TexnoUp ADMIN'


# class NewsForm(ModelForm):
#     class Meta:
#         model = XarakteristikaModels
#
# class NewsAdmin(ModelAdmin):
#
#     form = NewsForm
#
#     search_fields = ['full_name',
#                      'Xarakter_name']
#     list_filter = ('Xarakter_name',
#                    'active'
#                    )



admin.site.register(TelefonlarModels)
admin.site.register(XarakteristikaModels)
admin.site.register(Chegirmalar)
admin.site.register(Tel_Rasmlari)
admin.site.register(IjtimoitarmoqModels)
admin.site.register(Bizhaqimizda)
admin.site.register(XususiyatModels)

