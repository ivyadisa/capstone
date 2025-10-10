from django.urls import path
from .import views

urlpatterns = [

    # user authentication
    path('signup/', views.signup_views, name='signup'),
    path('login/', views.login_views, name ='login'),
    path('logout', views.logout_view, name ='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),

    # students urls
    path('', views.student_list, name='student_list'),
    path('students/<int:pk>/', views.student_detail, name='student_detail'),
    path('students/add/', views.student_create, name='student_create'),
    path('students/<int:pk>/edit/', views.student_update, name='student_update'),
    path('students/<int:pk>/delete/', views.student_delete, name='student_delete'),


]

