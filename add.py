import sqlite3
def add_one(name,rollno,books_borrowed):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute(" INSERT INTO LMS VALUES(?,?,?)",(name,rollno,books_borrowed))
    conn.commit()
    conn.close()
def update_one(updated_name,roll_no,update_books):
    conn = sqlite3.connect('library.db')
    c = conn.cursor()
    c.execute("UPDATE lms SET books_borrowed=(?) WHERE rollno=(?)",(update_books,roll_no))
    print("Your borrowed books are updated " +updated_name)
    conn.commit()
    conn.close()












