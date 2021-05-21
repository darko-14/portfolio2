from django.urls import path
from .views import WorkView, WorkDetailsAPIView

urlpatterns = [
    path('', WorkView.as_view()),
    path('<int:id>', WorkDetailsAPIView.as_view()),
]