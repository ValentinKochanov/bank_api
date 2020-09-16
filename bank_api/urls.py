from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from main.views import (CustomerViewSet,
                        AccountViewSet,
                        AccountBalance,
                        ReplenishmentView,
                        OutlayView)


router = routers.DefaultRouter()
router.register(r'customers', CustomerViewSet)
router.register(r'accounts', AccountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/balance/', AccountBalance.as_view(), name='balance'),
    path('accounts/replenishment/', ReplenishmentView.as_view(), name='replenishment'),
    path('accounts/outlay/', OutlayView.as_view(), name='outlay'),
    path('', include(router.urls))
]
