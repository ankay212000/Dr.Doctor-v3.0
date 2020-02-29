import urllib.request
from bs4 import BeautifulSoup as bs 
import re
import nltk
import heapq

def symdes(topic):
    try:
        url='https://en.wikipedia.org/wiki/'
        url=url+topic
        htmldoc = urllib.request.urlopen(url)
        soupObject = bs(htmldoc,'html.parser')
        paragraphContent = soupObject.findAll('p')
        allparaCon = " "
        for Content in paragraphContent:
            allparaCon=allparaCon+Content.text

        allparaCon_cleanedData = re.sub(r'\[[0-9]*\]',' ',allparaCon)
        allparaCon_cleanedData = re.sub(r'\s+',' ',allparaCon_cleanedData)
        sentences_tokens = nltk.sent_tokenize(allparaCon_cleanedData)
        #allparaCon_cleanedData

        '''allparaCon_cleanedData=re.sub(r'[^a-zA-Z]',' ',allparaCon_cleanedData)
        allparaCon_cleanedData=re.sub(r'\s+',' ',allparaCon_cleanedData)
        '''
        print(allparaCon_cleanedData.split(".")[0])
        print(allparaCon_cleanedData.split(".")[1])
    except:
        print("We don't have any information for this symptoms at this moment!!")    
    
    '''words_tokens = nltk.word_tokenize(allparaCon_cleanedData)
stopwords = nltk.corpus.stopwords.words('english')
word_frequencies = {}
for words in words_tokens:
    if words not in stopwords:
        if words not in word_frequencies:
            word_frequencies[words] = 1
        else:    
            word_frequencies[words] +=1

max_freq_word=max(word_frequencies.values())

for word in word_frequencies.keys():
    word_frequencies[word]=(word_frequencies[word]/max_freq_word)

sentences_scores = {}
for sentence in sentences_tokens:
    for word in nltk.word_tokenize(sentence.lower()):
        if word in word_frequencies.keys():
            if(len(sentence.split(' '))):
                sentences_scores[sentence] = word_frequencies[word]
            else:
                sentences_scores[sentence] += word_frequencies[word]'''               
      