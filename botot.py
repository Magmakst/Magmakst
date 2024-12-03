import telebot
bot = telebot.TeleBot(token='8144702224:AAFSDpqfzNLqygIYroGFyDVsCnmL4HaVkI8')

user_data = {}
#функція для того щоп при прописаній ключовій команді старт в нас бот видавав готовий текст
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я допоможу тобі підрахувати твої калорії. Спочатку введи свою вагу (в кг):")

    user_data[message.chat.id] = {}
#бере інформацію з юзера про нього
@bot.message_handler(func=lambda message: True)
def handle_message(message):

    chat_id = message.chat.id
    if chat_id not in user_data:
        bot.reply_to(message, "Напиши /start, щоб почати!")
        return
    user = user_data[chat_id]
    if 'weight' not in user:
        try:
            user['weight'] = float(message.text)
            bot.reply_to(message, "Супер! Тепер введи свій зріст (в см):")
        except ValueError:
            bot.reply_to(message, "Будь ласка, введи вагу числом, наприклад: 70")
        return
    if 'height' not in user:
        try:
            user['height'] = float(message.text)
            bot.reply_to(message, "Дякую! А тепер введи свій вік (у роках):")
        except ValueError:
            bot.reply_to(message, "Будь ласка, введи зріст числом, наприклад: 170")
        return
    if 'age' not in user:
        try: # підрахунок калорій
            user['age'] = int(message.text)
            weight = user['weight']
            height = user['height']
            age = user['age']
            calories = 10 * weight + 6.25 * height - 5 * age + 5
            bot.reply_to(message, f"Твоя базова потреба в калоріях: {calories:.2f} ккал/день.")
        except ValueError:
            bot.reply_to(message, "Будь ласка, введи вік числом, наприклад: 25")
        return

bot.polling(non_stop=True )
