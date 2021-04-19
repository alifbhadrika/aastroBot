import sqlite3

def create_db():
    conn = sqlite3.connect("aastrobot.db")
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

def check():
    conn = sqlite3.connect("aastrobot.db")
    c = conn.cursor()
    c.execute("""
    SELECT *
    FROM kata_penting
    """)
    res = c.fetchall()
    print(res)
    conn.commit()
    conn.close()

def addTask(entry):
    conn = sqlite3.connect("aastrobot.db")
    c = conn.cursor()
    c.execute("INSERT INTO tasks VALUES(?,?,?,?,?)", entry)
    print("Berhasil menambahkan record", end=" ")
    print(entry, end=" ")
    print("ke data tasks")
    conn.commit()
    conn.close()