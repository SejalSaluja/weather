from django.shortcuts import render

# Create your views here.
from django.shortcuts import render 
# import json to load json data to python dictionary 
import json 
# urllib.request to make a request to api 
import urllib.request 
from .models import WeatherData
  
def index(request): 
    if request.method == 'POST': 
        city = request.POST['city'] 
        ''' api key might be expired use your own api_key 
            place api_key in place of appid ="your_api_key_here "  '''
  
        # source contain JSON data from API 
  
        source = urllib.request.urlopen( 
            'http://api.openweathermap.org/data/2.5/weather?q=' 
                    + city + '&appid=3aab12700e72d88d3f3e4b1bad2eea09').read() 
  
        # converting JSON data to a dictionary 
        list_of_data = json.loads(source) 
  
        # data for variable list_of_data 
        wd = WeatherData()
        wd.city = city
        wd.country_code = str(list_of_data['sys']['country'])
        wd.temperature = str(list_of_data['main']['temp']) + 'k'
        wd.pressure =  str(list_of_data['main']['pressure'])
        wd.humidity = str(list_of_data['main']['humidity'])
        wd.save()
        wbdata = WeatherData.objects.all().order_by('-timestamp')
        data = { 
            "wbdata": wbdata,
            "country_code": str(list_of_data['sys']['country']), 
            "coordinate": str(list_of_data['coord']['lon']) + ' '
                        + str(list_of_data['coord']['lat']), 
            "temp": str(list_of_data['main']['temp']) + 'k', 
            "pressure": str(list_of_data['main']['pressure']), 
            "humidity": str(list_of_data['main']['humidity']), 
        } 
        print(data) 
    else: 
        data ={} 
        return render(request, "index.html", data)