from tkinter import *
from tkinter import ttk
from customtkinter import *
import requests
from tkinter import messagebox
import time
from datetime import datetime

root = CTk()
root.title('Weather APP')
root.iconbitmap('Weather_31085.ico')
root.geometry('600x500')
root.resizable(False, False)
root.config(background='#7ecbff')

search_city_entry = CTkEntry(root, bg_color='#7ecbff', corner_radius=20, font=('Comic Sans MS', 18),
                             placeholder_text='Enter City Name', width=300, height=50)
search_city_entry.place(relx=0.5, rely=0.1, anchor=CENTER)

search_image = PhotoImage(file='icons8.png')


def get_info():
    try:
        city_name_label.configure(text=search_city_entry.get().capitalize())
        city_name = (search_city_entry.get()).capitalize()
        api_key = '74186d51cd4ce64de11f515bfecd4d15'
        r = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}')
        data = r.json()
        weather = data['weather'][0]["main"]
        temperature = data["main"]["temp"]
        pressure = data["main"]["pressure"]
        humidity = data["main"]["humidity"]
        temperature_celsius = int(temperature - 273.15)
        date = data['dt']
        sunrise = data['sys']['sunrise']
        sunset = data['sys']['sunset']
        date_human = datetime.utcfromtimestamp(date).strftime('%Y-%m-%d %H:%M')
        sunrise_human = datetime.utcfromtimestamp(sunrise).strftime('%H:%M:%S')
        sunset_human = datetime.utcfromtimestamp(sunset).strftime('%H:%M:%S')
        temperature_info_label.configure(text=f"Temp {temperature_celsius}")
        humidity_info_label.configure(text=f"Humidity {humidity}")
        pressure_info_label.configure(text=f"Pressure {pressure}")
        air_condition_label.configure(text="Air Condition:")
        air_condition_info_label.configure(text=weather)
        date_label.configure(text=date_human)
        sunrise_label.configure(text=f"Sunrise: {sunrise_human}")
        sunset_label.configure(text=f"Sunset: {sunset_human}")
        if weather == 'Clouds':
            weather_image_label.configure(image=clouds_weather_image)
        elif weather == "Clear":
            weather_image_label.configure(image=clear_weather_image)
        elif weather == 'Rain':
            weather_image_label.configure(image=rainy_weather_image)
        elif weather == 'Snow':
            weather_image_label.configure(image=snow_weather_image)
        elif weather == 'Thunderstorm':
            weather_image_label.configure(image=stormy_weather_image)
        search_city_entry.delete(0, END)
    except:
        messagebox.showerror("Error", "Wrong City name or invalid input!")


search_button = Button(root, image=search_image, bd=0, bg="#7ecbff", command=get_info)
search_button.place(relx=0.80, rely=0.1, anchor=CENTER)

temperature_image = PhotoImage(file='icons8-thermometer-100.png')
humidity_image = PhotoImage(file='icons8-hygrometer-100.png')
pressure_image = PhotoImage(file='icons8-windsock-100.png')

temperature_label = CTkLabel(root, text="", image=temperature_image, bg_color='#7ecbff', width=10, height=10)
temperature_label.place(relx=0.20, rely=0.9, anchor=CENTER)

humidity_label = CTkLabel(root, text="", image=humidity_image, bg_color='#7ecbff', width=10, height=10)
humidity_label.place(relx=0.5, rely=0.9, anchor=CENTER)

pressure_label = CTkLabel(root, text="", image=pressure_image, bg_color='#7ecbff', width=10, height=10)
pressure_label.place(relx=0.8, rely=0.9, anchor=CENTER)

city_name_label = CTkLabel(root, text="", font=('Comic Sans MS', 31, 'bold'), bg_color='#7ecbff')
city_name_label.place(relx=0.5, rely=0.24, anchor=CENTER)

temperature_info_label = CTkLabel(root, text="...", bg_color="#7ecbff", font=("Comic Sans MS", 20, "bold"))
temperature_info_label.place(relx=0.20, rely=0.75, anchor=CENTER)

humidity_info_label = CTkLabel(root, text="...", font=("Comic Sans MS", 20, "bold"), bg_color="#7ecbff")
humidity_info_label.place(relx=0.5, rely=0.75, anchor=CENTER)

pressure_info_label = CTkLabel(root, text="...", font=("Comic Sans MS", 20, "bold"), bg_color="#7ecbff")
pressure_info_label.place(relx=0.8, rely=0.75, anchor=CENTER)

air_condition_label = CTkLabel(root, text="", font=("Comic Sans MS", 20, "bold"), bg_color="#7ecbff")
air_condition_label.place(relx=0.2, rely=0.35, anchor=CENTER)

air_condition_info_label = CTkLabel(root, text="", font=("Comic Sans MS", 20, "bold"), bg_color="#7ecbff")
air_condition_info_label.place(relx=0.5, rely=0.65, anchor=CENTER)

clear_weather_image = PhotoImage(file="icons8-weather-96.png")
clouds_weather_image = PhotoImage(file="icons8-clouds-100.png")
rainy_weather_image = PhotoImage(file="icons8-rain-100.png")
snow_weather_image = PhotoImage(file="icons8-snow-100.png")
stormy_weather_image = PhotoImage(file="icons8-stormy-64.png")

weather_image_label = CTkLabel(root, text="", image=None, bg_color="#7ecbff")
weather_image_label.place(relx=0.5, rely=0.43, anchor="center")

date_label = CTkLabel(root, text='', bg_color="#7ecbff", font=("Comic Sans MS", 20, "bold"))
date_label.place(relx=0.82, rely=0.45, anchor=CENTER)

sunrise_label = CTkLabel(root, text='', bg_color="#7ecbff", font=("Comic Sans MS", 15, "bold"))
sunrise_label.place(relx=0.82, rely=0.55, anchor=CENTER)

sunset_label = CTkLabel(root, text='', bg_color="#7ecbff", font=("Comic Sans MS", 15, "bold"))
sunset_label.place(relx=0.82, rely=0.60, anchor=CENTER)

root.bind("<Return>", lambda event: get_info())

root.mainloop()
