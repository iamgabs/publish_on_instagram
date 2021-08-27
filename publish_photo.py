#######################################
#                                     #
#  Publish on Instagram with python   #
#    Powered by Garbriel Carvalho     #
#                                     #
#######################################

#IMPORT MODULE
from instabot import Bot

bot = Bot()

#LOGIN
bot.login(username="Your username", password="Your password")

#Captions
captions = "PUT YOUR CAPTIONS HERE!"

#PUBLISH
bot.upload_photo("YOUR PHOTO HERE", caption= captions)
