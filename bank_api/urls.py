from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from main.views import (CustomerViewSet,
                        AccountViewSet,
                        AccountBalance,
                        ReplenishmentView,
                        OutlayView,)


router = routers.DefaultRouter()
router.register(r'customer', CustomerViewSet)
router.register(r'account', AccountViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/balance/', AccountBalance.as_view()),
    path('account/replenishment/', ReplenishmentView.as_view()),
    path('account/outlay/', OutlayView.as_view()),
    path('', include(router.urls))
]
