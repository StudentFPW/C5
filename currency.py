import requests
import json


class Currency:
    @staticmethod
    def get_price(FROM: str, TO: str, AMOUNT: int) -> int:
        """
        Он принимает валюту для конвертации, валюту для конвертации и сумму в первой валюте и возвращает сумму во второй
        валюте.

        :param FROM: Валюта, которую вы хотите конвертировать.
        :type FROM: str
        :param TO: Валюта, в которую вы хотите конвертировать.
        :type TO: str
        :param AMOUNT: Сумма валюты, которую вы хотите конвертировать.
        :type AMOUNT: int
        :return: Цена валюты в валюте, которую вы хотите.
        """
        ANY = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={FROM}&tsyms={TO}")
        return AMOUNT * json.loads(ANY.content)[TO]
