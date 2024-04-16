from django.urls import path

from three.views import PageAPIView

urlpatterns = [
    path('pages/', PageAPIView.as_view()),
]