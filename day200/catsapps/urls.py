from django.urls import path

from . import views

app_name = "catsapps"

urlpatterns = [
    # HomePage
    path("", views.index, name="index"),
    path("name/", views.Names, name="names"), # "name/"- просто ссылка, views должен совпадать с нашей созданной функцией в ней, name="names"- как мы будем обращаться по ссылке в html
    path("namebycats/<int:name_id>", views.Namesbycats, name="name"), # 
    #path("colors/", views.colors, name="colors"),
    #path("colors/<int:color_id>", views.color, name="color"),
    #path("catss/", views.catss, name="catss"),
    #path("catss/<int:cats_id>", views.cats, name="cats"),
]
