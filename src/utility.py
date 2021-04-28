import re
from datetime import datetime, date, timedelta
from bm import *
from kmp import *

# chatbot utilities
keywords = {'Tubes','Quiz','Tucil','Ujian','PR','Praktikum'}
months_synonym = {'agu' : 'aug', 'mei' : 'may', 'des' : 'dec', 'okt' : 'oct'}
date1pattern = r'(\d{2})[/-](\d{2})[/-](\d{4})'
date2pattern = r'(\b\d{1,2}\D{0,3})?\b(?:[jJ]an(?:uari)?|[fF]eb(?:ruari)?|[mA]ar(?:et)?|[aA]pr(?:il)?|[mM]ei|[jJ]un(?:i)?|[jJ]ul(?:i)?|[aA]ug(?:ust)?|[aA]gustus?|[sS]ep(?:tember)?|[oO][ck]t(?:ober)?|([nN]ov|[dD]e[cs])(?:ember)?)\D?(\d{1,2}\D?)?\D?((19[7-9]\d|20\d{2})|\d{2})'
kodepattern = r'([kK][uU]|[iI][fF])(\d{2})(\d{2})'
timeperiodpattern = r'\b[0-9]+?\b\s([hH]ari|[mM]inggu)'
todaypattern = r'\b[hH]ari\b\sini'
taskidpattern = r'\b[tT]ask\b\s[0-9]+?\b'

keyword = None
kodematkul = None
tanggal = None
tanggal_period = None
deadline = None
task_id = None
selesai = None
topik = None


def getDate(S):
    ''' return komponen date pada string S '''
    date = re.search(date1pattern,S)
    if not date:
        date = re.search(date2pattern,S)
        if (not date):
            return -1
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
    ''' return id task string S '''
    taskid = re.search(taskidpattern,S)
    if taskid:
        return int(taskid.group().split(' ')[1])
    return -1


def findAllDate(S):
    ''' return list of komponen date pada string S '''
    date = []
    date1 = re.findall(date1pattern,S)
    date2 = re.findall(date2pattern,S)
    for i in range(len(date1)):
        newdate1 = re.search(date1pattern,S)
        S = re.sub(date1pattern,'done',S,1)
        if (newdate1):
            date.append(newdate1.group())
    for i in range(len(date2)):
        newdate2 = re.search(date2pattern,S)
        S = re.sub(date2pattern,'done',S,1)
        if (newdate2):
            date.append(newdate2.group())
    return date


def getDatePeriod(S):
    ''' 
    return komponen date period pada string S
    [2020-12-21, 2021-12-21] dimana elmt pertama
    adalah start date dan elmt ke-2 adalah enddate
    '''
    timeperiod = []
    if bm(S,'hari ini') != -1:
        enddate = date.today()
        timeperiod.append(date.today())
        timeperiod.append(enddate)
        return timeperiod
    else:
        period = re.search(timeperiodpattern,S)
        if not period:
            period = findAllDate(S)
            if (len(period) < 2):
                return -1
            timeperiod.append(getDate(period[0]))
            timeperiod.append(getDate(period[1]))
            return timeperiod
        period = period.group().split(' ')
        if kmp('minggu',period[1]) != -1:
            enddate = date.today() + timedelta(days=int(period[0])*7)
        elif kmp('hari',period[1]) != -1 :
            enddate = date.today() + timedelta(days=int(period[0]))
        timeperiod.append(date.today())
        timeperiod.append(enddate)
        return timeperiod


def getKodeMatkul(S):
    ''' return kode matkul pada string S'''
    kode = re.search(kodepattern,S)
    if (kode):
        return kode.group().upper()
    return -1

def getTopik(S):
    ''' return topik tugas pada string S '''
    kode = re.search(kodepattern,S)
    if (kode):
        return str(S.partition(kode.group()+str(' '))[2])
    return -1


def inspectQuery(S):
    global keyword
    global kodematkul
    global tanggal
    global tanggal_period
    global deadline
    global task_id
    global selesai
    global topik
    keyword = getKeyword(S)
    tanggal_period = getDatePeriod(S)
    if tanggal_period == -1:
        tanggal = getDate(S)
    kodematkul = getKodeMatkul(S)
    topik = getTopik(S)
    task_id = getTaskId(S)
    deadline = kmp(S,"deadline") or bm(S,"deadline")

    if (isAdded()):
        print(1)
        return 1
    elif (deadline != -1 and keyword != -1 and kodematkul != -1):
        print(5)
        return 5
    elif (deadline != -1):
        if (tanggal != -1 and task_id != -1):
            print(6)
            return 6
        elif (tanggal_period == -1 and keyword == -1):
            print(2)
            return 2
        elif (tanggal_period != -1 and keyword == -1):
            print(3)
            return 3
        elif (tanggal_period != -1 and keyword != -1) :
            print(4)
            return 4
    elif (isRemove(S)):
        print(7)
        return 7     
    elif (isHelp(S)):
        print(8)        
        return 8
    else:
        return -1

def getKeyword(S):
    '''
    return kata penting di string S
    '''
    for kata in keywords:
        if (kata.lower() in S.lower().split(' ')):
            return kata
    return -1

def isAdded():
    return (tanggal != -1 and kodematkul and keyword != -1 and topik != -1)

def isUpdate(S):
    '''
    Mengembalikan true jika terdapat tanggal dan kata deadline dan diundur
    dan kata deadline muncul sebelum diundur
    '''
    deadline = kmp(S,"deadline")
    return getDate(S) != -1 and deadline != -1

def isRemove(S):
    '''
    Mengembalikan true jika terdapat kata 'selesai mengerjakan'
    delete dari task
    '''
    return kmp(S,"selesai mengerjakan") != -1 and bm(S,"selesai mengerjakan") != -1

def isHelp(S):
    '''
    Mengembalikan true jika terdapat kata 'bisa lakukan' 'aastrobot' 'help'
    '''
    helpflag1 = (bm(S,"bisa lakukan")!=-1) or (bm(S,"help")!=-1)
    return helpflag1 and keyword == -1 and tanggal == -1

if __name__ == "__main__":
    kalimat = 'Halo bot, task ong ingetin aku ya ada pada  14/12/2021 14/10/2021 tubes if2211 bab 2 sampai 3 cacatt loo'
    inspectQuery(kalimat)
    print(tanggal_period,tanggal,kodematkul, topik)