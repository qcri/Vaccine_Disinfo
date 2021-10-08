# VAERS-Twitter Dataset

Total Tweets in the original dataset: 727,148

Total Tweets where AstraZeneca mentioned: 296,969 (40.84%)



Total Tweets with URLs in the dataset: 198,046

Total URLs extracted from the all Tweets: 240,475

Total unique URLs extracted from all Tweets: 60,181

Total unique URLs extracted after expanding: 59,651

Total unique URLs after filtering Twitter domain URLs: 16,351

Total Tweets with URLs where AstraZeneca mentioned: 63,236 (31.93%)

Total URLs extracted from Tweets where AZ mentioned: 77,556 (32.25%)

Total unique URLs extracted from Tweets where AZ mentioned: 26,337 (43.76%)

Total unique URLs extracted from Tweets where AZ mentioned (after expanding): 25,962 (43.52%)

Total unique URLs extracted from Tweets where AZ mentioned after filtering Twitter domain URLs: 8,742 (53.46%)



### Feature Vector for URLs

| expanded_url                         | text | created_at | author_id | twtid |
|--------------------------------------|------|------------|-----------|-------|
| https://www.openvaers.com/covid-data | 1362 | 1516       | 681       | 1516  |


text: no of unique tweeted texts included the url

created_at: no of unique timestamps associated with tweets included the url

author_id: no of unique authors tweeted the url

twtid: no of unique tweets included the url


### Feature Vector for Domains

| resolved_domain                      | text | created_at | author_id | twtid |
|--------------------------------------|------|------------|-----------|-------|
| childrenshealthdefense.org           | 7562 | 9258       | 4172      | 9274  |


text: no of unique tweeted texts included the domain

created_at: no of unique timestamps associated with tweets included the domain

author_id: no of unique authors tweeted the domain

twtid: no of unique tweets included the domain