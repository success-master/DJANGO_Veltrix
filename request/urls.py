
from .import views
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import CreateRequest, RequestDetail, RequestDeleteView, RequestUpdateView, RequestStatusUpdateView



urlpatterns = [
    # path('', views.login),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('', auth_views.LoginView.as_view(template_name='request/login.html'), name='login'),
    path('new/', CreateRequest.as_view(), name='new-request'),
    path('detail/<int:pk>/', RequestDetail.as_view(), name='request_detail'),
    path('request/<int:pk>/update/', RequestUpdateView.as_view(template_name='request/request_update.html'), name='request_update'),
    path('status/<int:pk>/update/', RequestStatusUpdateView.as_view(template_name='request/status_update.html'), name='status_update'),
    path('request/<int:pk>/delete/', RequestDeleteView.as_view(), name='request_delete'),

    # path('new/', views.CreateRequest, name='new-request'),

    #OUTGOING REQUESTS
    path('outgoing/', views.out_requests, name='outgoing'),
    path('outprogress/', views.out_requests_in_progress, name='outprogress'),
    path('complete/', views.out_complete, name='out_complete'),



    #INCOMING REQUESTS
    path('incoming/', views.in_requests, name='incoming'),
    path('inprogress/', views.in_requests_progress, name='incoming_progress'),
    path('in_complete/', views.in_requests_complete, name='incoming_complete'),

]
