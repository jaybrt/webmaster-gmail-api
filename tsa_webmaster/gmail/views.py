from django.shortcuts import render
from rest_framework.views import APIView
from .utils import create_send_email
from rest_framework.response import Response
from rest_framework import status


# Create your views here.
class EmailRequest(APIView):
    email_kwarg = "email"

    def post(self, request, format=None):
        usr_email = request.data.get(self.email_kwarg)

        if usr_email:
            create_send_email(usr_email)
            return Response({"message": "email sent!"}, status=status.HTTP_200_OK)
        else:
            return Response(
                {"Bad Request": "No email provided"}, status=status.HTTP_400_BAD_REQUEST
            )
