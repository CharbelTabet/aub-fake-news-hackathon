from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard.as_view(), name='dashboard'),
    path('defaultdashboard/', views.defaultDashboard.as_view(), name='defaultDashboard'),
    path('topics/', views.topics.as_view(), name='empty'),
    path('community/', views.community.as_view(), name='community'),
    path('chatbot/', views.chatbot.as_view(), name='chatbot'),
    path('stayintouch/', views.stayintouch.as_view(), name='stayintouch'),
    path('threads/', views.threads.as_view(), name='threads'),
    path('topics/', views.topics.as_view(), name='topics'),
    path('topics/new/', views.addTopic.as_view(), name='addTopic'),
    path('threads/new/', views.addThread.as_view(), name='submit'),
    path('topics/update/<slug:pk>', views.updateTopic.as_view(), name='updateTopic'),
    path('topics/delete/<slug:pk>', views.deleteTopic.as_view(), name='deleteTopic'),
    path('view/', views.read.as_view(), name='view'),
    path('threads/<slug:pk>', views.readDetail.as_view(), name='viewDetail'),
    path('auth/<slug:pk>', views.authenticate.as_view(), name='authenticate'),
    path('threads/update/<slug:pk>', views.update.as_view(), name='update'),
    path('threads/delete/<slug:pk>', views.delete.as_view(), name='delete'),
    path('threads/approve/<slug:pk>', views.approve.as_view(), name='approve'),
    path('threads/reject/<slug:pk>', views.reject.as_view(), name='reject')
]
