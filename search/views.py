from django.shortcuts import render
from django.http import HttpResponse
import requests
global str
from .models import Word
from .forms import WordForm

def search_list(request):
    results = Word.objects.all()
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            print (results.last())
            a = results.last()
            b = "near=%s" % a
            url = ("https://api.foursquare.com/v2/venues/search/?"
                    "{0}"
                    "oauth_token=OXR3SOQTEPY4WKQZEKOSGHHK52MZZPRGPNA3CL25MQZKVKYJ&v=20170705"
                    .format(b))
            c = requests.get(url)
            d = c.text
            return HttpResponse(url)
        else:
            form = WordForm()
            return render(request, 'search/search_list.html', {'results' : results, "d": d})
    else:
        form = WordForm()
        return render(request, 'search/search_list.html', {'results' : results, "form": form})
