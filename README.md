# More_Money_More_Problems (DRAFT)
---

I used Jefferson Henrique's [Get Old Tweets repository](https://github.com/edmundooo/GetOldTweets-python) to get all the Tweets by the current [members of the United States Congress with Twitter accounts](https://gwu-libraries.github.io/sfm-ui/posts/2017-05-23-congress-seed-list). I then used Pandas to explore and clean the Tweets. Next, I used Natural Languge Toolkit to preprocess the text of the Tweets and used [scikit-learn's Latent Dirichlet allocation](http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.LatentDirichletAllocation.html) to model their topics. Finally, I introduced [Campaign Finance information](https://www.opensecrets.org/api/admin/?function=user_api_use) for each member of Congress and analyzed how the amount PAC money they receive to finance their campaigns affects what they Tweet about.


---
### This repository includes:



* __01_Get_Congress_Tweets.py:__  (present tense verbs), (no period at end)

* __02_EDA.ipynb:__  (present tense verbs), (no period at end
