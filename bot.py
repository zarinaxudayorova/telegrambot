import logging

from aiogram import Bot, Dispatcher, executor, types
import requests

def quran_uzb(sura,oyat):
    url_uz = f"https://cdn.jsdelivr.net/gh/fawazahmed0/quran-api@1/editions/uzb-muhammadsodikmu.json"
    r = requests.get(url_uz).json()
    for quran in r["quran"]:
       if quran['chapter'] == sura and quran['verse'] == oyat:
           return str(quran['text'])

API_TOKEN = '7588394007:AAG8XFyHR_elA1cH1NAd2_7tJLm4o6n2yz8'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply("Salom, men sizga qur'on oyatlarini topishda yordam beraman\nsura va oyat raqamini vergul bilan ajratgan xolda kiriting : ")


@dp.message_handler()
async def echo(message: types.Message):
    d = message.text
    sura=int(d.split(",")[0])
    oyat = int(d.split(",")[1])
    oyat_matni = quran_uzb(sura,oyat)
    await message.answer(oyat_matni)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)