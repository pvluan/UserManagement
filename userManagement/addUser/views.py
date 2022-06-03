from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .models import UserInfo
from .serializers import AddUserSerializer

# Create your views here.
class UserListView(APIView):
   # permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # list all username
        users = UserInfo.objects.filter(user = request.user.id)
        serializer = AddUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    # create User:
    def post(self, request, *args, **kwargs):
        #create user
        data = {
            'userName': request.data.get('userName'),
            'user': request.user.id
        }
        serializer = AddUserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)