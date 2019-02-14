
#############
#Get the Altitude and Latitude of the robot
#############

import urllib
import requests
import json 

#http://api.ipstack.com/check?access_key=db74ee611adfab655cb0a527107ecf34

def getLocation():
  url = 'http://api.ipstack.com/check?access_key=db74ee611adfab655cb0a527107ecf34'
  resp = requests.get(url=url)
  data = resp.json() # Check the JSON Response Content documentation below
  #print(str(data['latitude'])+','+str(data['longitude']))
  #print(data['region_name'])
  return [data['latitude'],data['longitude']]

# Python program to find current 
# weather details of any city 
# using openweathermap api 


# Enter your API key here 
api_key = "f2c7492093041753eff23e654fb3c005"

# base_url variable to store url 
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Give city name 
city_name = 'Beirut'

# complete_url variable to store 
# complete url address 
complete_url = base_url + "appid=" + api_key + "&q=" + city_name 

# get method of requests module 
# return response object 
response = requests.get(complete_url) 

# json method of response object 
# convert json format data into 
# python format data 
x = response.json() 


# Now x contains list of nested dictionaries 
# Check the value of "cod" key is equal to 
# "404", means city is found otherwise, 
# city is not found 
if x["cod"] != "404": 

  # store the value of "main" 
  # key in variable y 
  y = x["main"] 

  # store the value corresponding 
  # to the "temp" key of y 
  current_temperature = y["temp"] -273.15

  # store the value corresponding 
  # to the "pressure" key of y 
  current_pressure = y["pressure"] 

  # store the value corresponding 
  # to the "humidity" key of y 
  current_humidiy = y["humidity"] 

  # store the value of "weather" 
  # key in variable z 
  z = x["weather"] 

  # store the value corresponding 
  # to the "description" key at 
  # the 0th index of z
  print( [current_temperature,current_humidiy])
else: 
  #return(-1)
  pass