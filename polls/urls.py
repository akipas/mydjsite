from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('<int:question_id>/', views.detail, name='detail'),

    path('<int:question_id>/results/', views.results, name='results'),

    path('<int:question_id>/vote/', views.vote, name='vote'),
    
    path('date',views.date_actuelle, name='date_actuelle'),

    path('addition/<int:nombre1>/<int:nombre2>/',views.addition, name='addition'),
    path('<int:question_id>', views.view_articles, name='view_article')
]
