
import telegram
TOKEN = '1602686596:AAGByzpMndN5gTZyPX-0Md5TNl21-pZ5pdc'
bot = telegram.Bot(token=TOKEN)
user_bot = bot.getMe()
print(user_bot.id)
print(user_bot.first_name)
print(type(user_bot))

