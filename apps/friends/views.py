from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index(request):
	context = {
		"users": User.objects.all()
	}
	return render(request, "friends/index.html", context)