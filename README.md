# More Money, More Problems
---

<img width="1007" alt="screen shot 2018-10-01 at 3 43 05 pm" src="https://user-images.githubusercontent.com/25728710/46312190-59f62200-c592-11e8-9aaf-c65d65c72646.png">

---

## Summary:

The Python scripts and IPython notebooks in this repo collect, clean, preprocess and perform topic modeling on all Tweets of the current members of the US Congress. They also introduce campaign finance information for each member of Congress and investigate the relationship between the amount of PAC (Political Action Committee) members receive to finance their campaigns and what they Tweet about.

---

### Scripts and Notebooks:

* __01_get_congress_tweets.py:__ gets the Tweets of all the current members of the US Congress, and writes the Tweets and select Tweet metadata as CSV files

* __02_partial_data_eda.ipynb:__ reads in Senator Amy Klobuchar's Tweets performs EDA on on the them

* __03_tweets_to_pickle.ipynb:__ reads all Tweets from CSV files and then Pickles the data

* __04_full_data_clean_preprocess.ipynb:__ reads all Tweets from Pickle, performs EDA, cleans and preprocceses Tweets in preparation for topic modeling

* __05_congress_metadata.ipynb:__ - downloads metadata for each Congress member, and resolves discrepancies between the Twitter usernames listed in the Congress metadata and Tweet data

* __06_topic_modeling.py:__ reads preprocessed Tweets from Pickle, converts preprocessed Tweets to a matrix of token counts, and performs Latent Dirichlet Allocation to derive topics from and assign topics to the Tweets

* __07_Campaign_Finance_Data.ipynb:__ downloads campaign finance information for each relevant member of Congress

* __08_campaign_finance_eda_aggregate_pac.ipynb:__ performs EDA on aggreate camapaign finance data for current Congress, and aggregates PAC contribution totals for each relevant member of Congress

* __09_topic_pac_analysis.ipynb:__ shows the amount of PAC money received by Congress Members by state, party, etc., abbreviates topics for analysis, shows the top Tweet topics by Congress Members who received the most and least money from PACs to finance their most recent campaigns, and explores the high level differences between in PAC contributions depending on what Congress Members Tweet about

---
