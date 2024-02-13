from django.urls import path
from.import views
app_name='jobseeker'
urlpatterns=[
    path('signup',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('',views.home,name='home'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('forgot/',views.forgot,name='forgot'),
    path('about/',views.about,name='about'),
    path('apply/<int:hid>',views.apply,name='apply'),
    path('form/',views.form,name='form'),
    path('profile/',views.profile,name='profile'),
    path('jlogout/',views.jlogout,name='jlogout'),
    path('status/',views.status,name='status'),
]
