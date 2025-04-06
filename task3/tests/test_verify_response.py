import requests

from get_url import get_api_urls


def test_verify_response_status_code():
    """
    Test to verify the status code of the API response.

    This test sends a GET request to the SZSE API endpoint for each cycle type (daily, weekly, monthly)
    and verifies that the response status code is 200 OK.

    Raises:
        AssertionError: If the response status code is not 200 OK for any cycle type.
    """
    for url in get_api_urls():
        response = requests.get(url)
        print(f"{url=}")
        print(f"{response.status_code=}")
        assert (
            response.status_code == 200
        ), f"Expected status code 200, but got {response.status_code}"
        print("[PASS] All 200.")
