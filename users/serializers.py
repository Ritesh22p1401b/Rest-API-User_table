from rest_framework import serializers
from django.contrib.auth import get_user_model

User=get_user_model()

class UserRegister(serializers.ModelSerializer):
    
    password2=serializers.CharField(style={'input_type':'password'},write_only=True)
    
    class Meta:
        model=User
        fields=["username","email","password","password2"]
        
    def save(self):
        user=User(
            email=self.validated_data['email'],
            username=self.validated_data['username'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        
        if password != password2:
            raise serializers.ValidationError({'password':'password does not match'})
        user.set_password(password)
        user.save()
        return user
    
class UserDetailsSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=User
        fields=['username','email','first_name','last_name']
