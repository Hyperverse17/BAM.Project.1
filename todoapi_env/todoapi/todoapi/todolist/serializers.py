from rest_framework import serializers

from .models import User


class UserSerializer(serializers.ModelSerializer):
  name = serializers.CharField(max_length=1000, required=True)
  surname = serializers.CharField(max_length=1000, required=True)
  login_name = serializers.CharField(max_length=1000, required=True)
  password = serializers.CharField(max_length=1000, required=True)

  def create(self, validated_data):
    # Once the request data has been validated, we can create a User item instance in the database
    return User.objects.create(
      name=validated_data.get('name'),
      surname=validated_data.get('surname'),
      login_name=validated_data.get('login_name'),
      password=validated_data.get('password')
    )

  def update(self, instance, validated_data):
    # Once the request data has been validated, we can update the User item instance in the database
    instance.name = validated_data.get('name', instance.name)
    instance.surname = validated_data.get('surname', instance.surname)
    instance.login_name = validated_data.get('login_name', instance.login_name)
    instance.password = validated_data.get('password', instance.password)

    instance.save()
    return instance

  class Meta:
    model = User
    fields = (
      'id',
      'name',
      'surname',
      'login_name',
      'password',
      'creation_date',
      'last_updated'
    )