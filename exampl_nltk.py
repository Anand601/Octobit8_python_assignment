#!/usr/bin/env python
# coding: utf-8

# In[3]:

import nltk


# In[9]:


text="hi my name is Anand. I am from aurangabad . its a very beautiful place , in maharashtra"
from nltk.tokenize import sent_tokenize
sent_tokenize(text)


# In[10]:


sent_tokenize("बसंती इन कुत्तों के सामने मत नाचना. यह हाथ मुझे दे दे ठाकुर! रिश्ते तो हम तुम्हारे बाप लगते हैं, नाम है शहंशाह!")


# In[11]:


nltk.word_tokenize(text)


# In[7]:


import nltk


# In[13]:


from nltk.corpus import wordnet
nltk.download('wordnet')
  
syn=wordnet.synsets('love')
print(syn)


# In[14]:


syn[0].definition()


# In[15]:


syn[0].examples()


# In[16]:


from nltk.corpus import wordnet
antonyms=[]
for syn in wordnet.synsets('depressed'):
        for l in syn.lemmas():
                 if l.antonyms():
                          antonyms.append(l.antonyms()[0].name())
print(antonyms)


# In[18]:


from nltk.stem import PorterStemmer
word_stemmer = PorterStemmer()
word_stemmer.stem('believes')


# In[19]:


from nltk.stem import WordNetLemmatizer
lemmatizer=WordNetLemmatizer()
lemmatizer.lemmatize('believes')


# In[20]:


from nltk.corpus import stopwords
stopwords.words('english')


# In[21]:


from nltk.corpus import stopwords
text="Today is a great day. It is even better than yesterday. And yesterday was the best day ever!"
stopwords=set(stopwords.words('english'))
from nltk.tokenize import word_tokenize
words=word_tokenize(text)
wordsFiltered=[]
for w in words:
   
   if w not in stopwords:
       wordsFiltered.append(w)
                
wordsFiltered


# In[23]:


import nltk
nltk.download('averaged_perceptron_tagger')
from nltk.tokenize import PunktSentenceTokenizer
text='I am a human being, capable of doing terrible things'
sentences=nltk.sent_tokenize(text)
for sent in sentences:
    print(nltk.pos_tag(nltk.word_tokenize(sent)))
        


# In[ ]:




