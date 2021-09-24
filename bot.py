import telebot
from telebot import types
from pycoingecko import CoinGeckoAPI
from py_currency_converter import convert
import time
import stockquotes

############## PYPI
#### CRYPTOCURRENCY: pip install pycoingecko
#### FIAT: pip install py-currency-converter
#### STOCKS: pip install stockquotes

bot = telebot.TeleBot('1944273740:AAEfH-Jxe0XVz141nX5LSSUZ1dTbVwr9XYI')

cg = CoinGeckoAPI()
SICK = True


@bot.message_handler(commands=['start'])
def start_bot(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('Курс крипты ₿')
    button2 = types.KeyboardButton('Курс фиата 💲')
    button3 = types.KeyboardButton('Информация 📜')
    button4 = types.KeyboardButton('Главная 🌍')
    button5 = types.KeyboardButton('Курс акций 📈')
    markup.add(button4, button1, button2, button5, button3)
    bot.send_message(message.chat.id, 'Привет, {0.first_name}. '
                                      'Я рад тебя видеть! :)'.format(message.from_user), reply_markup=markup)

'''BUTTONS CRYPTOCURRENCY, FIAT AND etc'''

# FROM COINGECKO
crypto_course = cg.get_price(ids='bitcoin,ethereum,cardano,binancecoin,solana,ripple,dogecoin,'
                                     'polkadot,terra-luna,uniswap,chainlink,litecoin,'
                                     'bitcoin-cash,algorand', vs_currencies='usd')
crypto = "Курс криптовалют:\n" + f"\n· Bitcoin: {crypto_course['bitcoin']['usd']} $" \
             + f"\n· Ethereum: {crypto_course['ethereum']['usd']} $" \
             + f"\n· Cardano: {crypto_course['cardano']['usd']} $" \
             + f"\n· Binance Coin: {crypto_course['binancecoin']['usd']} $" \
             + f"\n· Solana: {crypto_course['solana']['usd']} $" \
             + f"\n· XRP: {crypto_course['ripple']['usd']} $" \
             + f"\n· Dogecoin: {crypto_course['dogecoin']['usd']} $" \
             + f"\n· Polkadot: {crypto_course['polkadot']['usd']} $" \
             + f"\n· Terra: {crypto_course['terra-luna']['usd']} $" \
             + f"\n· Uniswap: {crypto_course['uniswap']['usd']} $" \
             + f"\n· ChainLink: {crypto_course['chainlink']['usd']} $" \
             + f"\n· Litecoin: {crypto_course['litecoin']['usd']} $" \
             + f"\n· Bitcoin Cash: {crypto_course['bitcoin-cash']['usd']} $" \
             + f"\n· Algorand: {crypto_course['algorand']['usd']} $" \
             + "\n\nУзнать больше /information"



#FROM CONVERT
fiat_course = convert(amount=1, to=['RUB', 'EUR', 'UAH', 'AUD', 'BGN', 'BRL', 'GBP', 'ISK',
                                    'KZT', 'MXN', 'NOK', 'CZK', 'JPY', 'PHP', 'CNY', 'RON', 'INR'])

fiat = "Курс фиата:\n" + f"\n•🇷🇺 1 USD в RUB {fiat_course['RUB']}"\
       + f"\n•🇪🇺 1 USD в EUR {fiat_course['EUR']}"\
       + f"\n•🇺🇦 1 USD в UAH {fiat_course['UAH']}"\
       + f"\n•🇦🇺 1 USD в AUD {fiat_course['AUD']}"\
       + f"\n•🇧🇬 1 USD в BGN {fiat_course['BGN']}"\
       + f"\n•🇧🇷 1 USD в BRL {fiat_course['BRL']}"\
       + f"\n•🇬🇧 1 USD в GBP {fiat_course['GBP']}"\
       + f"\n•🇮🇸 1 USD в ISK {fiat_course['ISK']}"\
       + f"\n•🇰🇿 1 USD в KZT {fiat_course['KZT']}"\
       + f"\n•🇲🇽 1 USD в MXN {fiat_course['MXN']}"\
       + f"\n•🇳🇴 1 USD в NOK {fiat_course['NOK']}"\
       + f"\n•🇨🇿 1 USD в CZK {fiat_course['CZK']}"\
       + f"\n•🇯🇵 1 USD в JPY {fiat_course['JPY']}"\
       + f"\n•🇵🇭 1 USD в PHP {fiat_course['PHP']}"\
       + f"\n•🇨🇳 1 USD в CNY {fiat_course['CNY']}"\
       + f"\n•🇷🇴 1 USD в RON {fiat_course['RON']}"\
       + f"\n•🇮🇳 1 USD в INR {fiat_course['INR']}" \
         f"\n\nУзнать больше /information"



# INFORMATION

information = 'Здесь представлена вся информация о боте.\n\n' \
              '• Команды:\n' \
              '/start - Запустить бота.\n' \
              '/15cmin - Отправлять курс криптовалют каждые 15 минут.\n' \
              '/60cmin - Отправлять курс криптовалют каждые 60 минут.\n' \
              '/24chours - Отправлять курс криптовалют каждые 24 часа.\n' \
              '/stop_crypto - Отключить автоматизацию по криптовалюте.\n' \
              '/15fmin - Отправлять курс фиата каждые 15 минут.\n' \
              '/60fmin - Отправлять курс фиата каждые 60 минут.\n' \
              '/24fhourse - Отправлять курс фиата каждые 24 часа.\n' \
              '/stop_fiat - Отключить автоматизацию по фиату.\n\n' \
              '• Отказ от ответственности:' \
              '\nВсё, что предоставляет бот, предназначено только для информационных целей.' \
              ' Мы не рекомендуем владеть, продавать или покупать тот или инной актив.' \


# STONCKS

stocks = 'AAPL', 'MSFT', 'GOOGL', 'AMZN', 'FB', 'TSLA', 'NVDA', 'V', 'JNJ', 'PYPL'
apple, microsoft, google, amazon, facebook, tesla,\
    nvidia, visa, johnson, paypal = stockquotes.Stock(stocks[0]), stockquotes.Stock(stocks[1]), \
                                       stockquotes.Stock(stocks[2]), stockquotes.Stock(stocks[3]),\
                                       stockquotes.Stock(stocks[4]), stockquotes.Stock(stocks[5]), \
                                       stockquotes.Stock(stocks[6]), stockquotes.Stock(stocks[7]), \
                                       stockquotes.Stock(stocks[8]), stockquotes.Stock(stocks[9])

AAPL, MSFT, GOOGL, AMZN, FB, TSLA, NVDA, V, JNJ,\
    PYPL = apple.current_price, microsoft.current_price, google.current_price,\
                                        amazon.current_price, facebook.current_price, tesla.current_price,\
                                        nvidia.current_price, visa.current_price, johnson.current_price, \
                                        paypal.current_price

course = f'· Apple Inc: {AAPL}$\n· Microsoft: {MSFT}$\n· Alphabet Inc (Google): {GOOGL}$' \
        f'\n· Amazon Inc: {AMZN}$\n· Facebook Inc: {FB}$' \
        f'\n· Tesla Inc: {TSLA}$\n· NVIDIA: {NVDA}$\n· Visa Inc: {V}$' \
        f'\n· Johnson & Johnson: {JNJ}$\n· PayPal Inc: {PYPL}$' \
         f'\n\nУзнать больше /information'

# MAIN

main = 'Следить за курсом криптовалют, фиата и акциями никогда не было так просто!\n' \
       '\nВедь сейчас Bitcoin стоит ' + f'{crypto_course["bitcoin"]["usd"]} $, 1 доллар равняется ' + \
       f'{fiat_course["RUB"]} ₽, а акция Apple Inc {AAPL}$.\n' + \
       '\nС помощью бота, ты можешь следить за курсом криптовалют, фиата и акциями, а также настраивать,' \
       ' чтобы тебе курс приходил автоматически, подробнее: /information'

'''BUTTONS CRYPTOCURRENCY, FIAT AND etc'''



# TIME SETTINGS


@bot.message_handler(commands=['15cmin'])
def settings(message):
    SICK = True
    if message.text == "/15cmin":
        bot.send_message(message.chat.id, "Отлично! Теперь вы будете получать"
                                          " курс токенов каждые 15 минут.")
        time.sleep(5)
        while SICK:
            if message.text == "/stop_crypto":
                SICK = False

            bot.send_message(message.chat.id, crypto + '\nПриостановить автоматизацию: /stop_crypto')
            time.sleep(3)


@bot.message_handler(commands=['stop_crypto'])
def crypto_stop(message):
    if message.text == "/stop_crypto":
        bot.send_message(message.chat.id, 'Приостановлено')



@bot.message_handler(content_types=['text'])
def bot_send_message(message):
    if message.chat.type == 'private':
        if message.text == "Курс крипты ₿":
            bot.send_message(message.chat.id, crypto)

        elif message.text == 'Курс фиата 💲':
            bot.send_message(message.chat.id, fiat)

        elif message.text == 'Главная 🌍':
            bot.send_message(message.chat.id, main)

        elif message.text == 'Курс акций 📈':
            bot.send_message(message.chat.id, course)

        elif message.text == 'Информация 📜' or '/information':
            bot.send_message(message.chat.id, information)


bot.polling()