from django.urls import path
from home import views

urlpatterns = [
    path('', views.main, name='main'),
    path('<slug:post>/', views.post_single, name='post_single'),
    path('dia_res', views.pagedia, name='pagedia'),
    # path('resdia', views.diabetes, name='diabetes'),
    # path('/', views.test, name='house'),
    # path('', views.start, name='start'),
    
    # path('signup', views.signup, name="signup"),
    # path('signin', views.signin, name="signin"),
    # path('signout', views.signout, name="signout"),
    # path('about', views.about, name='about'),
    # path('', views.predictor, name='predictor'),
    # path('result', views.forminfo, name='result')
]