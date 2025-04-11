CREATE DATABASE weather_db;
USE weather_db;
CREATE TABLE daily_weather(
city VARCHAR(50),
temperature FLOAT,
humidity INT,
pressure INT,
weather VARCHAR(50),
description VARCHAR(100),
wind_speed FLOAT, 
timestamp DATETIME
);
