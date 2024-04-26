from django.contrib import admin
from django.urls import path,include
from. import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",views.homePage,name=""),
    path("login",views.login,name="login"),
    path("AboutUs",views.About,name="About"),
    path("ContactUs",views.Contact,name="Contact"),
    path("Register", views.registrationPage, name="register"),
    path("adminhome",views.adminhome,name="adminhome"),
    path("",include("adminapp.urls")),
]