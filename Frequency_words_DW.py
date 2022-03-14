'''
Created on Dec 16, 2021

@author: Danxia Wang
'''
import string
import string
import nltk
from nltk.corpus import stopwords
import sqlite3
import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

conn = sqlite3.connect('BestBuyPrinters.db')
c=conn.cursor()

allreviews=pd.read_sql_query("select * from CustomerReviews",conn)
reviews=allreviews.loc[:, 'Reviews']

all_words=[]
for i in range(len(reviews)):
    review=str(reviews[i].lower())
    tokens = nltk.word_tokenize(review)
    all_words.extend(tokens)
    
freq_dic=nltk.FreqDist(all_words)

'''remove punctuations and stopwords'''
stopwords=list(set(stopwords.words('english')))
p = [',','.',"'",'"','?','!',";",'’',':']

for token in stopwords+p:
    if token in freq_dic: # Why adding this line?
        freq_dic.pop(token)
print(freq_dic.most_common(10))


'''       
wordcloud = WordCloud(width = 700, height = 700, background_color ='white', min_font_size = 10).generate(all_words) 

# plot the WordCloud image                        
plt.figure(figsize = (5, 5), facecolor = None) 
plt.imshow(wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0) 
  
plt.show()
'''

