from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django import utils
from django.urls import reverse


class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)

class User(AbstractUser):
    username = None
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
   
    
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    
    def get_password_reset_url(self):
        base64_encoded_id = utils.http.urlsafe_base64_encode(utils.encoding.force_bytes(self.id))
        token = PasswordResetTokenGenerator().make_token(self)
        reset_url_args = {'uidb64': base64_encoded_id, 'token': token}
        reset_path = reverse('Accounts:password_reset_confirm', kwargs=reset_url_args)
        reset_url = f'{settings.DOMAIN_NAME}{reset_path}'
        return reset_url
    
    objects = UserManager()
    class Meta:
        db_table = 'User'

    def __str__(self):
        return self.first_name+' '+self.last_name



