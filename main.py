
import telegram
TOKEN = '1602686596:AAGByzpMndN5gTZyPX-0Md5TNl21-pZ5pdc'

bot = telegram.Bot(token=TOKEN)


print(bot.get_webhook_info())
print(bot.set_webhook(url='https://motof.pythonanywhere.com/'))


    # dispatcher = Dispatcher(bot,None,workers=0)

    # update = telegram.Update.de_json(request.get_json(force=True), bot)
    # dispatcher.add_handler(MessageHandler(Filters.text, hi))

    # dispatcher.process_update(update)