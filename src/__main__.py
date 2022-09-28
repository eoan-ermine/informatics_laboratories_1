import os

import requests

city = "Moscow,RU"
appid = os.getenv("APP_ID")

if __name__ == "__main__":
	res = requests.get("http://api.openweathermap.org/data/2.5/weather", params={
		"q": city, "units": "metric", "lang": "ru", "APPID": appid
	})
	data = res.json()

	print("Город:", city)
	print("Погодные условия:", data["weather"][0]["description"])
	print("температура:", data["main"]["temp"])
	print("Минимальная температура:", data["main"]["temp_min"])
	print("Максимальная температура:", data["main"]["temp_max"])

	res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={
		"q": city, "units": "metric", "lang": "ru", "APPID": appid
	})
	data = res.json()

	print("Прогноз погоды на неделю")
	for element in data["list"]:
		print(
			"Дата <", element["dt_txt"], ">\r\nТемпература <{0:+3.0f}".format(element["main"]["temp"]),
			"> \r\nПогодные условия <", element["weather"][0]["description"], ">"
		)
		print("_____________________________")
