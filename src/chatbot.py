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
            toReturn = "Task Added" + "(ID:" + str(idx) + ") " + \
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
            toReturn += str(task) + "<br>"
        if(toReturn != ""):
            return toReturn
        else:
            return "Tidak terdapat task"
    elif (ret == 3):
        # Melihat daftar task di periode waktu start dan date
        startdate = u.tanggal_period[0]
        enddate = u.tanggal_period[1]
        tasks = q.checkTaskDatePeriod(startdate, enddate)
        toReturn = ""
        for task in tasks:
            toReturn += str(task) + "<br>"
        if(toReturn != ""):
            return toReturn
        else:
            return "Tidak terdapat task pada periode yang telah ditentukan"
    elif (ret == 4):
        # Melihat daftar task di periode waktu start dan date
        startdate = u.tanggal_period[0]
        enddate = u.tanggal_period[1]
        tasks = q.checkSpecificTaskDatePeriod(u.keyword, startdate, enddate)
        toReturn = ""
        for task in tasks:
            toReturn += str(task) + "<br>"
        if(toReturn != ""):
            return toReturn
        else:
            return "Tidak terdapat task pada periode yang telah ditentukan"
    elif (ret == 5):
        # Lokit Deadline   
        deadline = q.getDeadline(u.kodematkul, u.keyword)
        toReturn = ""
        for date in deadline:
            toReturn += str(date) +"<br>"
        if(toReturn != ""):
            return toReturn
        else:
            return "Tidak terdapat task pada waktu yang telah ditentukan"
    elif (ret == 6):
        # Update
        if (q.updateTask(u.task_id,u.tanggal)):
            return "Berhasil memperbarui deadline task ke "+str(u.task_id)+" menjadi "+str(u.tanggal)+" pada daftar task"
        else:
            return "Tidak terdapat task ke "+str(u.task_id)+" pada daftar task"
    elif (ret == 7):
        # Delete
        if (q.removeTask(u.task_id)):
            return "Berhasil menghapuskan task ke "+str(u.task_id)+" pada daftar task"
        else:
            return "Tidak terdapat task ke "+str(u.task_id)+" pada daftar task"
    elif(ret == 8):
        # Help
        retval = '''
        Hi!<br>
        AastroBot adalah asisten pencatan tugas tugas kamu, biar kagak kelewat deadline mulu<br><br>
        [Feature] <br>
        1. Menambahkan task baru<br>
        2. Melihat daftar task<br>
        3. Melihat deadline untuk task tertentu<br>
        4. Memperbarui task<br>
        5. Menghapus task<br><br>

        [Keyword list]<br>
        1. Kuis<br>
        2. Ujian<br>
        3. Tucil<br>
        4. Tubes<br>
        5. PR<br>
        6. Praktikum<br>
        '''
        return retval
    else:
        return """Maaf pesan tidak dikenali, anda dapat menuliskan "Apa yang bisa bot lakukan" untuk mengetahui daftar fitur"""

if __name__ == "__main__":
    # print(type(q.checkTasks()))
    # print("Masukkan pesan: ", end = "")
    text = "deadline hari ini"
    # toInput = input()
    print(getSuitableResponses(text))
    # print(u.inspectQuery(text))
    # print(u.tanggal,u.tanggal_period,u.keyword)
    # getSuitableResponses(text)