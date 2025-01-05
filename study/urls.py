
from django.urls import path,include
from .views import *

urlpatterns = [
    path("",home,name="home"),
    path("notes/",note,name="notes"),
    path("dictionary/",dictionary,name="dictionary"),
    path("login_/",login_,name="login"),
    path("delete/<int:pk>",delete,name="delete"),
    path("notedetailview_/<int:pk>",notedetailview.as_view(),name="notedetailview"),
    path("homework/",homework,name="homework"),
    path("update_work/<int:pk>",update_work,name="update_work"),
    path("delete_work/<int:pk>",delete_work,name="delete_work"),
    path("youtube/",youtube,name="youtube"),
    path("todo/",todo,name="todo"),
    path("book/",book,name="book"),
    path("delete__/<int:pk>",delete__,name="delete__"),
]