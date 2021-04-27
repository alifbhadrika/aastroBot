import re
import itertools
from Sastrawi.StopWordRemover.StopWordRemoverFactory import StopWordRemoverFactory
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory
from datetime import datetime
import sys
stemmer = StemmerFactory().create_stemmer()
stopword = StopWordRemoverFactory().create_stop_word_remover()

keywords = {'tubes','quiz','tucil','tubes','pr'}
months_synonym = {'agu' : 'aug', 'mei' : 'may', 'des' : 'dec', 'okt' : 'oct'}


kalimat = 'Halo bot, tolong ingetin aku ya ada tubes if2211 bab 2 sampai 3 pada 14-10-2012'

tgl = re.search(r'(\d{2})[/-](\d{2})[/-](\d{4})',kalimat)
tgl_bulan = re.search(r'(\b\d{1,2}\D{0,3})?\b(?:[jJ]an(?:uari)?|[fF]eb(?:ruari)?|[mA]ar(?:et)?|[aA]pr(?:il)?|[mM]ei|[jJ]un(?:i)?|[jJ]ul(?:i)?|[aA]ug(?:ust)?|[aA]gustus?|[sS]ep(?:tember)?|[oO][ck]t(?:ober)?|([nN]ov|[dD]e[cs])(?:ember)?)\D?(\d{1,2}\D?)?\D?((19[7-9]\d|20\d{2})|\d{2})',kalimat)
matkul = re.search(r'([kK][uU]|[iI][fF])(\d{2})(\d{2})',kalimat)

def date(S):
    date = re.search(r'(\d{2})[/.-](\d{2})[/.-](\d{4})',S)
    if not date:
        date = re.search(r'(\b\d{1,2}\D{0,3})?\b(?:[jJ]an(?:uari)?|[fF]eb(?:ruari)?|[mA]ar(?:et)?|[aA]pr(?:il)?|[mM]ei|[jJ]un(?:i)?|[jJ]ul(?:i)?|[aA]ug(?:ust)?|[aA]gustus?|[sS]ep(?:tember)?|[oO][ck]t(?:ober)?|([nN]ov|[dD]e[cs])(?:ember)?)\D?(\d{1,2}\D?)?\D?((19[7-9]\d|20\d{2})|\d{2})',S)
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