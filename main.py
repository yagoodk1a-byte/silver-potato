import telebot

from config import TOKEN
from utils import calculate_chests, calculate_numbers


bot = telebot.TeleBot(TOKEN)



@bot.message_handler(commands=['start'])
def start(message):

    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! 👋\n\n"
        "Я умею:\n"
        "📦 Расписывать лоты\n"
        "🧮 Считать числа\n\n"
        "Пример росписи:\n"
        "41:3\n"
        "42:2\n\n"
        "Пример подсчёта:\n"
        "100 200 -50"
    )



@bot.message_handler(commands=['help'])
def help_command(message):

    bot.send_message(
        message.chat.id,
        "ℹ️ Помощь\n\n"
        "📦 Роспись лотов:\n"
        "41:3\n"
        "42:2\n"
        "15/1000:4\n\n"
        "Можно писать с пробелами:\n"
        "41 : 3\n\n"
        "🧮 Обычный подсчёт:\n"
        "100 200 -50"
    )



@bot.message_handler(
    func=lambda message:
    message.text and message.text.lower() == "привет"
)
def hello(message):

    bot.send_message(
        message.chat.id,
        f"Привет, {message.from_user.first_name}! 👋\n"
        "Отправь мне лоты или числа."
    )



@bot.message_handler(
    func=lambda message: True
)
def handle_message(message):

    text = message.text


    # Если есть двоеточие — проверяем лоты
    if ":" in text:

        result = calculate_chests(text)

        if result:

            bot.reply_to(
                message,
                result
            )

            return



    # Иначе считаем числа

    result = calculate_numbers(text)


    if result:

        bot.reply_to(
            message,
            result
        )

    else:

        bot.reply_to(
            message,
            "❌ Не смог найти данные для обработки."
        )



print("Бот запущен...")


bot.infinity_polling()
