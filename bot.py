from telegram.ext import Updater, CommandHandler, MessageHandler
import logging

# Bot token
TOKEN = '6702478052:AAGkzLB5TGio-P4rifzHc7wElOoHcyzbQkc'

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

# Kino ma'lumotlarini oladigan funksiya
def get_movie_info(movie_number):
    # Bu yerda kinolar haqida ma'lumot saqlang. Misol uchun, dictionaryda.
    movies = {
        '1': 'Kino 1: Tavsif...',
        '2': 'Kino 2: Tavsif...',
        '3': 'Kino 3: Tavsif...',
        # Qo'shimcha kinolarni qo'shing
    }
    return movies.get(movie_number, 'Kechirasiz, bu raqam bo‘yicha kino topilmadi.')

# /start komandasi uchun handler
def start(update, context):
    update.message.reply_text('Salom! Kino haqida ma\'lumot olish uchun raqam kiriting.')

# Raqam qabul qiluvchi funksiya
def handle_message(update, context):
    movie_number = update.message.text
    movie_info = get_movie_info(movie_number)
    update.message.reply_text(movie_info)

# Xatoliklarni log qilish
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)

def main():
    updater = Updater(TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(None, handle_message))  # Bu yerda Filters.text o'rniga None ishlatilgan

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

if __name__ == 'main':
    main()