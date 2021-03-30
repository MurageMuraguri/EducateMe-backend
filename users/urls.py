from django.conf.urls import url
from users.views import UserRegistrationView
from users.views import UserLoginView


urlpatterns = [
    url(r'^signup', UserRegistrationView.as_view()),
    url(r'^login', UserLoginView.as_view()),
    ]