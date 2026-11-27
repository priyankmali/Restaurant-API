from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from .models import Profile



class RegisterSerializer(serializers.ModelSerializer):

    contact_number = serializers.CharField(required=False,allow_blank=True)

    profile_image = serializers.ImageField(required=False,allow_null=True)

    password = serializers.CharField(write_only=True,validators=[validate_password])

    confirm_password = serializers.CharField(write_only=True)



    class Meta:
        model = User
        fields = ['id','username','first_name','last_name','email','contact_number','profile_image','password','confirm_password']


    def validate_email(self, value):
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError("Email already registered.")
        return value

    def validation(self,data):
        if data['password'] != data['confirm_password']:
            raise serializers.ValidationError(
                {"confirm_password": "password do not match."}
            )
        return data




    def create(self, validated_data):

        contact_number = validated_data.pop('contact_number', '')

        profile_image = validated_data.pop('profile_image', None)

        validated_data.pop('confirm_password')

        password = validated_data.pop('password')

        user = User.objects.create_user(password=password, **validated_data)

        Profile.objects.create(user=user, contact_number=contact_number, profile_image=profile_image)

        return user




class ProfileSerializer(serializers.ModelSerializer):

    contact_number = serializers.CharField(source='profile.contact_number',read_only=True)

    profile_image = serializers.ImageField(source='profile.profile_image',read_only=True)

    class Meta:
            model= User
            fields = ['id','username','first_name','last_name','email','contact_number','profile_image']
            read_only_fields =['id','username']




class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(write_only=True)

    new_password = serializers.CharField(write_only=True, validators=[validate_password])

    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):

        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError({"confirm_password": "password do not match."})

        return data




class ForgotPasswordSerializer(serializers.Serializer):

    email = serializers.EmailField()




class ResetPasswordSerializer(serializers.Serializer):

    uid = serializers.CharField()

    token = serializers.CharField()

    new_password = serializers.CharField(write_only=True, validators=[validate_password])

    confirm_password = serializers.CharField(write_only=True)

    def validate(self, data):

        if data['new_password'] != data['confirm_password']:raise serializers.ValidationError("Passwords do not match")

        return data
    