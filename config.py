import os

BOT_TOKEN = os.environ.get("BOT_TOKEN", "5596614242:AAHN_Ob2lnFR_dh9jE8Z1uNIHGFv9UVNtx8")
SUDO = int(os.environ.get("SUDO", "1983379011"))
HEROKU = os.environ.get("HEROKU", "darken15")
APP_URL = "https://"+ HEROKU +".herokuapp.com/" + BOT_TOKEN
