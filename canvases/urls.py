from django.urls import path
from . import views

urlpatterns = [
  path("canvas/", views.ListCreateCanvasView.as_view()),
  path("canvas/<str:canvas_id>/", views.RetrieveUpdateDestroyCanvasView.as_view()),
  path("canvas/getthecanva", views.GetTheCanva.as_view()),
]