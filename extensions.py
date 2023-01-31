import json
from TOKEN import bot
from currency import get_cost


########################################################################################################################

@bot.message_handler(commands=["help"])
def helper(message):
    command_list = "/value список доступных валют"
    bot.send_message(message.chat.id, command_list)


# ----------------------------------------------------------------------------------------------------------------------

@bot.message_handler(content_types=["text"])
def starter(message):
    FROM, TO, AMOUNT = message.text.upper().split(" ")
    bot.send_message(message.chat.id, "{get:.2f}".format(get=(int(AMOUNT) * (json.loads(get_cost(FROM, TO))[TO]))))


# ----------------------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=["value"])
def list_of_currencies(message):
    values = "RUB\n" \
             "EUR\n" \
             "USD"
    bot.send_message(message.chat.id, values)


# ----------------------------------------------------------------------------------------------------------------------

# Функция, которая используется для получения обновлений от Telegram.
bot.polling(non_stop=True)
