"""
Welcome to a PhaseLLM demo app where we build a spreadsheet of restaurant recommendations for you!

There are three parts to this process, separated into three separate files:
1. step1.py -- uses PhaseLLM's WebSearchAgent to get a list of URLs to crawl and crawls those URLs
2. step2.py -- use an LLM to extract and aggregate restaurant information
3. step3.py -- saves the outputs into an Excel file

This file is step3.py

Questions? Please reach out: w --at-- phaseai --dot-- com
"""

import json
import pandas as pd

# Load processed JSON file.
parsed = {}
with open("parsed.json", "r") as reader:
    parsed = json.loads(reader.read())

# Conver the JSON into a Pandas DataFrame and save it to an Excel file
df = pd.DataFrame.from_records(list(parsed.values()))
df.to_excel("restaurants-in-ginza.xlsx", sheet_name="Restaurants")
