# Игру разработал студент (Leonids Jofe) из школы SkillFactory, курс Full-stack python developer, класс FPW-104
from TOKEN import bot
from currency import Currency


########################################################################################################################

class APIException(Exception):
    pass


# ----------------------------------------------------------------------------------------------------------------------

# Валюты — это класс со списком валют.
class Currencies:
    currencies = ["RUB", "EUR", "USD"]


# ----------------------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=["start", "help"])
def helper(message) -> None:
    command_list = "<имя валюты, цену которой вы хотите узнать>\n" \
                   "<имя валюты, в которой надо узнать цену первой валюты>\n" \
                   "<количество первой валюты>\n" \
                   "\n" \
                   "ПОЖАЛУЙСТА ВВЕДИТЕ ДАННЫЕ В РЯД\n" \
                   "Например: EUR USD 5\n" \
                   "\n" \
                   "/value список доступных валют"
    bot.send_message(message.chat.id, command_list)


# ----------------------------------------------------------------------------------------------------------------------

@bot.message_handler(commands=["value"])
def list_of_currencies(message) -> None:
    """
    Он отправляет пользователю сообщение со списком всех доступных валют.

    :param message: объект сообщения
    """
    values = "↓ Информация о всех доступных валютах ↓\n" \
             "RUB\n" \
             "EUR\n" \
             "USD"
    bot.send_message(message.chat.id, values)


# ----------------------------------------------------------------------------------------------------------------------

@bot.message_handler(content_types=["text"])
def starter(message) -> None:
    try:
        text = message.text.upper().split(" ")
        if len(text) == 3:
            FROM, TO, AMOUNT = text
        else:
            raise APIException
    except APIException:
        bot.send_message(message.chat.id, "→ Ошибка в тексте ! ←")
    else:
        # Это проверка на валидность введенных валют.
        if text[0] in Currencies.currencies and text[1] in Currencies.currencies:
            formula = Currency.get_price(FROM, TO, int(AMOUNT))
            bot.send_message(message.chat.id, "{TO} {get:.2f}".format(TO=TO, get=formula))
        else:
            bot.send_message(message.chat.id, "→ Введена неправильная или несуществующая валюта ! ←")


# ----------------------------------------------------------------------------------------------------------------------

# Функция, которая используется для получения обновлений от Telegram.
bot.polling(non_stop=True)
