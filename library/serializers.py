# from rest_framework import serializers
# from rest_framework.serializers import ValidationError
# from .models import Author, Book


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = "__all__"


# class BookSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Book
#         fields = "__all__"

#     def validate(self, data):
#         # Check if a book with the same title and author already exists
#         title = data.get("title")
#         author = data.get("author")

#         if Book.objects.filter(title=title, author=author).exists():
#             raise ValidationError(f"The book '{title}' by this author already exists.")
#         return data

from rest_framework import serializers
from rest_framework.serializers import ValidationError
from django.contrib.auth.models import User
from .models import Author, Book


# Serializer for User Registration
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ("username", "password", "email")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            password=validated_data["password"],
            email=validated_data["email"],
        )
        return user


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

    def validate(self, data):
        # Check if a book with the same title and author already exists
        title = data.get("title")
        author = data.get("author")

        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(f"The book '{title}' by this author already exists.")
        return data
