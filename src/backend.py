import re
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from datetime import datetime
import sys
stemmer = StemmerFactory().create_stemmer()
stopword = StopWordRemoverFactory().create_stop_word_remover()

keywords = {'tubes','quiz','tucil','tubes','pr'}
months_synonym = {'agu' : 'aug', 'mei' : 'may', 'des' : 'dec', 'okt' : 'oct'}


kalimat = 'Halo bot, tolong ingetin aku 3 hari ya ada pada 14-10-2012 sampai 13 oktober 2021 tubes if2211 bab 2 sampai 3 cacatt loo'

date1pattern = r'(\d{2})[/-](\d{2})[/-](\d{4})'
date2pattern = r'(\b\d{1,2}\D{0,3})?\b(?:[jJ]an(?:uari)?|[fF]eb(?:ruari)?|[mA]ar(?:et)?|[aA]pr(?:il)?|[mM]ei|[jJ]un(?:i)?|[jJ]ul(?:i)?|[aA]ug(?:ust)?|[aA]gustus?|[sS]ep(?:tember)?|[oO][ck]t(?:ober)?|([nN]ov|[dD]e[cs])(?:ember)?)\D?(\d{1,2}\D?)?\D?((19[7-9]\d|20\d{2})|\d{2})'
kodepattern = r'([kK][uU]|[iI][fF])(\d{2})(\d{2})'
timeperiodpattern = r'\b[0-9]+?\b\s([hH]ari|[mM]inggu)'


def timeperiod(S):
    time = re.search(timeperiodpattern,S)
    if time:
        return time.group()
    

print(timeperiod(kalimat))

def findalldate(S):
    date = []
    date1 = re.search(date1pattern,S)
    date2 = re.search(date2pattern,S)
    date.append(str(date1.group()))
    date.append(str(date2.group()))
    return date

print(findalldate(kalimat))

def date(S):
    date = re.search(date1pattern,S)
    if not date:
        date = re.search(date2pattern,S)
        if (not date):
            return
        datelist = date.group().split(' ')
        datelist[1] = datelist[1][0:3]
        month = datelist[1]
        if month.lower() in months_synonym.keys():
            datelist[1] = months_synonym[month.lower()]
        date = " ".join(datelist)
        dt = datetime.strptime(date, '%d %b %Y')
        return dt
    date = date.group()
    if ('-' in date):
        date = '/'.join(date.split('-'))
    dt = datetime.strptime(date, '%d/%m/%Y')
    return dt

print(date(kalimat).date())

def matkul(S):
    kode = re.search(kodepattern,S)
    if (kode):
        return kode.group().upper()
    return

print(matkul(kalimat))

def spek(S):
    kode = re.search(kodepattern,S)
    if (kode):
        return S.partition(kode.group()+str(' '))[2]

print(spek(kalimat))

# def toRegex(S):
#     S = stemmer.stem(stopword.remove(S))
#     S = S.replace(' ','.*')
#     S = '.*'+ S + '.*'
#     match = re.search(S, db)
#     k = re.search(r'(\d{2})[/.-](\d{2})[/.-](\d{4})',kalimat)
#     d = datetime.datetime.strptime(k.group(), '%d/%m/%Y')
#     print(d.date())
#     # if (match):
#     #     print(S)
#     # else:
#     #     print('gaada')

#toRegex(kalimat)