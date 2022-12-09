from django.contrib.auth.models import UserManager
class UserManager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('username for user must be set')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.user_type = 1
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

    def create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('username for user must be set')
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.user_type = extra_fields['user_type']
        user.save()
        return user
