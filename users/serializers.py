from django.contrib.auth import authenticate
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
#from rest.app.profile.models import UserProfile
from users.models import User
from rest_framework_jwt.settings import api_settings



#class UserSerializer(serializers.ModelSerializer):

   # class Meta:
    #    model = UserProfile
     #   fields = ('first_name', 'last_name', 'phone_number', 'age', 'gender')

JWT_PAYLOAD_HANDLER = api_settings.JWT_PAYLOAD_HANDLER
JWT_ENCODE_HANDLER = api_settings.JWT_ENCODE_HANDLER

class UserLoginSerializer(serializers.Serializer):

    email = serializers.CharField(max_length=255)
    password = serializers.CharField(max_length=128, write_only=True)
    token = serializers.CharField(max_length=255, read_only=True)

    def validate(self, data):
        email = data.get("email", None)
        password = data.get("password", None)
        user = authenticate(email=email, password=password)
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and / or password is not found or doesn\'t exist.'
            )
        try:
            payload = JWT_PAYLOAD_HANDLER(user)
            jwt_token = JWT_ENCODE_HANDLER(payload)
            update_last_login(None, user)
        except User.DoesNotExist:
            raise serializers.ValidationError(
                'User with given email and password does not exists'
            )
        return {
            'email':user.email,
            'token': jwt_token
        }
        

    
        
class UserRegistrationSerializer(serializers.ModelSerializer):

   # profile = UserSerializer(required=False)

    class Meta:
        model = User
        fields = ('email', 'password','name','date_of_birth','country','phone_number')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
       # profile_data = validated_data.pop('profile')
      # **validated_data,
        user = User.objects.create(
                                        email = validated_data['email'],
                                        password = validated_data['password'],
                                        name = validated_data['name'],
                                        date_of_birth = validated_data['date_of_birth'],
                                        country = validated_data['country'],
                                        phone_number = validated_data['phone_number']
                                        )
      
      #  UserProfile.objects.create(
    #     user=user,
        #    first_name=profile_data['first_name'],
         #   last_name=profile_data['last_name'],
          #  phone_number=profile_data['phone_number'],
           # age=profile_data['age'],
            #gender=profile_data['gender']
        #)
        return user