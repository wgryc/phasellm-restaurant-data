"""
Welcome to a PhaseLLM demo app where we build a spreadsheet of restaurant recommendations for you!

There are three parts to this process, separated into three separate files:
1. step1.py -- uses PhaseLLM's WebSearchAgent to get a list of URLs to crawl and crawls those URLs
2. step2.py -- use an LLM to extract and aggregate restaurant information
3. step3.py -- saves the outputs into an Excel file

This file is step1.py

Questions? Please reach out: w --at-- phaseai --dot-- com
"""

###
# The queries we want to run; this can work on any sort of restaurant
queries = [
    "best japanese restaurants in ginza part of tokyo",
    "ginza restaurants that only locals know",
    "tokyo ginza restaurants that are holes in the wall but AMAZING",
    "unique tokyo ginza restaurants",
    "tokyo ginza best food",
    "most unique tokyo (ginza) restaurants",
    "best tokyo ginza restaurants you can't miss",
]

###
# Your API keys and settings.

# OpenAI API Key; we use GPT-4 in this demo
openai_key = "YOUR OPENAI API KEY"

# Google API Key for using its web search components + a search ID
# Our search ID has a global web context; i.e., we simply use the base Google search offering
google_api_key = "YOUR GOOGLE API KEY"
search_id = "YOUR GOOGLE API SEARCH ID"

import json
from phasellm.agents import WebSearchAgent
from itertools import chain

# Instantiate the PhaseLLM WebSearchAgent
w = WebSearchAgent(api_key=google_api_key)

# We loop through each query and get the results from our web search. We store this in a bigger 'results' array.
results = []
for query in queries:
    print(query)
    results_new = w.search_google(
        query=query, custom_search_engine_id=search_id, num=10
    )
    results = list(chain(results, results_new))

# We save each title, URL, description, and content of the URL into a JSON file

results_dict = {"results": []}
for result in results:
    r = {
        "title": result.title,
        "url": result.url,
        "desc": result.description,
        "content": result.content,
    }
    results_dict["results"].append(r)

with open("search.json", "w") as writer:
    writer.write(json.dumps(results_dict))

print(f"Number of sites found and crawled: {len(results_dict['results'])}")
