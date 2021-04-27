import re
from datetime import datetime, date, timedelta
from bm import *
from kmp import *

# chatbot utilities
keywords = {'tubes','quiz','tucil','tubes','pr'}
months_synonym = {'agu' : 'aug', 'mei' : 'may', 'des' : 'dec', 'okt' : 'oct'}
date1pattern = r'(\d{2})[/-](\d{2})[/-](\d{4})'
date2pattern = r'(\b\d{1,2}\D{0,3})?\b(?:[jJ]an(?:uari)?|[fF]eb(?:ruari)?|[mA]ar(?:et)?|[aA]pr(?:il)?|[mM]ei|[jJ]un(?:i)?|[jJ]ul(?:i)?|[aA]ug(?:ust)?|[aA]gustus?|[sS]ep(?:tember)?|[oO][ck]t(?:ober)?|([nN]ov|[dD]e[cs])(?:ember)?)\D?(\d{1,2}\D?)?\D?((19[7-9]\d|20\d{2})|\d{2})'
kodepattern = r'([kK][uU]|[iI][fF])(\d{2})(\d{2})'
timeperiodpattern = r'\b[0-9]+?\b\s([hH]ari|[mM]inggu)'
todaypattern = r'\b[hH]ari\b\sini'
taskidpattern = r'\b[tT]ask\b\s[0-9]+?\b'


kalimat = 'Halo bot, hari task 9 ini tolong ingetin aku ya ada pada 14-12-2012 tubes if2211 bab 2 sampai 3 cacatt loo'

def getDate(S):
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
        return dt.date()
    date = date.group()
    if ('-' in date):
        date = '/'.join(date.split('-'))
    dt = datetime.strptime(date, '%d/%m/%Y')
    return dt.date()

def getTaskId(S):
    taskid = re.search(taskidpattern,S)
    if taskid:
        return taskid.group().split(' ')[1]


def findAllDate(S):
    date = []
    date1 = re.search(date1pattern,S)
    date2 = re.search(date2pattern,S)
    if (date1):
        date.append(getDate(date1.group()))
    if (date2):
        date.append(getDate(date2.group()))
    return date


def getDatePeriod(S):
    timeperiod = []
    period = re.search(timeperiodpattern,S)
    if not period:
        period = findAllDate(S)
        if (len(period) < 2):
            return
        timeperiod.append(getDate(period[0]))
        timeperiod.append(getDate(period[1]))
        return timeperiod
    period = period.group().split(' ')
    if period[1] == 'minggu':
        enddate = date.today() + timedelta(days=int(period[0])*7)
    else :
        enddate = date.today() + timedelta(days=int(period[0]))
    timeperiod.append(date.today())
    timeperiod.append(enddate)
    return timeperiod

def getKodeMatkul(S):
    kode = re.search(kodepattern,S)
    if (kode):
        return kode.group().upper()
    return

def getTopik(S):
    kode = re.search(kodepattern,S)
    if (kode):
        return str(S.partition(kode.group()+str(' '))[2])
    return


def inspectQuery(S):
    global keyword
    global kodematkul
    global tanggal
    global tanggal_period
    global deadline
    global task_id
    global selesai
    global topik
    tanggal_period = getDatePeriod(S)
    if not tanggal_period:
        tanggal = getDate(S)
    kodematkul = getKodeMatkul(S)
    spektask = getTopik(S)

'''
keyword = None
kodematkul = None
tanggal = None
tanggal_period = None
deadline = None
task_id = None
selesai = None
topik = None


inspectQuery(kalimat)
print(tanggal_period,tanggal,kodematkul)
'''