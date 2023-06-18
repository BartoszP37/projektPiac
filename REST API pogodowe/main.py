from flask import Flask, render_template, request
import requests

app=Flask(__name__)

def format_response(city):
    klucz_pogody="52ff15924d03f1cae4583ae82e3434a0"
    url="https://api.openweathermap.org/data/2.5/weather"
    params={"APPID": klucz_pogody, "q":city, "units":"Metric"}
    odpowiedz=requests.get(url,params=params)
    weather=odpowiedz.json()
    name=weather['name']
    desc=weather['weather'][0]['description']
    temp=weather['main']['temp']
    hum=weather['main']['humidity']
    wind_speed = weather['wind']['speed']
    clouds = weather['clouds']['all']
    pressure = weather['main']['pressure']
    return "City: %s Condition: %s Temperature: %s°C Humidity: %s%% Wind Speed: %s m/s Cloudiness: %s%% Pressure: %s hPa" % (
        name, desc, temp, hum, wind_speed, clouds, pressure)

@app.route('/', methods=['POST','GET'])
def home():
    if request.method=='GET':
        return render_template('home.html')
    if request.method == 'POST':
        city = request.form['city'] 
        weather_data = format_response(city)
        return render_template('home.html', data=weather_data)
    return render_template('home.html')

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0', port=80)