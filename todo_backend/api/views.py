from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import UserSerializer

@api_view(['POST'])
def user_creation_view(request):

    if request.method == 'POST':

        serializers = UserSerializer(data=request.data)
        data = {}
        if serializers.is_valid():
            user = serializers.save()
            data['response'] = "Succesfully created a new user"
            data['email'] = user.email
            data['username'] = user.username

            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)
