from rest_framework import serializers
from rest_framework.utils import model_meta

from .models import User

class UserSerializer(serializers.ModelSerializer):

  
  password = serializers.CharField(write_only=True)

  class Meta:
    model = User
    fields = [
      "id",
      "email",
      "password",
      "user_name",
    ]

class UserDetailSerializer(serializers.ModelSerializer):
  password = serializers.CharField()

  class Meta:
    model = User
    fields = [
      "id",
      "email",
      "password",
      "user_name",
      "date_joined",
      "is_superuser",
    ]
    # extra_kwargs = {"password": {"write_only": True}}

  def update(self, instance: User, validated_data: dict) -> User:

    # non_editable_keys = ("email", "cpf")

    password = validated_data.get("password")

    for key, value in validated_data.items():
      # if key not in non_editable_keys:
        setattr(instance, key, value)

    if password:
      instance.set_password(password)

    instance.save()

    return instance

class LoginSerializer(serializers.Serializer):

  email = serializers.EmailField(max_length=100)
  password = serializers.CharField(write_only=True)
