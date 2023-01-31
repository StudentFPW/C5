import requests


def get_cost(FROM: str, TO: str):
    """
    Он принимает два аргумента: первый — это валюта, из которой вы хотите конвертировать,
    а вторая — валюта, в которую вы хотите конвертировать.

    :param FROM: Валюта, которую вы хотите конвертировать.
    :type FROM: str.

    :param TO: Валюта, в которую вы хотите конвертировать.
    :type TO: str.

    :return: Объект JSON.
    """
    ANY = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={FROM}&tsyms={TO}")
    return ANY.content
