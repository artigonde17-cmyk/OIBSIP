from tkinter import *
from weather_api import get_weather, get_forecast
from PIL import Image, ImageTk
import geocoder

# ---------------- WINDOW ----------------
root = Tk()
root.title("Weather Pro App")
root.geometry("420x650")
root.config(bg="#0f172a")   # dark blue background
root.resizable(False, False)

# ---------------- TITLE ----------------
title = Label(root, text="Weather App", font=("Arial", 20, "bold"),
              bg="#0f172a", fg="white")
title.pack(pady=10)

# ---------------- CITY INPUT ----------------
city_entry = Entry(root, font=("Arial", 14), justify="center")
city_entry.pack(pady=10)

# ---------------- ICON ----------------
icon_label = Label(root, bg="#0f172a")
icon_label.pack(pady=10)

# ---------------- RESULT CARD ----------------
frame = Frame(root, bg="#1e293b", padx=10, pady=10)
frame.pack(pady=10, fill="both", expand=True)

result = Label(frame, text="", font=("Arial", 12),
               bg="#1e293b", fg="white", justify="left")
result.pack()

forecast_label = Label(frame, text="", font=("Arial", 10),
                       bg="#1e293b", fg="white", justify="left")
forecast_label.pack(pady=10)

# ---------------- ICON FUNCTION ----------------
def show_icon(condition):

    condition = condition.lower()

    if "clear" in condition:
        path = "icons/sunny.png"
    elif "cloud" in condition:
        path = "icons/cloudy.png"
    elif "rain" in condition:
        path = "icons/rain.png"
    elif "thunder" in condition:
        path = "icons/thunder.png"
    else:
        path = "icons/cloudy.png"

    img = Image.open(path)
    img = img.resize((100, 100))
    photo = ImageTk.PhotoImage(img)

    icon_label.config(image=photo)
    icon_label.image = photo

# ---------------- FORECAST ----------------
def show_forecast(city):

    data = get_forecast(city)

    if data:

        text = "5-Day Forecast\n\n"

        for i in range(0, 40, 8):
            d = data['list'][i]
            temp = d['main']['temp']
            desc = d['weather'][0]['main']

            text += f"Day {i//8+1}: {temp}°C | {desc}\n"

        forecast_label.config(text=text)

# ---------------- SEARCH WEATHER ----------------
def search_weather(city=None):

    if not city:
        city = city_entry.get()

    data = get_weather(city)

    if data:

        temp = data['main']['temp']
        humidity = data['main']['humidity']
        wind = data['wind']['speed']
        condition = data['weather'][0]['main']

        show_icon(condition)
        show_forecast(city)

        result.config(text=
            f"City: {city}\n"
            f"Temperature: {temp}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind: {wind} m/s\n"
            f"Condition: {condition}"
        )

    else:
        result.config(text="City Not Found")

# ---------------- AUTO LOCATION ----------------
def auto_location():

    g = geocoder.ip('me')
    city = g.city

    if city:
        city_entry.delete(0, END)
        city_entry.insert(0, city)
        search_weather(city)

# ---------------- BUTTONS ----------------
btn_frame = Frame(root, bg="#0f172a")
btn_frame.pack(pady=10)

Button(btn_frame, text="Search", width=12, command=search_weather,
       bg="#38bdf8", fg="black").grid(row=0, column=0, padx=5)

Button(btn_frame, text="My Location", width=12, command=auto_location,
       bg="#22c55e", fg="black").grid(row=0, column=1, padx=5)

# ---------------- AUTO START ----------------
auto_location()

# ---------------- RUN ----------------
root.mainloop()
