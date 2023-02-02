import requests
import json


# Этот класс представляет собой статический метод, который принимает базовую валюту, валюту котировки и сумму базовой
# валюты и возвращает сумму валюты котировки.
class Currency:
    @staticmethod
    def get_price(base: str, quote: str, amount: int) -> int:
        """
        > Он принимает базовую валюту, валюту котировки и сумму базовой валюты и возвращает сумму валюты котировки.

        :param base: Базовая валюта, которую вы хотите конвертировать.
        :type base: str
        :param quote: Валюта, в которую вы хотите конвертировать.
        :type quote: str
        :param amount: Сумма базовой валюты, которую вы хотите конвертировать.
        :type amount: int
        :return: Сумма котируемой валюты, эквивалентная базовой валюте.
        """
        ANY = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={base}&tsyms={quote}")
        return amount * json.loads(ANY.content)[quote]
