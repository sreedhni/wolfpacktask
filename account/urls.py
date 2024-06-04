from django.urls import path
from account.views import UserRegistrationAPIView,UserLoginView

urlpatterns = [
    path(
        'register/',
        UserRegistrationAPIView.as_view(),
        name='register',
    ),
    path(
        'login/',
        UserLoginView.as_view(),
        name='login',
    )


]
