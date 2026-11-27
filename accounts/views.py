from django.shortcuts import render
from .serializers import (RegisterSerializer,ProfileSerializer,ChangePasswordSerializer,ForgotPasswordSerializer,ResetPasswordSerializer)
from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import Profile
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,  urlsafe_base64_decode
from django.core.mail import send_mail
from django.conf import settings


class RegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer = RegisterSerializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response({"message": "Registeration successful.", "data": serializer.data}, status=status.HTTP_201_CREATED)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

#Add

class ProfileView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        serializer = ProfileSerializer(request.user)

        return Response(serializer.data,status=status.HTTP_200_OK)


    def patch(self, request):

        Profile.objects.get_or_create(user=request.user)

        serializer = ProfileSerializer(request.user, data=request.data,partial=True)

        if serializer.is_valid():

            serializer.save()

            return Response({
                "message": "Profile updated successfully",
                "data": serializer.data
            }, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ChangePasswordView(APIView):

    permission_classes = [IsAuthenticated]

    def post(self, request):

        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():

            user = request.user

            if not user.check_password(serializer.validated_data['old_password']):

                return Response({"error": "old password is incorrect"}, status= status.HTTP_400_BAD_REQUEST)

            user.set_password(serializer.validated_data['new_password'])

            user.save()

            return Response({"message": "Password changed successfully"}, status= status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class ForgotPasswordView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        serializer =  ForgotPasswordSerializer(data= request.data)

        if serializer.is_valid():

            email = serializer.validated_data['email']

            user = User.objects.filter(email__iexact=email, is_active = True).first()

            if user:

                uid  = urlsafe_base64_encode(force_bytes(user.pk))

                token = default_token_generator.make_token(user)

                reset_link = (f"http://localhost:3000/reset-password/"
                              f"?uid={uid}&token={token}")

                send_mail(subject="Password Reset",
                    message=f"Click here to reset your password: {reset_link}",
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[user.email],)

            return Response(
                {
                    "message": "If the email is registered, password reset instructions will be sent."
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class ResetPasswordView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):
        Profile.objects.get_or_create(user=request.user)

        serializer = ResetPasswordSerializer(data=request.data)

        if serializer.is_valid():

            uid = serializer.validated_data['uid']
            token = serializer.validated_data['token']

            try:

                user_id = urlsafe_base64_decode(uid).decode()

                user = User.objects.get(pk=user_id, is_active=True)

            except (ValueError, TypeError, User.DoesNotExist):
                return Response(
                    {"error": "Invalid reset link"},
                    status=status.HTTP_400_BAD_REQUEST
                )

            if not default_token_generator.check_token(user, token):

                return Response({"error": "Invalid or expired token"},status=status.HTTP_400_BAD_REQUEST)

            user.set_password(
                serializer.validated_data['new_password']
            )

            user.save()

            return Response(
                {
                    "message": "Password reset successfully"
                },
                status=status.HTTP_200_OK
            )

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

