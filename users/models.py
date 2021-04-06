import uuid
from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser



# Create your models here.

class UserManager(BaseUserManager):

    def create_user(self, email,password, name , date_of_birth , country, phone_number,  profile_photo = 'Okay'):
        """
        Create and return a `User` with an email, username and password.
        """
        if not email:
            raise ValueError('Users Must Have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
        )
    is_active = models.BooleanField(default=True)
    name = models.TextField()
    date_of_birth = models.DateField()
    country = models.TextField()
    phone_number = models.TextField()
    profile_picture = models.URLField()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','date_of_birth','country','phone_number']

    # Tells Django that the UserManager class defined above should manage
    # objects of this type.
    objects = UserManager()

    def __str__(self):
        return self.email

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "users"

class Courses(models.Model):
    _id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    content = models.TextField()
    teacher = models.TextField()
    teacher_country = models.TextField()
    
    REQUIRED_FIELDS = ['name','content','teacher','teacher_country']