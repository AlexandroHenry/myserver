from django.urls import path, include
from .views import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", testAPI),
    path("readbible/<str:book>&chapter=<int:chapter>&version=<str:version>", readbibleChapter),
    path("readbible/<str:book>&chapter=<int:chapter>&verse=<int:verse>&version=<str:version>", readbibleVerse),
    path("bookinfo/<str:book>", book),
    path("readbible/<str:keyword>&version=<str:version>", searchVerse)
]