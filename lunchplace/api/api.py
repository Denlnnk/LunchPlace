from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import EmployeeSerializer


class EmployeeAPIView(generics.RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeSerializer

    def get_object(self):
        return self.request.user

