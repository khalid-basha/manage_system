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

    def create_user(self, username, email, password, **extra_fields):
        print("---------------------hiiiiiiiiiii----------------------")
        if not username:
            raise ValueError('username for user must be set')
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.user_type = extra_fields['user_type']
        if user.user_type == 1:
            raise ValueError('Can\'t regist as Admin')
            user.user_type =2

        user.save()
        return user
