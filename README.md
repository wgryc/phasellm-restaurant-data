# Tutorial: Structured Data from PhaseLLM Web Search Agents and LLMs

Code related to the PhaseLLM tutorial outlining how to extract structured data using Web Search Agents and LLMs.

You need API access to OpenAI and Google's [Custom Search API](https://developers.google.com/custom-search/v1/overview).

After that, simply run...
- `python step1.py` to search the web and crawl the search results
- `python step2.py` to extract data about restaurants from the above
- `python step3.py` to conver the results into an Excel file

Note that this requires [PhaseLLM](https://phasellm.com/) version 0.0.14 or later.
