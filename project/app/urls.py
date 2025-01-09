from django.urls import path
from .import views

urlpatterns = [
    # path('<pk>',views.fun1)
    path('<pk>',views.fun1.as_view())
]
