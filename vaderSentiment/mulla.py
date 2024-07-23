import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

import nltk
nltk.download('punkt')

#Read in data

df = pd.read_csv("reviews.csv")
ax = df['rating'].value_counts().sort_index().plot(kind = 'bar', title = 'Count of Reviews by Stars', figsize = (10,5))
ax.set_xlabel('Stars Rating')

example = df['text'][50]
print(example)
# tokens = nltk.word_tokenize(example)
# print(tokens[:10])

plt.show()
