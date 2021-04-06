from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.serializers import UserRegistrationSerializer
from users.serializers import UserLoginSerializer
from users.serializers import CourseSerializer
from users.models import User
from users.models import Courses
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework.decorators import api_view

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
    queryset = User.objects.all()
    

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = User.objects.filter(email=serializer.data['email']).values()

        response = {
            'success' : 'True',
            'status code' : status.HTTP_200_OK,
            'message': 'User logged in  successfully',
            'user_info':{
                'email' : serializer.data['email'],
                'name' : user[0]['name'],
                'country' : user[0]['country'],
                'phone_number' : user[0]['phone_number'],
                'date_of_birth' : user[0]['date_of_birth'],
                'profile_picture' : user[0]['profile_picture'],
                'uID': user[0]['id']
            },
            'token' : serializer.data['token'],
            }
        status_code = status.HTTP_200_OK

        return Response(response, status=status_code)

@api_view(['GET','POST'])
def courses_list(request):
    if request.method == 'GET':
        courses = Courses.objects.all()
        print (courses)
        courses_serializer = CourseSerializer(courses, many = True)
        return JsonResponse(courses_serializer.data, safe = False)
    
    elif request.method == 'POST':
        courses_data = JSONParser().parse(request)
        courses_serializer = CourseSerializer(data = courses_data)
        
        if courses_serializer.is_valid():
            courses_serializer.save()
            return JsonResponse(courses_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(courses_serializer.errors, status=status.HTTP_400_BAD_REQUEST)