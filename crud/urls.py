from django.urls import path
from.import views
urlpatterns=[
    path('',views.home,name='home'),
    path('create/',views.create,name='create'),
    path('read/',views.read,name='read'),
    path('registration/',views.registration,name='registration'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('edit/<int:id>',views.edit,name='edit'),
    path('update/<int:id>',views.update,name='update')
    
]