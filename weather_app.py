import requests
city=input("enter city name:")
api_key="16753225629ae7da2cf45606f4da1f66"
url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
print("api key:",api_key)
print("url:",url)
response=requests.get(url)
data=response.json()
if data["cod"]==200:
    print("\nweather report")
    print("city:",data["name"])
    print("temperture:",data["main"]["temp"],"C")
    print("humidity:",data["main"]["humidity"],"%")
    print("weather:",data["weather"][0]["description"])
else:
    print("city not found!")