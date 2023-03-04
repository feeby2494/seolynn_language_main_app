from django.urls import include, path
from .views import secret, Public


urlpatterns = [
    path("secret/", secret, name="secret"),
    path('public/', Public.as_view(), name="public"),
]