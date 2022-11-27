from django.contrib.auth.backends import ModelBackend, UserModel


class CustomBackend(ModelBackend):
    def authenticate(self, request, username = ..., password= ..., **kwargs):
        if username is None:
            username = kwargs.get(UserModel.USERNAME_FIELD)
        if username is None or password is None:
            return
        try:
            user = UserModel.objects.get(email=username)
            print(self.user_can_authenticate(user))
        except UserModel.DoesNotExist:
            UserModel().set_password(password)
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user