# With reference to .png*, revealed this endpoint in network tab which shows the required data
# random is observed to be a random number, so it is not hardcoded and perhaps prevent dos attacks
# The endpoint is a GET request to the Shenzhen Stock Exchange API to retrieve historical stock data for a specific stock code.
# cycleType is determining frequency of capture, 32 is daily, 33 is weekly, 34 is monthly
# code is the stock code for which the data is being requested, in this case, '000001' which is the stock code for the Shenzhen Stock Exchange Index (SZSE Composite Index) required
# Example:
# api_url = 'https://www.szse.cn/api/market/ssjjhq/getHistoryData?random=0.6332035049957934&cycleType=34&marketId=1&code=000001&language=EN'
import random


def get_random_str():
    """
    Generates a random float as a string with 16 decimal places.

    Returns
    -------
    str
        A string representation of a random float between 0 and 1,
        formatted to 16 decimal places.
    """

    return f"{random.random():.16f}"


def get_stock_code():
    """
    Returns the stock code for the Shenzhen Stock Exchange Index (SZSE Composite Index)
    which is '000001' under the test context.

    Returns
    -------
    str
        The stock code as a string.
    """
    return "000001"


def get_api_urls():
    """
    Returns a list of URLs for the Shenzhen Stock Exchange API to retrieve historical
    data for the Shenzhen Stock Exchange Index (SZSE Composite Index) with different
    frequencies.

    The URLs are constructed by calling `get_random_str`, `get_stock_code`, and
    generating URLs for cycle types 34 (monthly), 33 (weekly), and 32 (daily).

    Returns
    -------
    list
        A list of URLs as strings. / list[str]
    """

    return [
        f"https://www.szse.cn/api/market/ssjjhq/getHistoryData?random={get_random_str()}&cycleType={cycleId}&marketId=1&code={get_stock_code()}&language=EN"
        for cycleId in ["34", "33", "32"]
    ]
