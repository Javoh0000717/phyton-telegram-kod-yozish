Python 3.11.2 (tags/v3.11.2:878ead1, Feb  7 2023, 16:38:35) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import telegram
... from telegram.ext import Updater, CommandHandler
... import random
... 
... def start(update, context):
...     context.bot.send_message(chat_id=update.effective_chat.id, text="Salom, Kopgina aholidan surovnoma utqazish botiga xush kelibsiz!")
...     
... def surovnoma(update, context):
...     # surovnoma nomlari
...     surovnoma_nomlari = ['Sudoku', 'Kubik Rubik', 'Pazl', 'Monopoliya', 'Shaxmat', 'Doma']
...     # surovnoma tanlash
...     surovnoma_tanlov = random.choice(surovnoma_nomlari)
...     # javobni jo'natish
...     context.bot.send_message(chat_id=update.effective_chat.id, text="Kopgina aholidan surovnoma utqazish uchun "+surovnoma_tanlov+" ni tavsiya qilamiz!")
... 
... def main():
...     # Telegram bot kaliti
...     TOKEN = 'botning API kaliti'
...     # updater yaratish
...     updater = Updater(TOKEN, use_context=True)
...     # dispatcher yaratish
...     dispatcher = updater.dispatcher
...     # Start komandasi
...     start_handler = CommandHandler('start', start)
...     dispatcher.add_handler(start_handler)
...     # Surovnoma komandasi
...     surovnoma_handler = CommandHandler('surovnoma', surovnoma)
...     dispatcher.add_handler(surovnoma_handler)
...     # botni ishga tushirish
...     updater.start_polling()
...     updater.idle()
... 
... if __name__ == '__main__':
...     main()
