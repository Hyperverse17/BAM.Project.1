from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.mixins import UpdateModelMixin, DestroyModelMixin

from .models import User
from .serializers import UserSerializer


class UserListView(
  APIView, # Basic View class provided by the Django Rest Framework
  UpdateModelMixin, # Mixin that allows the basic APIView to handle PUT HTTP requests
  DestroyModelMixin, # Mixin that allows the basic APIView to handle DELETE HTTP requests
):

  def get(self, request, id=None):
    if id:
      # If an id is provided in the GET request, retrieve the User item by that id
      try:
        # Check if the user item the user wants to update exists
        queryset = User.objects.get(id=id)
      except User.DoesNotExist:
        # If the user item does not exist, return an error response
        return Response({'errors': 'This user item does not exist.'}, status=400)

      # Serialize user item from Django queryset object to JSON formatted data
      read_serializer = UserSerializer(queryset)

    else:
      # Get all user items from the database using Django's model ORM
      queryset = User.objects.all()

      # Serialize list of users item from Django queryset object to JSON formatted data
      read_serializer = UserSerializer(queryset, many=True)

    # Return a HTTP response object with the list of user items as JSON
    return Response(read_serializer.data)


  def post(self, request):
    # Pass JSON data from user POST request to serializer for validation
    create_serializer = UserSerializer(data=request.data)

    # Check if user POST data passes validation checks from serializer
    if create_serializer.is_valid():

      # If user data is valid, create a new user item record in the database
      user_item_object = create_serializer.save()

      # Serialize the new user item from a Python object to JSON format
      read_serializer = UserSerializer(user_item_object)

      # Return a HTTP response with the newly created user item data
      return Response(read_serializer.data, status=201)

    # If the users POST data is not valid, return a 400 response with an error message
    return Response(create_serializer.errors, status=400)


  def put(self, request, id=None):
    try:
      # Check if the user item the user wants to update exists
      user_item = User.objects.get(id=id)
    except User.DoesNotExist:
      # If the user item does not exist, return an error response
      return Response({'errors': 'This user item does not exist.'}, status=400)

    # If the user item does exists, use the serializer to validate the updated data
    update_serializer = UserSerializer(user_item, data=request.data)

    # If the data to update the user item is valid, proceed to saving data to the database
    if update_serializer.is_valid():

      # Data was valid, update the user item in the database
      user_item_object = update_serializer.save()

      # Serialize the user item from Python object to JSON format
      read_serializer = UserSerializer(user_item_object)

      # Return a HTTP response with the newly updated user item
      return Response(read_serializer.data, status=200)

    # If the update data is not valid, return an error response
    return Response(update_serializer.errors, status=400)


  def delete(self, request, id=None):
    try:
      # Check if the user item the user wants to update exists
      user_item = User.objects.get(id=id)
    except User.DoesNotExist:
      # If the user item does not exist, return an error response
      return Response({'errors': 'This user item does not exist.'}, status=400)

    # Delete the chosen user item from the database
    user_item.delete()

    # Return a HTTP response notifying that the user item was successfully deleted
    return Response(status=204)
