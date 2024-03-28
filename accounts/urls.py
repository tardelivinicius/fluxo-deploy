from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from accounts.views import AccountView

router = routers.DefaultRouter()
# Contas bancárias
router.register(r'', AccountView, basename='accounts')
urlpatterns = [
    path(r'/', include(router.urls))
]