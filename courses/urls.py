from django.urls import path
from . import views

app_name = 'classes'

urlpatterns = [
    path('', views.courses_index, name='courses'),
    path('polls', views.polls_index, name='polls'),
    path('polls/<int:question_id>/', views.detail, name='detail'),
    path('polls/<int:question_id>/results/', views.results, name='results'),
    path('polls/<int:question_id>/vote/', views.vote, name='vote'),
]

