import datetime
from django.shortcuts import render
from  myapp.forms import LoginForm

def hello(request):
    today = datetime.datetime.now().date()
    return render(request, "hola.html", {"today": today})
def login(request):
    username = 'not logged in'
    if request.method =="POST":
        MyLoginForm = LoginForm(request.POST)
        if MyLoginForm.is_valid():
            username = MyLoginForm.cleaned_data['username']
        else:
            MyLoginForm = LoginForm()
        return render(request, "loggedin.html",{"username": username})





