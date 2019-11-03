from .serializers import *
from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
import secrets
import string
from rest_framework import status
from .utils import verify_password
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse_lazy
from django.views import generic
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from django.template import loader

with open("ban_list.txt", "r") as file:
    banned_passwords = file.readlines()
    file.close()


class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


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
            if verify_password(serializer.validated_data["password"]):
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
        serializer = UserValidator(data=request.data)
        if serializer.is_valid():
            try:
                user = CustomUser.objects.get(id=serializer.validated_data["user_id"])
                accounts = Account.objects.values("site", "user_name", "email", "id_account").filter(user=user)
                resp = []
                for account in accounts:
                    if len(account["email"]) > 0:
                        del account["user_name"]
                    else:
                        del account["email"]
                    resp.append(account)
                return JsonResponse({"accounts": resp}, status=status.HTTP_200_OK)
            except CustomUser.DoesNotExist:
                return JsonResponse({"status": "NOT found"}, status=status.HTTP_404_NOT_FOUND)
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
                user = CustomUser.objects.get(id=serializer.validated_data["user_id"])
                account = Account.objects.values("password", "site") \
                    .get(id_account=serializer.validated_data["account_id"], user=user)
                subject = 'PassWord Manager alert'
                message = f'Se he desbloqueado la informacion de tu cuenta de {account["site"]}, en caso de no haber realizado esta accion se recomienda cambiar de contraseña'
                email_from = settings.EMAIL_HOST_USER
                recipient_list = [user.email]
                send_mail(subject, message, email_from, recipient_list)

            except CustomUser.DoesNotExist:
                return JsonResponse({"status": "NOT found"}, status=status.HTTP_404_NOT_FOUND)
            else:
                return JsonResponse(account, status=status.HTTP_200_OK)

        else:
            return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    else:
        return JsonResponse({"Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@login_required
def accounts_manager(request):
    template = loader.get_template('accounts.html')
    if request.user.is_authenticated:
        # Do something for authenticated users
        # current_user = request.user
        # accounts = Account.objects.filter(user=current_user)
        # for account in accounts:
        #     print(account)
        # context = {"accounts": accounts}
        # else:
        #     context = {}
        #
        # return HttpResponse(template.render(context, request))
        return HttpResponse(template.render({}, request))


@login_required
def add_account(request):
    template = loader.get_template('add_account.html')
    if request.user.is_authenticated:
        return HttpResponse(template.render({}, request))


@api_view(['POST'])
def add_account_api(request):
    if request.method == 'POST':
        serializer = NewAccountValidator(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"status": "Data saved correctly"}, status=status.HTTP_200_OK)
        else:
            return JsonResponse(serializer.errors, status=status.HTTP_404_NOT_FOUND)

    else:
        return JsonResponse({"Method not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
