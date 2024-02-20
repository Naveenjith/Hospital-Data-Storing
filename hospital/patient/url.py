from django.urls import  path

from patient import views

urlpatterns = [
    path('',views.register2),
    path('viewpat/',views.patientview,name='viewpat'),
    path('updatepat/<int:TK>',views.patupdate,name='update'),
    path('deletpat/<int:TK>',views.deletpat,name='delete')
]