from .models import Students
from .serializers import StudentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

# Create your views here.


class StudentListCreate(ListCreateAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer


class Student_ret_up_delt(RetrieveUpdateDestroyAPIView):
    queryset = Students.objects.all()
    serializer_class = StudentSerializer
