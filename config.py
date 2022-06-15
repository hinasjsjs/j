import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "1913685619:AAE-y6Vim44l2fYTvyxMe0biI1f_yU8iuKA")
SUDO = int(os.environ.get("SUDO", "1571471419"))
HEROKU = os.environ.get("HEROKU", "darken15")
APP_URL = "https://"+ HEROKU +".herokuapp.com/" + BOT_TOKEN
