from django.shortcuts import render
from django.http import HttpResponse
import requests
import simplejson as json
from .models import Word
from .forms import WordForm

def search_list(request):
    results = Word.objects.all()
    previous_searches = results.order_by("-created_time")
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            print (results.last())
            a = results.last()
            b = "near=%s" % a
            url = ("https://api.foursquare.com/v2/venues/search/?"
                    "{0}"
                    "&oauth_token=OXR3SOQTEPY4WKQZEKOSGHHK52MZZPRGPNA3CL25MQZKVKYJ&v=20170705"
                    .format(b))
            data = requests.get(url)
            text = data.text
            data = json.loads(text)
            response = data["response"]
            venues = response["venues"]
            return render(request, 'search/search_list.html', {'results' : results, "venues": venues, 'previous_searches': previous_searches, "form": form})
        else:
            form = WordForm()
            return render(request, 'search/search_list.html', {'results' : results, "venues": venues, 'previous_searches': previous_searches})
    else:
        form = WordForm()
        return render(request, 'search/search_list.html', {'results' : results, "form": form, 'previous_searches': previous_searches})
