from __future__ import print_function
import pandas as pd
import pickle 

# Import gensim for Latent Dirichlet Allocation
from gensim import corpora, models, similarities, matutils

# Logging for gensim (set to INFO)
import logging
(logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s',
                     level=logging.INFO))

from  sklearn.feature_extraction.text  import CountVectorizer

'''
Subject: Topics of Tweets of US Congress through the Lens of Campaign Finance
 
Date: 09/12/2018
 
Name: Edmund D. Chitwood

Summary:
The following Script:
- reads updated preprocessed Tweets into a Pandas DataFrame,
- vectorizes the word counts,
- performs LDA to derive topics from and assign topics to the Tweets, and
- stores topics and links to Tweets in a DataFrame and Pickles it.
'''

# Load Data
tweets = pd.read_pickle("updated_preprocessed_tweets.pkl")

# Create the document-term matrix with count vectorizer
cv = CountVectorizer()
matrix = cv.fit_transform(tweets.clean_text)
columns=cv.get_feature_names()
matrix = matrix.transpose()
corpus = matutils.Sparse2Corpus(matrix)

# Dict of unique words 
id2word = dict(zip(list(range(0, 423988)), columns))

# Create Latent Dirichlet Allocation (LDA) model (same as "fit" in sklearn)
lda = (models.LdaModel(corpus=corpus, num_topics=50, id2word=id2word,
                       passes=20,eval_every=None,))

# Preserve model for further analysis
lda.save('lda.model')

# Transform the docs from the word space to the topic space 
# (like "transform" in sklearn)
lda_corpus = lda[corpus]

# Store the documents' topic vectors in a list 
lda_docs = [doc for doc in lda_corpus]

# Create DF to hold topics for each Tweet
topics = []

for i in lda_docs:
    topics.append(dict(i))

topics_df = pd.DataFrame(topics)

# Combine topics DataFrame with links to actual Tweets
tweet_topics = pd.DataFrame()
tweet_topics['tweets'] = tweets.permalink
tweet_topics.reset_index(inplace=True)
tweets_links_topics = pd.concat([tweet_topics, topics_df], axis=1, sort=False)

# Preserve Tweets to topics mapping
tweets_links_topics.to_pickle('tweets_links_topics.pkl')