from .serializers import *
from django.http import JsonResponse
from rest_framework.decorators import api_view
import secrets
import string
from rest_framework import status
import re
from django.core.mail import send_mail
from django.conf import settings

with open("ban_list.txt", "r") as file:
    banned_passwords = file.readlines()
    file.close()


# Create your views here.
@api_view(['GET'])
def generate_password(request):
    if request.method == 'GET':
        serializer = KeyValidator(data=request.data)
        if serializer.is_valid():
            alphabet = string.ascii_letters + string.digits + "@#$%^&+="
            while True:
                password = ''.join(secrets.choice(alphabet) for i in range(12))
                if password not in banned_passwords:
                    return JsonResponse({"password": password}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)
    else:
        return JsonResponse({"Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def validate_password(request):
    if request.method == 'POST':
        serializer = PasswordValidator(data=request.data)
        if serializer.is_valid():
            if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', serializer.validated_data["password"]):
                return JsonResponse({"status": "ok"}, status=status.HTTP_200_OK)
            else:
                return JsonResponse({"status": "not secure"}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    else:
        return JsonResponse({"Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET'])
def show_accounts(request):
    if request.method == 'GET':
        serializer = KeyValidator(data=request.data)
        if serializer.is_valid():
            accounts = Account.objects.values("site", "user", "email", "id_account")
            resp = []
            for account in accounts:
                if len(account["email"]) > 0:
                    del account["user"]
                else:
                    del account["email"]
                resp.append(account)
            return JsonResponse({"accounts": resp}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    else:
        return JsonResponse({"Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def show_password(request):
    if request.method == 'POST':
        serializer = AccountValidator(data=request.data)
        if serializer.is_valid():
            try:
                account = Account.objects.values("password", "site").get(id_account=serializer.validated_data["id"])
                subject = 'PassWord Manager alert'
                message = f'Se he desbloqueado la informacion de tu cuenta de {account["site"]}, en caso de no haber realizado esta accion se recomienda cambiar de contraseña'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = ['kleverfsarango@gmail.com']
                send_mail(subject, message, email_from, recipient_list)

            except Account.DoesNotExist:
                return JsonResponse({"status": "NOT found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return JsonResponse(account, status=status.HTTP_200_OK)

        else:
            return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    else:
        return JsonResponse({"Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
