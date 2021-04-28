import re
import itertools
import sys
import utility as u
import query as q
from datetime import datetime

def getSuitableResponses(text):
    ret = u.inspectQuery(text)
    if (ret == 1):
        # Add Task
        if (q.addTaskThroughBot(u.tanggal, u.keyword, u.topik, u.kodematkul)):
            idx = q.getLastId()
            toReturn = "Task Added\n" + "(ID:" + str(idx) + ") " + \
                str(u.tanggal) + " - " + str(u.kodematkul) + " - " + \
                str(u.keyword) + " - " + str(u.topik)
            return toReturn
        else:
            return "Nothing Added, Try Again"
    elif (ret == 2):
        # Melihat daftar task
        tasks = q.checkTasks()
        toReturn = ""
        for task in tasks:
            toReturn += str(task) + "\n"
        return toReturn
    elif (ret == 3):
        # Melihat daftar task di periode waktu start dan date
        startdate = u.tanggal_period[0]
        enddate = u.tanggal_period[1]
        tasks = q.checkTaskDatePeriod(startdate, enddate)
        toReturn = ""
        for task in tasks:
            toReturn += str(task) + "\n"
        return toReturn
    elif (ret == 4):
        # Melihat daftar task di periode waktu start dan date
        startdate = u.tanggal_period[0]
        enddate = u.tanggal_period[1]
        tasks = q.checkSpecificTaskDatePeriod(u.keyword, startdate, enddate)
        toReturn = ""
        for task in tasks:
            toReturn += str(task) + "\n"
        return toReturn
    elif (ret == 5):
        # Lokit Deadline   
        deadline = q.getDeadline(u.kodematkul, u.keyword)
        toReturn = ""
        for date in deadline:
            toReturn += str(date) +"\n"
        return toReturn
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
        retval = '''
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
        return retval
    else:
        return """Maaf pesan tidak dikenali, anda dapat menuliskan "Apa yang bisa bot lakukan" untuk mengetahui daftar fitur"""

if __name__ == "__main__":
    q.checkTasks()
    print("Masukkan pesan: ", end = "")
    text = "Apa yang bot bisa lakukan?"
    # toInput = input()
    # print(getSuitableResponses(toInput))
    # print(u.inspectQuery(text))
    # print(u.tanggal,u.tanggal_period,u.keyword)
    # getSuitableResponses(text)