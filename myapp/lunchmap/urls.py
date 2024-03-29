from django.urls import path
from . import views

app_name = 'lunchmap'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views. DetailView.as_view(), name='detail'),
    path('creat/', views.CreateView.as_view(), name='create'),
    #path('creatcomment/', views.CreateView.as_view(), name='createcomment'),
    path('<int:pk>/update/', views.UpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', views.DeleteView.as_view(), name='delete'),
    path('comment/create/<int:pk>/',
         views.CommentCreate.as_view(), name='comment_create'),
]
