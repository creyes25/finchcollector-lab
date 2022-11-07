from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path("finches/", views.finches_index, name="finches_index"),
  path('finches/<int:finch_id>/', views.finchs_details, name='finchs_details'),
  path('finches/create/' , views.FinchCreate.as_view(), name='finchs_create'),
]

