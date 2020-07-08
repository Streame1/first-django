from django.conf.urls import url

from polls.views import HomeView

urlpatterns = [
    url(r'^first-page/',HomeView.as_view(), name ="polls"),
]
