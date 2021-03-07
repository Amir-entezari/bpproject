from django.urls import path
from. import views
from django.conf import settings
from django.conf.urls.static import static
#################################################################


#*************************************URLs PATTERNS*********************************************

urlpatterns = [
    path ('' , views.home , name ="home"),
#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      TEACHERS URLs      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#*************************************TEACHERs EXERERCISE***************************************



    path('ostads/', views.ostads,name='ostads'),
    path('ostads/tamrin' , views.ostads_tamrin , name ="ostads_tamrin"),
    path('ostads/tamrin/upload' , views.ostads_tamrin_upload,name="ostads_tamrin_upload"),
    path('ostads/tamrin/javab/<int:javab_id>' , views.ostads_tamrin_javab , name="ostads_tamrin_javab"),


#**************************************TEACHERs VIDEOS*****************************************
   
   
    path('ostads/videos/', views.ostads_videos,name='ostads_videos'),
    path('ostads/videos/upload' , views.ostads_videos_upload,name="ostads_videos_upload"),
    path('ostads/videos/seen/<int:videoid>', views.ostads_videos_seen , name ="ostads_videos_seen"),

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@      STUDEBT URLs      @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

#*************************************students EXERERCISE***************************************
    path('students/', views.students,name='students'),
    path('students/videos/', views.students_videos,name='students_videos'),
    path('students/tamrin' , views.students_tamrin , name ="students_tamrin"),
    path ('student/tamrin/upload' , views.student_tamrin_upload , name ="student_tamrin_upload"),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

