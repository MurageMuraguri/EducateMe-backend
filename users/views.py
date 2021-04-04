from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.serializers import UserRegistrationSerializer
from users.serializers import UserLoginSerializer

# Create your views here.
class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        status_code = status.HTTP_201_CREATED
        response = {
            'success' : 'True',
            'status code' : status_code,
            'message': 'User registered  successfully',
            }
        
        return Response(response, status=status_code)


class UserLoginView(RetrieveAPIView):

    permission_classes = (AllowAny,)
    serializer_class = UserLoginSerializer
    

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        print(serializer.data)
        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'user_info':{
                'email' : serializer.data['email'],
               # 'name' : serializer.data['name'],
               # 'country' : serializer.data['country'],
               # 'phone_number' : serializer.data['phone_number'],
               # 'date_of_birth' : serializer.data['date_of_birth'],
                #'profile_picture' : serializer.data['profile_picture'],
               # 'uID':serializer.data['uID']
            },
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)