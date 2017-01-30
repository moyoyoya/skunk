from django.shortcuts import render
from .forms import getDeeplink
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.


@login_required
def deeplink(request):
    if request.method == 'POST':
        getUrl = request.POST['URLField']
        if getUrl.is_valid():
            link = getUrl.clean()



    return render(request, 'account/dashboard.html', {'section': 'dashboard'})
