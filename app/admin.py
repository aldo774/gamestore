from django.contrib import admin
from .models import Plataforma, Item, Cadastro, CadastroPF, CadastroPJ, Vis, Contato

admin.site.register(Contato)
admin.site.register(Vis)
admin.site.register(Plataforma)
admin.site.register(Item)
admin.site.register(Cadastro)
admin.site.register(CadastroPF)
admin.site.register(CadastroPJ)