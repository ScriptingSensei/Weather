import tkinter as tk
import requests
import tkinter.messagebox
from PIL import ImageTk, Image

base = tk.Tk()

base.title("Weather App")
base.configure(bg="blue")
base.geometry("700x600")

# Load weather image
img = Image.open("C:/Users/Asus/Downloads/weather.png")
img = img.resize((150, 150))
img = ImageTk.PhotoImage(img)

# Widgets
title_1 = tk.Label(text="Weather App", width=15, font=("bold", 30), bg="blue")
weather_logo = tk.Label(base, image=img, bg="blue")
title_2 = tk.Label(text="Enter City name:", width=32, font=("italic", 15), bg="blue")
search_city = tk.Entry(base)

def search_weather():
    api_key = "14ed2a78adcbcbfe1ac9d1ffb8c5eea6"
    base_url = "https://api.openweathermap.org/data/2.5/weather?"
    city_name = search_city.get()
    complete_url = f"{base_url}q={city_name}&appid={api_key}"

    response = requests.get(complete_url)
    x = response.json()

    try:
        if x['cod'] != '400':
            y = x['main']
            temp_High = round(y['temp_max'] - 273.15)
            temp_Low = round(y['temp_min'] - 273.15)
            pressure_value = y['pressure']
            hum_value = y['humidity']

            z = x['weather']
            description_weather = z[0]['description']

            m = x['sys']
            country_detail = m['country']

            temp_high_rs.configure(text=f"{temp_High} °C")
            temp_low_rs.configure(text=f"{temp_Low} °C")
            pres_rs.configure(text=f"{pressure_value} Pa")
            hum_rs.configure(text=f"{hum_value} g/Kg")
            des_rs.configure(text=description_weather)
            coun_rs.configure(text=country_detail)
        else:
            raise Exception("City not found")

    except Exception as e:
        tkinter.messagebox.showinfo("Error", f"Error: {e}")

button_search = tk.Button(text="Search", bg="white", command=search_weather)

def close_app():
    closeapp = tkinter.messagebox.askyesno("Weather App", "Do you want to exit?")
    if closeapp:
        base.destroy()

def credits_func():
    tkinter.messagebox.showinfo(title="Credits", message='''
    Made by:
    - Musawwir
    - Owais

    GPL V4 License 2024''')

# Menu
menubar = tk.Menu(base)
base.configure(menu=menubar)
submenu1 = tk.Menu(menubar, tearoff=0)
submenu2 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label="File", menu=submenu1)
menubar.add_cascade(label="Help", menu=submenu2)
submenu1.add_command(label="Exit", command=close_app)
submenu2.add_command(label="About", command=credits_func)

# Labels for weather data
temp_high = tk.Label(text="Temp (high):", width=20, font=("bold", 20), bg="blue")
temp_high_rs = tk.Label(text="", width=20, font=("bold", 20), bg="blue")
temp_low = tk.Label(text="Temp (low):", width=20, font=("bold", 20), bg="blue")
temp_low_rs = tk.Label(text="", width=20, font=("bold", 20), bg="blue")
pres = tk.Label(text="Pressure:", width=20, font=("bold", 20), bg="blue")
pres_rs = tk.Label(text="", width=20, font=("bold", 20), bg="blue")
hum = tk.Label(text="Humidity:", width=20, font=("bold", 20), bg="blue")
hum_rs = tk.Label(text="", width=20, font=("bold", 20), bg="blue")
desc = tk.Label(text="Description:", width=20, font=("bold", 20), bg="blue")
des_rs = tk.Label(text="", width=20, font=("bold", 20), bg="blue")
coun = tk.Label(text="Country:", width=20, font=("bold", 20), bg="blue")
coun_rs = tk.Label(text="", width=20, font=("bold", 20), bg="blue")

# Footer labels
footer_1 = tk.Label(text="Temperature is measured in Degrees Celsius", bg="blue")
footer_2 = tk.Label(text="Pressure in Pascals (Pa)", bg="blue")
footer_3 = tk.Label(text="Humidity is measured in grams Per Kilogram of air (g/Kg)", bg="blue")

# Grid layout
title_1.grid(row=0, column=2)
weather_logo.grid(row=1, column=2)
title_2.grid(row=2, column=2)
search_city.grid(row=3, column=2)
button_search.grid(row=3, column=3)
temp_high.grid(row=4, column=2)
temp_high_rs.grid(row=4, column=3)
temp_low.grid(row=5, column=2)
temp_low_rs.grid(row=5, column=3)
pres.grid(row=6, column=2)
pres_rs.grid(row=6, column=3)
hum.grid(row=7, column=2)
hum_rs.grid(row=7, column=3)
desc.grid(row=8, column=2)
des_rs.grid(row=8, column=3)
coun.grid(row=9, column=2)
coun_rs.grid(row=9, column=3)
footer_1.grid(row=10, column=2)
footer_2.grid(row=11, column=2)
footer_3.grid(row=12, column=2)

base.mainloop()
