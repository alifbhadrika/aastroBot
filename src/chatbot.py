import re
import itertools
import sys
import utility as u
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from datetime import datetime


def clean_text(text):
    '''
    Melakukan stemming dan menghilangkan stopwords pada kalimat inputan
    '''
    stemmer = StemmerFactory().create_stemmer()
    stopword = StopWordRemoverFactory().create_stop_word_remover()
    text = stemmer.stem(stopword.remove(text))
    return text

def getSuitableResponses(text):
    ret = u.inspectQuery(text)
    if (ret == 1):
        print("1")
    elif (ret == 2):
        print("2")
    elif (ret == 3):
        print("3")
    elif (ret == 4):
        print("4")
    elif (ret == 5):
        print("5")        
    elif (ret == 6):
        print("6")
    elif (ret == 7):
        print("7")        
    else:
        print("-1")        

if __name__ == "__main__":
    print("Masukkan pesan: ", end = "")
    text = input()
    getSuitableResponses(text)