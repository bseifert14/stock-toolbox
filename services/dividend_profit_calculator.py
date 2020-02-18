import requests
import json

def dividend_meta():
    response = requests.get("https://www.alphavantage.co/query?function=TIME_SERIES_MONTHLY_ADJUSTED&symbol=MSFT&apikey=V07NOD78ZP7V84V6&outputsize=full")

    # Data payload now set in the 'json_data' object. First half of the payload is 'Meta Data',
    # second half is 'Monthly Adjusted Time Series'.
    json_data = json.loads(response.text)

    # The portion of the data payload we want is the second half, 'Monthly Adjusted Time Series'
    for meta_data, adjusted_time_series in json_data.items():
        data = adjusted_time_series

    dates = ['2019-11-29', '2019-08-30', '2019-05-31', '2019-02-28', '2018-11-30', '2018-08-31',
             '2018-05-31', '2018-02-28', '2017-11-30']

    data_index = {'1. open': 'open'
                    , '2. high': 'high'
                    , '3. low': 'low'
                    , '4. close': 'close'
                    , '5. adjusted close': 'adjusted_close'
                    , '6. volume': 'volume'
                    , '7. dividend amount': 'dividend_amount'}

    stonk_data = []
    processed_stock_data = []

    for date, stock_data in json_data['Monthly Adjusted Time Series'].items():
        stock_data = dict((data_index[key], value) for (key, value) in stock_data.items())
        stock_data['date'] = date
        processed_stock_data.append(stock_data)

    return processed_stock_data
