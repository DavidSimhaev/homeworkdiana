from django.shortcuts import render
from .models import Name,Color,Cat

# Create your views here.
def index(request):
    """Home page of application"""
    return render(request, "catsapps/index.html" )

def Names(request):
    name = Name.objects.all() # Достаем все данные по имени кошки 
    content = {"NAME":name} # NAME ключ по которому мы будем обращаться в html
    return render(request, "catsapps/name.html", content) # "<---catsapps/name.html" наш html 


def Namesbycats(request, name_id):
    name = Cat.objects.filter(id=name_id) # Здесь мы отбираем котов по их айди имени, то что у тебя было тоже можно сделать, но это будет запутанная логика
    context = { "NAMESBYCATS": name}
    return render(request, "catsapps/namesbycats.html", context) # Все правильно , только айди нужно присваивать в "catsapps/name.html и добавить в url <int:name_id>" 

# Дальше пробуй и старайся разнообразить с именами функцией, так ты не запутаешься 



