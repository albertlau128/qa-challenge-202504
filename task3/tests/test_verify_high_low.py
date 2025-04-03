import requests

from get_url import get_api_urls


def test_verify_response_picupdata():
    print()
    """Test to verify the status code of the API response."""
    for url in get_api_urls():
        response = requests.get(url)
        print(f'{url=}')
        # print(f'{response.status_code=}')
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        # print(response.json())
        assert response.json() is not None, "Response JSON is None"
        assert 'message' in response.json(), "Response JSON does not contain 'message' key"
        assert response.json()['message'] == '成功'
        assert 'data' in response.json(), "Response JSON does not contain 'data' key"
        assert response.json()['data'] is not None, "Response JSON 'data' is None"
        assert response.json()['data']['code'] == '000001', "Response JSON 'data' code is not '000001'"
        for day_stock_data in response.json()['data']['picupdata']:
            data = dict(zip(['date', 'open', 'close', 'low', 'high', 'chg', 'percent_chg', 'vol', 'amt'], day_stock_data))
            assert float(data['high']) - float(data['low']) >= 0, f"High price {data['high']} is less than low price {data['low']} on date {data['date']}"
    print("[PASS]All tests for verify_high_low passed successfully!")