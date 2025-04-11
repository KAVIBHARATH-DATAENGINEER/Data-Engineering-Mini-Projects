
import requests
import pandas as pd
from datetime import datetime
import mysql.connector


API_KEY="31e6b40ceaab29fad4106cdc7698d9bc"
CITY='Namakkal'
URL=f"https://api.openweathermap.org/data/2.5/weather?q={"Namakkal"}&appid={"31e6b40ceaab29fad4106cdc7698d9bc"}&units=metric"

def extract_data():
    response=requests.get(URL)
    data=response.json()
    return data

def transform_data(data):
    weather={
        "city": data["name"],
        "temperature": data["main"]["temp"],
        "humidity": data["main"]["humidity"],
        "pressure": data["main"]["pressure"],
        "weather": data["weather"][0]["main"],
        "description": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"],
        "timestamp": datetime.now()
    }
    df=pd.DataFrame([weather])
    return df
def load_data(df):
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Kavi@123",
        database="weather_db"
    )
    cursor=conn.cursor() 
    for _, row in df.iterrows():
        cursor.execute("INSERT INTO daily_weather(city,temperature,humidity,pressure,weather,description,wind_speed,timestamp)" 
                       "VALUES (%s,%s,%s,%s,%s,%s,%s,%s)",
                       tuple(row.values))
        
    conn.commit()
    cursor.close()
    conn.close()
 

def run_pipeline():
    print("!...Successfully Running weather data pipeline ( Python + Pandas + API+ Mysql )...!")
    data=extract_data()
    df=transform_data(data)
    load_data(df)  
run_pipeline()
    