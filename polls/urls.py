
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'votacao'
router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet)
router.register(r'posts',views. PostViewSet)
router.register(r'messages',views.ChatMessageViewset)
urlpatterns = [
    path('create/', views.question_create, name='question_create'),
    path('', views.index, name='index'),
    path("cadastro/",views.cadastro,name='cadastro'),
    path("logins/",views.logins,name='logins'),
    path('', include(router.urls)),
]
