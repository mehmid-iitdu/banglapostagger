from django.contrib import admin
# from django.contrib.auth import views
from django.urls import include, path
from pos_tagger import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('resource/', views.resource, name='resource'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('stats/', views.stats, name='stats'),
    path('accounts/', include('accounts.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('api/save/', views.save_sentence_tag, name='api_save'),
]