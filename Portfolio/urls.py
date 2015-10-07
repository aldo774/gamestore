from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Examples:
    # url(r'^$', 'Portfolio.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('app.urls', namespace="item")),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^imagens/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT,}),
]