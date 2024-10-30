from django.contrib import admin
from django.urls import path
from .views import CarInt, CreateView, NewCar, EditCar, DeleteCar, CreateUser
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CarInt.as_view(), name="base"),
    path('newcar/', CreateView.as_view(), name="new"),
    path('newcar/<int:pk>/', NewCar.as_view(), name="newcar"),
    path('newcar/<int:pk>/edit', EditCar.as_view(), name="editcar"),
    path('newcar/<int:pk>/delete', DeleteCar.as_view(), name="delete"),
    path('newcar/<int:pk>/user_form', CreateUser.as_view(), name="userdetail"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
