#!/usr/bin/env python
# coding: utf-8

# (This script scheduled via Crontab)

from td.client import TDClient

# Create a new session, credentials path is required.
TDSession = TDClient(
    client_id = 'J4QOQPWNPV2SN0ZUYGZ4SAWFZKFMPYNX', # my developer API key
    redirect_uri = 'https://localhost',             # set in API developer account
    credentials_path = 'td_state.json'              # save in cwd for now
)

# Login to the session
TDSession.login()

# ### 1. Query TD Ameritrade API

# create timestamp
import datetime as dt

now = str(dt.datetime.now()) #str or no?
print(now)

# Grab real-time stock quotes for 'NVDA' (Nvidia Corporation)

nvda_quotes = TDSession.get_quotes(instruments=['NVDA'])

# Grab real-time option quotes
nvda_quotes_options = TDSession.get_options_chain(option_chain={'symbol': 'NVDA'})
                                  #'callExpDateMap':'2021-12-10:1'} #yyyy-mm-dd:daystoexpiry

# insert timestamp field
nvda_quotes['timestamp'] = now
nvda_quotes_options['timestamp'] = now

# ### 2. Store JSON response in DB

from pymongo import MongoClient

# Instantiate client
client = MongoClient()

# Define working db
db = client.proj7db

# Define working collection
prices = db.prices

# Store the API response
# prices.insert_one(nvda_quotes)
prices.insert_one(nvda_quotes_options)

# Deletion (if needed)
# prices.remove({}) # nuclear option
# prices.remove({'symbol':'NVDA'}) 

# Confirm one record has been added
print(prices.count_documents({}))