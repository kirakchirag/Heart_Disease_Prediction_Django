from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="home"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('logout', views.log_out, name="logout"),
    path('module1', views.module1, name='module1'),
    path('module2', views.module2, name='module2'),
    path('module3', views.module3, name='module3'),
    path("view_result", views.view_results, name="results")

]
