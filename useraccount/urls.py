from django.urls import path

from dj_rest_auth.jwt_auth import get_refresh_view
from dj_rest_auth.registration.views import RegisterView
from dj_rest_auth.views import LoginView, LogoutView, UserDetailsView
from rest_framework_simplejwt.views import TokenVerifyView

from useraccount.api import landlord_detail, my_reservations

urlpatterns = [
    path("register/", RegisterView.as_view(), name="rest_register"),
    path("login/", LoginView.as_view(), name="rest_login"),
    path("logout/", LogoutView.as_view(), name="rest_logout"),
    path("<uuid:pk>", landlord_detail, name="landlord-detail"),
    path("token/refresh", get_refresh_view, name="refresh-token"),
    path("reservations", my_reservations, name="reservations_list"),
]
