
from django.urls import  path

from doctor import views

urlpatterns = [
    path('',views.register),
    path('viewdoc/',views.doctorview,name='viewdoct'),
    path('updatedoc/<int:dk>',views.updatedoct,name='update'),
    path('deletdoc/<int:dk>',views.deletdoc,name='delete')
]
