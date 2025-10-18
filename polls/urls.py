from django.urls import path
from .import views

app_name = 'polls'
urlpatterns = [
    # /polls/
    path('', views.index, name='index'),
    # /polls/(q_id)/
    path('<int:question_id>/', views.detail, name='detail'),
    # /polls/(q_id)/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # /polls/(q_id)/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]