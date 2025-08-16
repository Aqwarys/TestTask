from django.urls import path, include

from order import views

from rest_framework.routers import DefaultRouter

app_name = "order"

router = DefaultRouter()
router.register(r"", views.OrderModelViewSet)

urlpatterns = [
    path('', include(router.urls), name="order-list")
]
