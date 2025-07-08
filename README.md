# Azure Function: Yahoo Finance Meta Data Fetcher

This is a Python-based Azure Timer Trigger Function that fetches historical meta data from the Yahoo Finance API via RapidAPI. It is designed to run on a schedule, pull stock data for MSFT, and save selected metadata fields into a timestamped CSV file.

## What It Does

- Runs on a schedule using a timer trigger.
- Makes an authenticated HTTP request to the Yahoo Finance API on RapidAPI.
- Extracts selected metadata fields from the API response.
- Writes the data to a CSV file using the current UTC timestamp in the filename.
- Logs process details using the standard Python logging module.

## Output Example

```csv
currency,symbol,exchangeName,exchangeTimezoneName,regularMarketPrice,chartPreviousClose
USD,MSFT,NasdaqGS,America/New_York,340.54,339.99
```
## Requirements

-   Python 3.9+
    
-   Azure Functions Core Tools
    
-   A RapidAPI account with access to the Yahoo Finance API
    
-   Set the environment variable `API_key` with your RapidAPI key

## Getting Started

### Clone the Repository

bash

CopyEdit

`git clone https://github.com/yourusername/yahoo-finance-timer-trigger.git cd yahoo-finance-timer-trigger`


### Install Dependencies

If you're running the function locally:

bash

CopyEdit

`pip install -r requirements.txt`

### Set Environment Variable

Set your RapidAPI key as an environment variable:

#### Linux/macOS:

bash

CopyEdit

`export API_key="your-rapidapi-key"`

#### Windows CMD:

cmd

CopyEdit

`set API_key=your-rapidapi-key`


### Run the Function Locally

bash

CopyEdit

`func start`


### Deploy to Azure

bash

CopyEdit

`func azure functionapp publish <YourFunctionAppName>`

## Timer Configuration

The timer schedule is defined in `function.json` using CRON expressions.

### Example (runs every 5 minutes):
{
  "schedule": "0 */5 * * * *"
}
For more on CRON expressions, refer to the Azure Functions timer trigger documentation.

## Metadata Fields Extracted

-   currency
    
-   symbol
    
-   exchangeName
    
-   exchangeTimezoneName
    
-   regularMarketPrice
    
-   chartPreviousClose
    

## Technologies Used

-   Azure Functions (Timer Trigger)
    
-   Python 3.9+
    
-   Requests (HTTP library)
    
-   Pandas (DataFrame manipulation and CSV export)
    
-   RapidAPI (Yahoo Finance API)


## Notes

The API URL is currently hardcoded to fetch data for MSFT:

bash

CopyEdit

`https://yahoo-finance127.p.rapidapi.com/historic/msft/1d/5d` 

You can change `msft` to any other ticker symbol in the URL to fetch different stock data.


## Error Handling

-   All request and file writing operations are wrapped in a `try-except` block.
    
-   Exceptions are logged using `logging.error`.
    
-   Timer overdue status is logged using `mytimer.past_due`.

## Authors

**Zaynab Ahmed Khan**  
Contact: zaynabkhan982@gmail.com

## License
This project is open-source and available under the MIT License.
