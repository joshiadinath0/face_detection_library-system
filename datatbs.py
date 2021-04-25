import sqlite3
conn= sqlite3.connect('library.db')
c   =  conn.cursor()
c.execute("""CREATE TABLE lms(
        Name text,
        rollno text,
        books_borrowed text    
        )""")
conn.commit()
conn.close()
