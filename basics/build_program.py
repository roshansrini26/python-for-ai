"""
Functions
"""
def greet():
    name = "Roshan"
    if name == "Roshan":
        print(f"Hello{name}!")
    else:
        print("Hello, stranger!")

greet()  # Output: Hello Roshan!

"""
Local variables are defined inside a function and can only be accessed within that function.
"""

def calculate_price():
    pencil = 10
    eraser = 5
    total = pencil + eraser
    print(f"Total price: {total}")
    return total

result = calculate_price()  # Output: Total price: 15

"""
GLobal variables are defined outside of functions and can be accessed anywhere in the code.
"""

discount_rate = 0.2

def apply_discount(price):
    discount = price * discount_rate
    return price - discount

apply_discount(result) 

"""
Parameters and return 
"""

"""
Packages

Let’s clarify what these terms mean:
    Module: A single Python file (like math.py)
    Package: A folder containing multiple modules
    Function: A reusable block of code (like print() or sqrt())
    Class: A blueprint for creating objects 
Think of it like this:
    A module is like a toolbox
    A package is like a garage with multiple toolboxes
    A function is like a specific tool (hammer, screwdriver)
    A class is like a blueprint for building tools

pip freeze to list installed packages
"""

"""
Working with API: Pull data from Web services
"""

import requests

lat = 48.85
lon = 2.35

url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m"

response = requests.get(url)
data = response.json()

print(data)

temp = data['current']['temperature_2m']
print(temp)

"""
Building API converting to data
"""

import requests
from datetime import datetime, timedelta

today = datetime.now()
prev_week = today - timedelta(days=7)

start_date = prev_week.strftime("%Y-%m-%d") #strftime converts datetime, date or time object into a formatted string
end_date = today.strftime("%Y-%m-%d")

url = f"https://api.open-meteo.com/v1/forecast?latitude=48.85&longitude=2.35&start_date={start_date}&end_date={end_date}&daily=temperature_2m_max,temperature_2m_min"

response = requests.get(url)
data = response.json()

import pandas as pd

daily_data = data['daily']

df = pd.DataFrame({
    'date': daily_data['time'],
    'max_temp': daily_data['temperature_2m_max'],
    'min_temp': daily_data['temperature_2m_min']
})

df['date'] = pd.to_datetime(df['date'])

print(df)

