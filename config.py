import telebot

bot = telebot.TeleBot('5893039898:AAFlpUzBXR7A4Nan04OQmw3FhkcRoxmpvU0')
RAPIDAPI_KEY = "f7889a0e0cmsh5abcf4290d9f9a9p1306e7jsn7079fec31c86"

locations_url = "https://hotels4.p.rapidapi.com/locations/v3/search"

properties_url = "https://hotels4.p.rapidapi.com/properties/v2/list"

location_detail_url = "https://hotels4.p.rapidapi.com/properties/v2/detail"

headers = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "f7889a0e0cmsh5abcf4290d9f9a9p1306e7jsn7079fec31c86",
    "X-RapidAPI-Host": "hotels4.p.rapidapi.com"
}