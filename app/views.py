from django.shortcuts import render,redirect
import requests
from .forms import WeatherForm

import datetime
import json

# Create your views, here.
def home(request):
      form=WeatherForm()
      if request.method=='POST':
            dataentry=False
          
            form=WeatherForm(request.POST)
            if form.is_valid():
                  city=form.cleaned_data['city']
                  BASE_URL="https://api.openweathermap.org/data/2.5/forecast?"
                  API_KEY=open("api.txt","r").read()
                  
                  
                 
                  CITY=city
                
                  url=BASE_URL +"appid="+API_KEY+"&q="+CITY
                  response=requests.get(url).json()
             
                  current_time = datetime.datetime.now()
                  formatted_datetime = current_time.strftime("%H")
                  
                  
                  def indexfinder(response,formatted_datetime):
                        list=[]
                        for i in range(0,40): 
                              timestamp=response['list'][i]['dt_txt']
                              datetime_obj = datetime.datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                              formatted_timestamp = datetime_obj.strftime("%H")
                              limit=[int(formatted_datetime),int(formatted_datetime)+1,int(formatted_datetime)+2]
                        
                              if int(formatted_timestamp) in limit:
                                 list.append(i)
                        return list
                        
                 
                  data=[]
                  index=indexfinder(response,formatted_datetime)
                  for l in index:
                        data.append(response['list'][l])
                    
                  days_details=[]  
                  for r in data:
                  
                        # print(r)
                        days_details.append({
                        "icon":r['weather'][0]['icon'],
                        "days": datetime.datetime.fromtimestamp(r['dt']).strftime("%A"),
                        "temperature_celcius":round(r['main']['temp']-273.15,2),
                  
                        "description":r['weather'][0]['description'],
                        "icon":r['weather'][0]['icon'],
                        "humidity":r['main']['humidity'],
                        "Wind":round(r['wind']['speed']*(3.6),2),
                        "date_time":r['dt_txt'][0:10]
                  })
                  form=WeatherForm()
                  
                  dataentry=True
                  context={
                  'days_details':days_details,
                  'form':form,
                  'city':city,
                  'current_time':current_time,
                  'dataentry':dataentry
                  

                  }
            
                  return render(request,'app/home.html',context)
      return render(request,'app/home.html',{'form':form})

def features(request):
      return render(request,'app/features.html')