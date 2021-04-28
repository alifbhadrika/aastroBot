import re
import itertools
import sys
import utility as u
import query as q
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
        # Add Task
        if (q.addTaskThroughBot(u.tanggal, u.keyword, u.topik, u.kodematkul)):
            return "Added"
        else:
            print("not added")
            return "not Added"
    elif (ret == 2):
        # Melihat daftar task
        q.checkTasks()
    elif (ret == 3):
        # Melihat daftar task di periode waktu start dan date
        startdate = u.tanggal_period[0]
        enddate = u.tanggal_period[1]
        q.checkTaskDatePeriod(startdate, enddate)
    elif (ret == 4):
        # Melihat daftar task di periode waktu start dan date
        startdate = u.tanggal_period[0]
        enddate = u.tanggal_period[1]
        q.checkSpecificTaskDatePeriod(u.keyword, startdate, enddate)
    elif (ret == 5):
        # Lokit Deadline   
        deadline = q.getDeadline(u.kodematkul, u.keyword)
        print(deadline)
        return "Itu ya Deadlinenya"   
    elif (ret == 6):
        # Update
        if (q.updateTask(u.task_id,u.tanggal)):
            return "Berhasil memperbarui deadline task ke "+str(u.task_id)+" menjadi "+str(u.tanggal)+" pada daftar task"
        else:
            return "Tidak terdapat task ke "+str(u.task_id)+" pada daftar task"
    elif (ret == 7):
        # Delete
        task_id = u.getTaskId()
        if (q.removeTask(task_id)):
            return "Berhasil menghapuskan task ke "+str(task_id)+" pada daftar task"
        else:
            return "Tidak terdapat task ke "+str(task_id)+" pada daftar task"
    elif(ret == 8):
        # Help
        return 
        '''
        Hi!
        AastroBot adalah asisten pencatan tugas tugas kamu, biar kagak kelewat deadline mulu
        [Feature] 
        1. Menambahkan task baru
        2. Melihat daftar task
        3. Melihat deadline untuk task tertentu
        4. Memperbarui task
        5. Menghapus task

        [Keyword list]
        1. Kuis
        2. Ujian
        3. Tucil
        4. Tubes
        5. PR
        6. Praktikum
        '''
    else:
        return """Maaf pesan tidak dikenali, anda dapat menuliskan "Apa yang bisa bot lakukan" untuk mengetahui daftar fitur"""

if __name__ == "__main__":
    q.checkTasks()
    print("Masukkan pesan: ", end = "")
    text = input()
    getSuitableResponses(text)
    print(u.inspectQuery(text))
    print(u.tanggal,u.tanggal_period,u.keyword)
    # getSuitableResponses(text)