from django.urls import path
from . import views

urlpatterns = [
    path ('', views.add_user,name="add_user"),
    path('delete/<int:id>/',views.delete_data,name='delete_data'),
    path('<int:id>',views.update_form,name='update_form'),
]

