import requests

from get_url import get_api_urls


def test_verify_response_picupdata():
    """
    Test to verify the logic of the highs and lows in the API response data.

    This test checks that the high value is greater than or equal to the low value
    for each data point in the API response.

    Args:
        None

    Returns:
        None

    Raises:
        AssertionError: If the high value is less than the low value for any data point.
    """

    for url in get_api_urls():  # for each time interval (daily, weekly, monthly)
        response = requests.get(url)  # make a GET request to the API endpoint
        print(f"{url=}")  # print the URL being tested
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"  # check if the response status code is 200 OK
        print(f"{response.status_code=}")

        # Response integrity checks - response is not empty, critical keys exist and have valid values

        assert response.json() is not None, "Response JSON is None"
        assert (
            "message" in response.json()
        ), "Response JSON does not contain 'message' key"

        assert (
            response.json()["message"] == "成功"
        ), f"Response JSON 'message' is not '成功', is {response.json()['message']} instead"
        assert "data" in response.json(), "Response JSON does not contain 'data' key"
        assert response.json()["data"] is not None, "Response JSON 'data' is None"
        assert (
            response.json()["data"]["code"] == "000001"
        ), f"Response JSON 'data' code is not '000001', is {response.json()['data']['code']} instead"

        # the picupdata stores interested data, have the following structure for each interval (day/week/month)
        picupdata_keys = [
            "date",
            "open",
            "close",
            "low",
            "high",
            "chg",
            "percent_chg",
            "vol",
            "amt",
        ]
        # Check the high lows are making sense
        for day_stock_data in response.json()["data"]["picupdata"]:
            data = dict(
                zip(
                    picupdata_keys,
                    day_stock_data,
                )
            )  # creating a data dictionary for further usage if test of other values are needed
            
            # debug print the data dictionary
            print(f"{data=}")
                
            # Check if the high price is greater than or equal to the low price
            assert float(data["high"]) >= float(
                data["low"]
            ), f"High price {data['high']} is less than low price {data['low']} on date {data['date']}"

    print("[PASS] All tests for verify_high_low passed successfully!")
