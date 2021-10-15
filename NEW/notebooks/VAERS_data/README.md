# VAERS-Twitter Dataset

Total Tweets in the original dataset: 727,148

Total Tweets with URLs in the dataset: 198,046

#### After filtering for Twitter domain

Unique Tweets: 143,402

Unique URLs: 15,465

Unique domains: 2980

#### All URLs dataset

all_urls.csv - This dataset contains all the unique URLs (without Twitter domain) [md5sum: 6f7b1e2b67697737ad1044af584c14ad]

expanded_urls.csv - This dataset contains all the unique URLs after expanding [md5sum: 4ee5f5a2bc76482a948478ad0f0484f1]



### Feature Vector for URLs

|                url                | nodeID | nodeLang | nodeText | nodeTime | nodeUserID | parentID | parentUserID | nodeDate | has_az_keywords | no_az_keywords |
|:---------------------------------:|:------:|:--------:|:--------:|----------|------------|----------|--------------|----------|-----------------|----------------|
| https://wonder.cdc.gov/vaers.html |  4980  |    27    |   2155   | 4960     | 3851       | 2093     | 1639         | 211      | True            | True           |


nodeText: no of unique tweeted texts included the url

nodeTime: no of unique timestamps associated with tweets included the url

nodeUserID: no of unique authors tweeted the url

nodeID: no of unique tweets included the url


