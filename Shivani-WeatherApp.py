import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + \
        city+"&appid=1bddb27de6fe856d12b27e8e9e0d2e1c"

    json_data = requests.get(api).json()

    description = json_data["weather"][0]["description"]
    temp = int(json_data['main']['temp'] - 273.15)
    min_temp = int(json_data['main']['temp_min'] - 273.15)
    max_temp = int(json_data['main']['temp_max'] - 273.15)
    pressure = int(json_data['main']['pressure'])
    humidity = int(json_data['main']['humidity'])
    sunrise = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunrise'] - 21600))
    sunset = time.strftime('%I:%M:%S', time.gmtime(json_data['sys']['sunset'] - 21600))
    visible = json_data["visibility"]
    lat = int(json_data["coord"]["lat"])
    lon = int(json_data["coord"]["lon"])
    w_speed = int(json_data["wind"]["speed"])
    deg = json_data["wind"]["deg"]

    if deg in [0, 360]:
        deg = "Towards North"
    elif deg > 0 and deg < 90:
      deg = "Towards North-East"
    elif deg == 90:
      deg = "Towards East"
    elif deg > 90 and deg < 180:
      deg = "Towards South-East"
    elif deg == 180:
      deg = "Towards South"
    elif deg > 180 and deg < 270:
      deg = "Towards South-West"
    elif deg == 270:
      deg = "Towards West"
    elif deg > 270 and deg < 360:
      deg = "Towards North-West"

    final_info = description + "\n" + str(temp) + "°C"
    final_data = "\n" + "Min Temp: " + str(min_temp) + "°C" + "\n" + "Max Temp: " + str(max_temp) + "°C"  + "\n" + "Pressure: " + str(pressure) + "milibars"
    + "\n" + "Humidity: " + str(humidity) + "%" + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset  + "\n" + "Visibility: " + str(visible) + "meters"
    + "\n" + "Lattitude: " + str(lat) + "\n" + "Longitude: " + str(lon) + "\n" + "Wind Speed: " + str(w_speed) + "miles per hour" + "\n" + "Degree: " + deg

    label1.config(text=final_info)
    label2.config(text=final_data)


#GUI
canvas = tk.Tk()
canvas.geometry("700x700")
canvas.title("Megh-Suryam")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width=20, font = t)
textField.pack(pady=20)
textField.focus()
textField.bind('<Return>', getWeather)
#Search_btn = tk.Button(canvas, text="Search Weather",width=12, command=getWeather)
#Search_btn.pack()

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()