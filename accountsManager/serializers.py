from rest_framework import serializers
from .models import *
from decouple import config
from .utils import verify_password

SECURE_KEY = config('SECURE_KEY')


class KeyValidator(serializers.Serializer):
    """
    Serializer used to check data that comes from user, uses provided key to identify channel.
    """
    key = serializers.CharField(required=True, max_length=60)

    def validate_key(self, key):
        """
        Function used to validate if key exists
        :param key: key provided from system to use in chanel
        :return: returns key if key exists otherwise raises a validation error.
        """
        if key == SECURE_KEY:
            return key
        else:
            raise serializers.ValidationError("Wrong Access Key")

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class UserValidator(serializers.Serializer):
    """
    Serializer used to check data that comes from user, uses provided key to identify channel.
    """
    key = serializers.CharField(required=True, max_length=60)
    user_id = serializers.IntegerField(required=True)

    def validate_key(self, key):
        """
        Function used to validate if key exists
        :param key: key provided from system to use in chanel
        :return: returns key if key exists otherwise raises a validation error.
        """
        if key == SECURE_KEY:
            return key
        else:
            raise serializers.ValidationError("Wrong Access Key")

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class PasswordValidator(serializers.Serializer):
    """
    Serializer used to check data that comes from user, uses provided key to identify channel.
    """
    key = serializers.CharField(required=True, max_length=60)
    password = serializers.CharField(required=True, max_length=60)

    def validate_key(self, key):
        """
        Function used to validate if key exists
        :param key: key provided from system to use in chanel
        :return: returns key if key exists otherwise raises a validation error.
        """
        if key == SECURE_KEY:
            return key
        else:
            raise serializers.ValidationError("Wrong Access Key")

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class AccountValidator(serializers.Serializer):
    """
    Serializer used to check data that comes from user, uses provided key to identify channel.
    """
    key = serializers.CharField(required=True, max_length=60)
    user_id = serializers.IntegerField(required=True)
    account_id = serializers.IntegerField(required=True)

    def validate_key(self, key):
        """
        Function used to validate if key exists
        :param key: key provided from system to use in chanel
        :return: returns key if key exists otherwise raises a validation error.
        """
        if key == SECURE_KEY:
            return key
        else:
            raise serializers.ValidationError("Wrong Access Key")

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass


class NewAccountValidator(serializers.Serializer):
    """
    Serializer used to check data that comes from user, uses provided key to identify channel.
    """
    key = serializers.CharField(required=True, max_length=60)
    user_id = serializers.IntegerField(required=True)
    site = serializers.CharField(required=True, max_length=300)
    user_name = serializers.CharField(required=False, max_length=300)
    email = serializers.EmailField(required=False, max_length=300)
    password = serializers.CharField(required=True, max_length=20)

    def validate_key(self, key):
        """
        Function used to validate if key exists
        :param key: key provided from system to use in chanel
        :return: returns key if key exists otherwise raises a validation error.
        """
        if key == SECURE_KEY:
            return key
        else:
            raise serializers.ValidationError("Wrong Access Key")

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        try:
            user = CustomUser.objects.get(id=validated_data["user_id"])
            if verify_password(validated_data["password"]):
                if "user_name" in validated_data and len(validated_data["user_name"]) > 0:
                    account = Account(user=user, site=validated_data["site"], user_name=validated_data["user_name"],
                                      password=validated_data["password"])
                elif "email" in validated_data and len(validated_data["email"]) > 0:
                    account = Account(user=user, site=validated_data["site"], email=validated_data["email"],
                                      password=validated_data["password"])
                else:
                    raise serializers.ValidationError("Must provide user name or email")
                account.save()
                return account
            else:
                raise serializers.ValidationError("Not valid password")
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError("User not found")
