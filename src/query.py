import sqlite3
import os

def create_db():
    db = os.path.join(os.path.dirname(__file__), '..\\test\\aastrobot.db')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute('DROP TABLE IF EXISTS kata_penting')
    c.execute("""
    CREATE TABLE kata_penting (
        jenis_tugas TEXT PRIMARY KEY
    );
    """)
    c.execute("""
    INSERT INTO kata_penting
    VALUES
        ("Kuis"),
        ("Ujian"),
        ("Tucil"),
        ("Tubes"),
        ("PR"),
        ("Praktikum");
    """)
    c.execute('DROP TABLE IF EXISTS tasks')
    c.execute("""
    CREATE TABLE tasks (
        id_task INT PRIMARY KEY,
        tanggal DATE NOT NULL,
        mata_kuliah TEXT NOT NULL,
        jenis_tugas TEXT NOT NULL,
        topik_tugas TEXT NOT NULL,
        FOREIGN KEY (jenis_tugas) REFERENCES kata_penting(jenis_tugas)
    );
    """)
    conn.commit()
    conn.close()

def checkKataPenting():
    db = os.path.join(os.path.dirname(__file__), '..\\test\\aastrobot.db')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("""
    SELECT *
    FROM kata_penting
    """)
    res = c.fetchall()
    print(res)
    conn.commit()
    conn.close()

def checkTasks():
    db = os.path.join(os.path.dirname(__file__), '..\\test\\aastrobot.db')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("""
    SELECT *
    FROM tasks
    """)
    res = c.fetchall()
    print(res)
    conn.commit()
    conn.close()

def getDeadline(kodematkul, keyword):
    db = os.path.join(os.path.dirname(__file__), '..\\test\\aastrobot.db')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    toQuery = (kodematkul, keyword, )
    c.execute("""
    SELECT tanggal
    FROM tasks
    WHERE mata_kuliah = ? and jenis_tugas = ?
    """, toQuery)
    res = c.fetchall()
    print(res)
    conn.commit()
    conn.close()
    return res

def addTask(entry):
    db = os.path.join(os.path.dirname(__file__), '..\\test\\aastrobot.db')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("INSERT INTO tasks VALUES(?,?,?,?,?)", entry)
    print("Berhasil menambahkan record", end=" ")
    print(entry, end=" ")
    print("ke data tasks")
    conn.commit()
    conn.close()

def addTaskThroughBot(tanggal, keyword, topik, kodematkul):
    db = os.path.join(os.path.dirname(__file__), '..\\test\\aastrobot.db')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    idx = 1
    if (getLastId() != None):
        idx = getLastId() + 1
    added = True
    try:
        entry = (idx, tanggal, kodematkul, keyword, topik,)
        c.execute("INSERT INTO tasks VALUES(?,?,?,?,?)", entry)
        print("done")
    except:
        added = False
    conn.commit()
    conn.close()
    return added

def updateTask(id_task, tanggal):
    db = os.path.join(os.path.dirname(__file__), '..\\test\\aastrobot.db')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    updated = True
    try:
        c.execute("UPDATE tasks SET tanggal = ? WHERE id_task = ?", (tanggal, id_task,))
        print("Berhasil mengupdate task", end=" ")
        print(id_task, end=" dari data tasks")
    except:
        updated = False
    conn.commit()
    conn.close()
    return updated
    
def removeTask(id_task):
    print(id_task)
    print(type(id_task))
    db = os.path.join(os.path.dirname(__file__), '..\\test\\aastrobot.db')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    removed = True
    try:
        c.execute("DELETE FROM tasks WHERE id_task = ?", (id_task,))
        print("Berhasil menghapuskan task", end=" ")
        print(id_task, end=" dari data tasks")    
    except:
        removed = False
    conn.commit()
    conn.close()
    return removed

def getLastId():
    db = os.path.join(os.path.dirname(__file__), '..\\test\\aastrobot.db')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT MAX(id_task) FROM tasks")
    result = c.fetchone()
    conn.commit()
    conn.close()
    return result[0]

def checkTaskDatePeriod(startdate, enddate):
    db = os.path.join(os.path.dirname(__file__), '..\\test\\aastrobot.db')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE tanggal BETWEEN ? AND ?",(startdate, enddate,))
    res = c.fetchall()
    print(res)
    conn.commit()
    conn.close()

def checkSpecificTaskDatePeriod(task, startdate, enddate):
    db = os.path.join(os.path.dirname(__file__), '..\\test\\aastrobot.db')
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute("SELECT * FROM tasks WHERE jenis_tugas = ? AND (tanggal BETWEEN ? AND ?)",(task, startdate, enddate,))
    res = c.fetchall()
    print(res)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    # create_db()
    end = False
    checkTasks()
    '''
    id_task, tanggal, mata_kuliah, jenis_tugas, topik_tugas,
    '''
    while not end:
        x = int(input())
        if (x == 0):
            entry = input().split()
            addTask(entry)
            checkTasks()
        elif (x==1):
            id, tanggal = input().split()
            updateTask(int(id),tanggal)
            checkTasks()
        elif (x==2):
            id = int(input())
            removeTask(id)
            checkTasks()
        elif (x==3):
            print(getLastId())
        else:
            end = True
    create_db()