from rest_framework import serializers
from .models import *
from decouple import config

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
    id = serializers.IntegerField(required=True)

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