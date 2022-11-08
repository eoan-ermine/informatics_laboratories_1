import os
import sys

import requests

city = "Moscow,RU"
appid = os.getenv("APP_ID")

if __name__ == "__main__":
	res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={
		"q": city, "units": "metric", "lang": "ru", "APPID": appid
	})
	if res.status_code != 200:
		print("Error, can't retrieve current weather information")
		sys.exit(1)
	data = res.json()

	print("Город:", city)
	print("Погодные условия:", data["weather"][0]["description"])
	print("Температура:", data["main"]["temp"])
	print("Минимальная температура:", data["main"]["temp_min"])
	print("Максимальная температура:", data["main"]["temp_max"])
	print("Видимость (м):", data["visibility"])
	print("Скорость ветра (м/c):", data["wind"]["speed"])

	res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={
		"q": city, "units": "metric", "lang": "ru", "APPID": appid
	})
	if res.status_code != 200:
		print("Error, can't retrieve forecast")
		sys.exit(1)
	data = res.json()

	print("\nПрогноз погоды на неделю\n")
	for element in data["list"]:
		print(f"Дата <{element['dt_txt']}>")
		print("Температура <{0:+3.0f}>".format(element["main"]["temp"]))
		print(f"Видимость (м) <{element['visibility']}>")
		print(f"Скорость ветра (м/с) <{element['wind']['speed']}>")
		print(f"Погодные условия <{element['weather'][0]['description']}>")
		print("_____________________________\n")
