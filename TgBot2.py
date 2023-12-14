import telebot
import requests
import json

bot =telebot.TeleBot('6644985919:AAGO1S79Nq89Bp4zmxhTqhlSjKPHmqbYzqk')
API = 'd5f96faac7424ec682b124433231412'

@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Привет, я супер-пупер-ДУПЕР бот, который запрограммирован супер-пупер-ДУПЕР девчонками: Сонькой и Оксанкой. \nЯ подскажу тебе погоду и помогу с выбором одежды. В каком городе ты сейчас находишься?')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city=message.text.strip().lower()
    res = requests.get(f'http://api.weatherapi.com/v1/current.json?key=d5f96faac7424ec682b124433231412&q={city}&aqi=no')
    data = json.loads(res.text)
    if data["current"]["temp_c"]<-5: t='В такую погоду очень легко заболеть. Одевайся теплее, не забудь шапку и шарф!'
    elif data["current"]["temp_c"]<10: t='Погода прохладная. Стоит надеть куртку'
    else: t='Погода - супер! Самое время пойти на прогулку :)'
    bot.reply_to(message, f'Сейчас погода: {data["current"]["temp_c"]}. {t}')

bot.polling(none_stop=True)