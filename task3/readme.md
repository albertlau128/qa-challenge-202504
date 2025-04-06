# Task 3: Automated Testing for SZSE API Endpoint

## Overview

This task involves automated testing for the SZSE (Shenzhen Stock Exchange) API endpoint, specifically for the stock code `000001`. The goal is to verify the integrity of the API response and ensure that it returns the expected data.

## Initial Identification of API Endpoint

The API endpoint was identified by analyzing the network traffic in the developer tools of the SZSE Market Data website. The endpoint is:

```http
https://www.szse.cn/api/market/ssjjhq/getHistoryData?random=<random>&cycleType=<cycleType>&marketId=1&code=<code>&language=EN"
```

### API Endpoint Parameters
- `random`: a random float between 0 and 1 (exclusive)
- `cycleType`: the time slicing method (32: daily, 33: weekly, 34: monthly)
- `marketId`: the market ID (always 1)
- `code`: the stock code (in this case, 000001)
- `language`: the language of the response (always EN)


> Attempted to make a simple request to the above endpoint without any specific header using   `requests` libarary, already returning good results (200, no authentication)

## Testing Overview
Tests are stored in the `tests` subfolder, ready for `pytest` usage


`test_verify_response.py`
- Verify the API returns 200 for each daily, weekly and monthly configurations

`test_verify_high_low.py`
- Checks integrity of API response (including checking returning 200)
- Checks if the overall critical structure of results are correct and key-values exist
- Check if highs and lows are logical 
    - float comparison, extra care taken on `str->float` conversion and floats comparison

## To Run Tests

1. Go into the `./task3` directory.
2. Initialize the poetry environment by running `poetry init`.
3. Install the dependencies by running `poetry install`.
4. Activate the poetry shell by running `poetry env activate`.
5. Run the tests using `pytest ./tests/` for all tests
6. Review the results and investigate any failed test cases.