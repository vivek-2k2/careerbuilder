from django.urls import path
from.import views
app_name='jobseeker'
urlpatterns=[
    path('signup',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('forgot/',views.forgot,name='forgot')
]
