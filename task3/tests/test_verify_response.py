import requests

from get_url import get_api_urls

def test_verify_response_status_code():
    """Test to verify the status code of the API response."""
    for url in get_api_urls():
        response = requests.get(url)
        print(f'{url=}')
        print(f'{response.status_code=}')
        assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
        print('[PASS] All 200.')