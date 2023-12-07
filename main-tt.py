import requests
import pandas as pd
import json
import datetime
import os
import logging
import azure.functions as func




def main(mytimer: func.TimerRequest) -> None:
    utc_timestamp = datetime.datetime.utcnow().replace(
        tzinfo=datetime.timezone.utc).isoformat()

    api_key = os.environ["API_key"]

    url = "https://yahoo-finance127.p.rapidapi.com/historic/msft/1d/5d"

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "yahoo-finance127.p.rapidapi.com"
    }

    try:
        response = requests.get(url, headers=headers)
        response_json = response.json()
        logging.info("API Response: %s", response_json)

        if 'meta' in response_json:
         
            meta_data = response_json['meta']

            selected_keys = ['currency', 'symbol', 'exchangeName', 'exchangeTimezoneName', 'regularMarketPrice', 'chartPreviousClose']
            meta_data_selected = {key: [meta_data[key]] for key in selected_keys}
            
            df = pd.DataFrame(meta_data_selected)
            df.to_csv(utc_timestamp + '_meta_data.csv', index=False)
            logging.info("Meta data saved to 'meta_data.csv'")
           
         
            

    except Exception as e:
        logging.error("Error fetching or saving meta data: %s", e)

    if mytimer.past_due:
        logging.info('The timer is past due!')

    logging.info('Python timer trigger function ran at %s', utc_timestamp)