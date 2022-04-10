#!/usr/bin/env python
# coding: utf-8

# (This script scheduled via Crontab)

# need to convert this notebook to "*.py" once it is finalized
# !nbconvert?


# ### 1. Query TD Ameritrade API

# create timestamp
import datetime as dt

now = str(dt.datetime.now()) #str or no?
print(now)

# Grab real-time stock quotes for 'NVDA' (Nvidia Corporation)

nvda_quotes = TDSession.get_quotes(instruments=['NVDA'])

# Grab real-time quotes for 'AMZN' (Amazon) and 'SQ' (Square)
# multiple_quotes = TDSession.get_quotes(instruments=['AMZN','SQ'])

# Grab real-time option quotes
nvda_quotes_options = TDSession.get_options_chain(option_chain={'symbol': 'NVDA'}
                                                               #'callExpDateMap':'2021-12-10:1'} #yyyy-mm-dd:daystoexpiry
                                           ) 

# insert timestamp field
nvda_quotes['timestamp'] = now
nvda_quotes_options['timestamp'] = now

# ### 2. Store JSON response in DB

from pymongo import MongoClient
# created 'proj7db' in mongo shell somehow
# https://www.mongodb.com/basics/create-database

# Instantiate client; confirm 'proj7db' among available databases
client = MongoClient()
client.database_names()


# Loop for storage; to be run every min 0900-1700 EST (8 hrs * 60 min = 480 documents per day)

# Define working db
db = client.proj7db

# Define working collection
prices = db.prices

# Store the API response
prices.insert_one(nvda_quotes)
prices.insert_one(nvda_quotes_options)

# Deletion (if needed)
# prices.remove({'symbol':'NVDA'}) # nuclear option

# Confirm one record has been added
print(prices.count_documents({}))