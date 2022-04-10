## Module #7 Project Proposal
### Mark Streer (DS/ML)

#### Question / Need:

Brokerage APIs often provide live price data on option chains - prices of call & put contracts at different strikes - along with prices of the underlying equity, quoted at the time of the query. While price history - e.g., the open/close/high/low/volume by day or other time period - is typically made available by brokerages in the case of stocks, the same is not true for their option chains. These data would be useful fodder for different machine learning models such as stock price prediction (regression), buy/sell decision criteria (classification), and deep learning models such as seq2seq and wave2vec.

#### Data Description:

Call and put premium prices for the stock, contract expiry date(s), and strike price(s) of interest will be queried live during market hours, at a frequency of once per minute. These data include:

* Bid/ask spread (mean) during period
* Trading volume during period
* Max/min price during period

For later modeling, these features can be used to derive additional ones (e.g. moving averages), and integrated with a granular price history of the underlying, such as available via Yahoo! Finance or [AlphaVantage](https://wwwl.alphavantage.co). Related (or seemingly unrelated) stocks' price histories could also be used as input.

#### Tools:

1. [TD Ameritrade Developer API]. Sample option-chain premium prices for stock of interest (e.g. NVDA) live during market days. Price data returned in JSON format.
2. MongoDB (pymongo) for data filtering and storage.

#### MVP Goal:
* Live pipeline that can sample the option chains for $NVDA for upcoming three months, once every five minutes.
* (Optimistic) Store the data acquired in a NoSQL database for efficient reference.