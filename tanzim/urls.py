from django.contrib import admin
from django.urls import path, include

from chart.views import IndexView, GetIBBData
from chart.api.routers import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('get-ibb-data/', GetIBBData),
    #path('', include('chart.api.urls')),
    path('api/', include(router.urls))
]
