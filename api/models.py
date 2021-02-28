from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.



#create a  user
#create a superuser
class MyAccountManager(BaseUserManager):
    def create_user(self,email, username,first_name,phone,location,picture, password=None):
        if not email:
            raise ValueError("user must have an email address!")
        if not username:
            raise ValueError("user`s must have an usrname")
        user = self.model(email=self.normalize_email(email),
                            first_name=first_name,
                            phone=phone,
                            location=location,
                            picture=picture,
                            username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    username=models.CharField(max_length=100, unique=True)
    date_join=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    first_name=models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    location=models.CharField(max_length=100)
    picture=models.ImageField(max_length=255,upload_to='picture', blank=True,null=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)

    objects=MyAccountManager()


    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_lebel):
        return True

class Award(models.Model):
    acconut_id=models.ForeignKey(Account, on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    point=models.IntegerField()
    created_date=models.DateTimeField(verbose_name='date joined', auto_now_add=True)
