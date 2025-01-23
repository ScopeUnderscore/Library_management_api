"""
URL configuration for library_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# Import required modules
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from library.views import UserRegisterView
from library.views import redirect_to_docs


# Define the Swagger schema view for API documentation
schema_view = get_schema_view(
    openapi.Info(
        title="Library Management API",  # Title of the API documentation
        default_version="v1.0",  # Version of the API
        description="API documentation for Library Management System",  # Brief description of the API
        terms_of_service="https://www.google.com/policies/terms/",  # Link to terms of service
        contact=openapi.Contact(
            email="contact@library.local"
        ),  # Contact email for support
        license=openapi.License(name="BSD License"),  # License information
    ),
    public=True,  # Indicates the schema view is publicly accessible
    permission_classes=(AllowAny,),  # Allows access to anyone
    authentication_classes=(
        TokenAuthentication,
    ),  # Authentication mechanism used for the API
)

# Define URL patterns for the application
urlpatterns = [
    path("", redirect_to_docs, name="redirect_to_docs"),  # Redirect root URL
    path("admin/", admin.site.urls),  # URL for the Django admin interface
    path("api/", include("library.urls")),  # Include URLs from the 'library' app
    path(
        "api-token-auth/", obtain_auth_token, name="api_token_auth"
    ),  # Endpoint for obtaining auth tokens
    path(
        "api/register/", UserRegisterView.as_view(), name="user_register"
    ),  # Endpoint for user registration
    path(
        "swagger/",  # URL for Swagger UI
        schema_view.with_ui(
            "swagger", cache_timeout=0
        ),  # Render Swagger UI with no cache timeout
        name="schema-swagger-ui",
    ),
    path(
        "redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"
    ),  # URL for ReDoc UI
]
