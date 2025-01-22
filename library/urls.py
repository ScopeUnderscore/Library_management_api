from django.urls import path
from library.views import AuthorList, BookList, AuthorViewSet, BookViewSet
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path("authors/", AuthorList.as_view(), name="author-list"),
    path("books/", BookList.as_view(), name="book-list"),
]

router = DefaultRouter()
router.register(r"authors", AuthorViewSet)
router.register(r"books", BookViewSet)

urlpatterns = router.urls
