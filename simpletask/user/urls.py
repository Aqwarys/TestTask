from django.urls import path
from user.views import UserView
app_name = "user"

urlpatterns = [
    path('<int:pk>', UserView.as_view(), name='user'),
]
