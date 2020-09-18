<img width="829" alt="screen shot 2018-11-01 at 11 49 15 am" src="https://user-images.githubusercontent.com/25728710/47862763-44ac2780-ddcc-11e8-8805-e6f514f08069.png">

---

### Summary:

The Python scripts and IPython notebooks in this repo collect, clean, preprocess and perform topic modeling on all Tweets of the current members of the US Congress. They also introduce campaign finance information for each member of Congress and investigate the relationship between the amount of PAC (Political Action Committee) members receive to finance their campaigns and what they Tweet about. In addition, [this map](https://datawrapper.dwcdn.net/h4cuM/4/) shows the amount of money PACs contributed to the campaigns of incumbent members of the U.S. House of Representatives in 2018.

---

<img width="1007" alt="screen shot 2018-10-01 at 3 43 05 pm" src="https://user-images.githubusercontent.com/25728710/46312190-59f62200-c592-11e8-9aaf-c65d65c72646.png">

---

### This repository includes:

1. __get_congress_tweets.py:__ gets the Tweets of all the current members of the US Congress, and writes the Tweets and select Tweet metadata as CSV files

2. __partial_data_eda.ipynb:__ reads in Senator Amy Klobuchar's Tweets performs EDA on the them

3. __tweets_to_pickle.ipynb:__ reads all Tweets from CSV files and then pickles the data

4. __full_data_clean_preprocess.ipynb:__ reads all Tweets from pickled file, performs EDA, cleans and preprocesses the Tweets in preparation for topic modeling

5. __congress_metadata.ipynb:__ downloads metadata for each Congress member, and resolves discrepancies between the Twitter usernames listed in the Congress metadata and those listed alongside the Tweet data

6. __topic_modeling.py:__ reads preprocessed Tweets from pickled file, converts preprocessed Tweets to a matrix of token counts, and performs Latent Dirichlet Allocation to derive topics from and assign topics to the Tweets

7. __campaign_finance_data.ipynb:__ downloads campaign finance information for each relevant member of Congress

8. __campaign_finance_eda_aggregate_pac.ipynb:__ performs EDA on aggregate campaign finance data for current Congress members, and aggregates PAC contribution totals for each relevant member of Congress

9. __topic_pac_analysis.ipynb:__ shows the amount of PAC money received by Congress Members by state, party, etc., abbreviates topics for analysis, shows the top Tweet topics by Congress Members who received the most and least money from PACs to finance their most recent campaigns, and explores the high level differences between in PAC contributions depending on what Congress Members Tweet about

* __Map.md:__ shows the amount of money PACs contributed to the campaigns of incumbent members of the U.S. House of Representatives in 2018

* __Presentation.pdf:__ presentation of process and results

---
