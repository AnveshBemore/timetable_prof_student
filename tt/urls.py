from django.urls import path
from .import views
urlpatterns=[
    # path('',views.student_register,name="student_registered"),
    path('',views.index,name="index"),
    path('index',views.index,name="index"),
    path('professor_subject',views.professor_subject,name="professor_subject"),
    path('student_register',views.student_register,name="student_register"),
    path('prof_subj_registration',views.prof_subj_registration,name='prof_subj_registration'),
    path('student_registered',views.student_registered,name='student_registered'),
    path('hall_view',views.hall_view,name='hall_view'),
    path('prof_view',views.prof_view,name='prof_view'),
    # path('delProf/<str:id>',views.delProf,name='delProf'),
    path('delProf',views.delProf,name='delProf'),
]