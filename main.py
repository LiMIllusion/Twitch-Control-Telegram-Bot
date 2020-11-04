import telegram
from telegram.ext import Updater, CommandHandler, Filters, MessageHandler
import logging
import json 

'''

{
    "token" : "", 
    "admin" : [],
    "client_id" : ""
}

'''
def start(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Ciao")

def echo(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = update.message.text)

def idRequest(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = update.effective_chat.id)

def contactAdmin(update, context):
    context.bot.send_message(chat_id = admins[0], text = update.message.text)

f = open("configuration.json", "r")

ids = json.loads(f.read())

bot_token = ids['token']
admin = ids['admins']
bot = telegram.Bot(token = bot_token)

print(bot.get_me())

updater = Updater(token = bot_token, use_context = True)

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
echo_hander = MessageHandler(Filters.text & (~Filters.command), echo)
id_request = CommandHandler('id', idRequest)
contact_admin = CommandHandler("cd", contactAdmin) 
dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_hander)
dispatcher.add_handler(id_request)
dispatcher.add_handler(contact_admin)
updater.start_polling()

