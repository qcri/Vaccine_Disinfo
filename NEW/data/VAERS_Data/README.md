# VAERS Dataset

No of total urls extracted from the Twitter dataset: 240,475

No of unique urls: 60,181

url_list.json => JSON file containing all the urls extracted from the Twitter dataset

unique_urls.csv => CSV file containing all the unique urls

unique_urls_with_netloc => CSV file containing all the unique urls with domains

## Filtered dataset for AstraZeneca keywords

All the data is stored in `/NEW/data/VAERS_Data/URLs for AstraZeneca Keywords/`.

```python
compiled_dictionary = re.compile(r"(?i)(AstraZeneca|Astra Zeneca|AZD1222|COVID|vaccine|immunity|herd immunity|Barrington|focused protection)" , flags=re.IGNORECASE)
```

No of total urls extracted from the filtered Twitter dataset: 77566

No of unique urls: 26,337

No of unique domains: 2103