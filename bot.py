# изменить названия кнопок

import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI
import time

bot = telebot.TeleBot('1944273740:AAEfH-Jxe0XVz141nX5LSSUZ1dTbVwr9XYI')

cg = CoinGeckoAPI()
SICK = True

crypto_course = cg.get_price(ids='bitcoin,ethereum,cardano,binancecoin,solana,ripple,dogecoin,'
                                 'polkadot,terra-luna,uniswap,chainlink,litecoin,'
                                 'bitcoin-cash,algorand', vs_currencies='usd')
crypto = "Курс криптовалют:\n" + f"\n· Bitcoin: {crypto_course['bitcoin']['usd']} $" \
         + f"\n· Ethereum: {crypto_course['ethereum']['usd']} $"\
         +f"\n· Cardano: {crypto_course['cardano']['usd']} $"\
         + f"\n· Binance Coin: {crypto_course['binancecoin']['usd']} $"\
         + f"\n· Solana: {crypto_course['solana']['usd']} $"\
         + f"\n· XRP: {crypto_course['ripple']['usd']} $"\
         + f"\n· Dogecoin: {crypto_course['dogecoin']['usd']} $"\
         + f"\n· Polkadot: {crypto_course['polkadot']['usd']} $"\
         + f"\n· Terra: {crypto_course['terra-luna']['usd']} $"\
         + f"\n· Uniswap: {crypto_course['uniswap']['usd']} $"\
         + f"\n· ChainLink: {crypto_course['chainlink']['usd']} $"\
         + f"\n· Litecoin: {crypto_course['litecoin']['usd']} $"\
         + f"\n· Bitcoin Cash: {crypto_course['bitcoin-cash']['usd']} $"\
         + f"\n· Algorand: {crypto_course['algorand']['usd']} $"\
         + "\n\nХотите автоматизировать? \nИспользуйте /settings"


@bot.message_handler(commands=['start'])
def start_bot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Курс крипты')
    button2 = types.KeyboardButton('Курс фиата')
    button3 = types.KeyboardButton('Информация')
    markup.add(button1, button2, button3)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}. Здесь ты можешь'
                                      ' следить за курсом криптовалют'
                                      ' и фиата! :)'.format(message.from_user), reply_markup=markup)


@bot.message_handler(commands=['settings'])
def bot_settings(message):
    bot.send_message(message.chat.id, 'Отправлять курс криптовалют каждые 15 минут - /15m'
                                      +'\nОтправлять курс криптовалют каждые 60 минут - /60m'
                                      +'\nОтправлять курс криптовалют каждые 24 часа - /24h'
                                      +'\nОтключить автоматизацию - /stop_crypto')

# TIME SETTINGS




@bot.message_handler(commands=['15m'])
def settings(message):
    SICK = True
    if message.text == "/15m":
        bot.send_message(message.chat.id, "Отлично! Теперь вы будете получать"
                                          " курс токенов каждые 15 минут.")
        time.sleep(5)
        while SICK:
            if message.text == "/stop_crypto":
                SICK = False

            bot.send_message(message.chat.id, crypto)
            time.sleep(3)


@bot.message_handler(commands=['stop_crypto'])
def crypto_stop(message):
    if message.text == "/stop_crypto":
        bot.send_message(message.chat.id, 'Приостановлено')



@bot.message_handler(content_types=['text'])
def bot_send_message(message):
    if message.chat.type == 'private':
        if message.text == "Курс крипты":
            bot.send_message(message.chat.id, crypto)

        elif message.text == 'Курс фиата':
            bot.send_message(message.chat.id, '1')

        elif message.text == 'Информация':
            bot.send_message(message.chat.id, 'Здесь представлена информация')


bot.polling()