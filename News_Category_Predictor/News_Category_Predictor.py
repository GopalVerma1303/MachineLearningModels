# %%
from sklearn.metrics import confusion_matrix
from sklearn.pipeline import make_pipeline
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.datasets import fetch_20newsgroups
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
data = fetch_20newsgroups()
categories = data.target_names

# %%
train = fetch_20newsgroups(subset='train', categories=categories)
test = fetch_20newsgroups(subset='test', categories=categories)
print(test.data[5])

# %%
print(train.data[1])

# %%

# %%
model = make_pipeline(TfidfVectorizer(), MultinomialNB())
model.fit(train.data, train.target)
labels = model.predict(test.data)
# %%
print(labels)
# %%
mat = confusion_matrix(test.target, labels)
# %%
sns.heatmap(
    mat.T,
    annot=True,
    fmt='d',
    cbar=False,
    xticklabels=train.target_names,
    yticklabels=train.target_names,
)
plt.xlabel('true label')
plt.ylabel('predicted label')
# %%
def predict_category(s, test=test, model=model):
    pred = model.predict([s])
    return train.target_names[pred[0]]
# %%
predict_category("")
# %%
