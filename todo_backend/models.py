from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# Create your models here.

#This is the custom user manager
class MyAccountManager(BaseUserManager):

    def create_user(self, email, username, password=True):
        if not email:
            raise ValueError("Users must have an email address")

        if not username:
            raise ValueError("Users must have an username address")

        #creates the user
        user = self.model(
                email = self.normalize_email(email),
                username = username,
        )

        #setting the password
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password):
        user = self.model(
            email = self.normalize_email(email),
            username = username,
        )

        user.set_password(password)
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user

#This is the custom user model
class User(AbstractBaseUser):

    email                   = models.EmailField(verbose_name='email', max_length=60, unique=True)
    username                = models.CharField(max_length=30, unique=True)

    #required fields when using a custom user model
    date_joined             = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login              = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin                = models.BooleanField(default=False)
    is_active               = models.BooleanField(default=True)
    is_staff                = models.BooleanField(default=False)
    is_superuser            = models.BooleanField(default=False)

    #specifies which field will be used to login
    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = MyAccountManager()

    def __str__(self):
        return self.email 

    #required methods when using custom user model
    def has_perm(self, perm, obj=True):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True
