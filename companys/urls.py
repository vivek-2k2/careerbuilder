from django.urls import path
from.import views
app_name='companys'
urlpatterns=[
    path('',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('forgot/',views.forgot,name='forgot'),
    path('hiring/',views.hiring,name='hiring'),
    path('cview/',views.cview,name='cview'),
    path('update/<int:hid>',views.update,name='update'),
    path('delete/<int:hid>',views.deletecomp,name='deletecomp'),
    path('applied/',views.applied,name='applied'),
    # path('view_resume/<int:rid>',views.view_resume,name='view_resume'),
    path('clogout/',views.clogout,name='clogout'),
    path('payment/',views.payment,name='payment'),
]