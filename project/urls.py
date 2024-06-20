
from django.contrib import admin
from django.urls import path
from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stulistcrte/', views.StudentListCreate.as_view()),
    path('sturetupdelt/<int:pk>', views.Student_ret_up_delt.as_view()),
]
