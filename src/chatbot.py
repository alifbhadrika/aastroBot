import re
import itertools
import sys
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from datetime import datetime
from kmp import *

def clean_text(text):
    '''
    Melakukan stemming dan menghilangkan stopwords pada kalimat inputan
    '''
    stemmer = StemmerFactory().create_stemmer()
    stopword = StopWordRemoverFactory().create_stop_word_remover()
    text = stemmer.stem(stopword.remove(text))
    return text

def getSuitableResponses(text):
    if (isAddTask(text)):
        # TODO
        print("TODO")    
    elif (isShowTask(text)):
        # TODO
        print("TODO")
    elif (isShowDeadline(text)):
        # TODO
        print("TODO")
    elif (isUpdateTask(text)):
        # TODO
        print("TODO")
    elif (isRemoveTask(text)):
        # TODO
        print("TODO")
    elif (isHelp(text)):
        # Ini bagian help
        print("Bot ini bisa mencatat dan memberitahu deadline tugas")
    else:
        # Ini eror kalo gaada yang dikenalin
        response = "Maaf, saya tidak mengerti apa maksud anda. Coba tanyakan 'Apa yang bisa bot lakukan?' untuk melihat daftar perintah"
        print(response)
        return response

if __name__ == "__main__":
    print("Masukkan pesan: ", end = "")
    text = input()
    getSuitableResponses(text)