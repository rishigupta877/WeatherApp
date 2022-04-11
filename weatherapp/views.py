from django.shortcuts import render
import json
import urllib.request

#import requests
# Create your views here.
def index(request):

    if request.method=='POST':
        city=request.POST['city']
        source=urllib.request.urlopen('https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=c841bb4827f326add84d109610ce401c').read()
        list_of_data=json.loads(source)

        data={
            "country_code": str(list_of_data['sys']['country']),
            "coordinate": str(list_of_data['coord']['lon']) + ','
                        + str(list_of_data['coord']['lat']),
            "temp": str(list_of_data['main']['temp'])+'°C',
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
           

        }
        print(data)
    else:
        data={}
    
   # print(r.text)
    return render(request,'weatherapp/index.html',data)