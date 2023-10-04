from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from .models import User
# Create your views here.


class UserView(APIView):
    def get(self, request, pk=None):
        if pk is not None:
            try:
                obj = User.objects.get(pk=pk)
            except:
                return Response(status=status.HTTP_404_NOT_FOUND)
            data =  UserSerializer(obj, many=False).data
            return Response(data)
        queryset = User.objects.all()
        data = UserSerializer(queryset, many=True).data
        return Response(data)

    def post(self, request,):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        # print(serializer.errors)
        # return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        if pk is not None:
            obj = User.objects.get(pk=pk)
            obj.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


