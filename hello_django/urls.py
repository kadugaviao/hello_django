from django.contrib import admin
from django.urls import path
from core import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/<nome>/<int:idade>/', views.hello),
    path('soma/<int:num1>/<int:num2>/', views.soma),
    path('subtrai/<int:num1>/<int:num2>', views.subtrai),
    path('divide/<int:num1>/<int:num2>', views.divide),
    path('multiplica/<int:num1>/<int:num2>', views.multiplica),
]
