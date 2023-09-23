from rest_framework import serializers
from todo_backend.models import User

class UserSerializer(serializers.ModelSerializer):

    #This is the password comparator which is also write_only
    confirm_password = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['email', 'username', 'password', 'confirm_password']
        extra_kwargs = {
                'password':{'write_only': True}
        }

    #Here we override the save method from the original user model
    def save(self):

        ## The 'validated_data' attribute is available after form validation in the models view
        user_instance = User(
                email = self.validated_data['email'],
                username = self.validated_data['username']
        )

        password = self.validated_data['password']
        conf_password = self.validated_data['confirm_password']

        if password != conf_password:
            raise serializers.ValidationError({'password': 'Password does not match'})

        user_instance.set_password(password)
        user_instance.save()

        return user_instance




