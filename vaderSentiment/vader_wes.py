from nltk.sentiment.vader import SentimentIntensityAnalyzer
from tqdm import tqdm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

# Create an instance of the Vader sentiment analyzer
wes = SentimentIntensityAnalyzer()

pName = input("Product Name: ")
df = pd.read_csv("reviews.csv")

# Run the polarity score on the entire dataset
res = {}

for i, row in tqdm(df.iterrows(), total = len(df)):
    text = row['text']
    myid = row['id']
    res[myid] = wes.polarity_scores(text)

# print(res)

vaders = pd.DataFrame(res).T
vaders = vaders.reset_index().rename(columns = {'index' : 'id'})
vaders = vaders.merge(df, how = 'left')

print(vaders)
vaders.head()

#plot holistic VADER results
graph = sns.barplot(data = vaders, x = 'rating', y = 'compound')
graph.set_title(pName + ' - Amazon Reviews Sentiment Analysis')

#plot VADER subplot results
fig, gs = plt.subplots(1, 3, figsize = (12, 3))
sns.barplot(data = vaders, x = 'rating', y = 'neg', ax = gs[0])
sns.barplot(data = vaders, x = 'rating', y = 'neu', ax = gs[1])
sns.barplot(data = vaders, x = 'rating', y = 'pos', ax = gs[2])

gs[0].set_title('Negative')
gs[1].set_title('Neutral')
gs[2].set_title('Positive')

plt.tight_layout()
plt.show()

# print(vaders)


# score = wes.polarity_scores("RedPeak is the best company ever!")
# print(score)