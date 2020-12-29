from django.contrib import admin
from django.urls import path
from mainsite.views import homepage, lotto, showpost, mychart , chart, temperture,temperture1,temperture2,temperture3,temperture4,temperture5,temperture6,temperture7,temperture8,temperture9,temperture10,temperture11,temperture12,temperture13,temperture14,temperture15,temperture16,temperture17,temperture18,temperture19
from mainsite import views

urlpatterns = [
    path('post/<str:slug>/', showpost),
    path('list/<int:id>/', views.showlist),
    path('admin/', admin.site.urls),
    path('playlist/', views.playlist),
    path('lotto/', lotto),
    path('mychart/', mychart),
    path('mychart/<int:bid>/', mychart),
    path('income_month/<int:year>/<int:month>/', chart ),
    path('', homepage),
    path('temperture/', temperture),
    path('temperture1/', temperture1),
    path('temperture2/', temperture2),
    path('temperture3/', temperture3),
    path('temperture4/', temperture4),
    path('temperture5/', temperture5),
    path('temperture6/', temperture6),
    path('temperture7/', temperture7),
    path('temperture8/', temperture8),
    path('temperture9/', temperture9),
    path('temperture10/', temperture10),
    path('temperture11/', temperture11),
    path('temperture12/', temperture12),
    path('temperture13/', temperture13),
    path('temperture14/', temperture14),
    path('temperture15/', temperture15),
    path('temperture16/', temperture16),
    path('temperture17/', temperture17),
    path('temperture18/', temperture18),
    path('temperture19/', temperture19),
]
