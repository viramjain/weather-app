from django.shortcuts import render
import requests

# Create your views here.
def Home(request):

    return render(request,'weather/home2.html')
def Temp(request):

    if request.method=='POST':
        city=request.POST['s']
        url="http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&APPID=9e67ca9c3c37db5040bb049b7f067ca9"

        r= requests.get(url.format(city)).json()
        city_weather={
        'city':city,
        'temprature':r['main']['temp'],
                }
        context={
        'a':city_weather,
            }
        print(city_weather)
        return render(request,'weather/home1.html',context)

    else:
        return render(request,'weather/home2.html')
def About(req):
    return render(req,'weather/about.html')
def Contact(req):
    return render(req,'weather/Contact.html')