import add
from qrdetect import data
import os
books=data
def switch():
    print(" ")
option= int(input("your option : 1 for new user , 2 for existing user and 3 for only reading a book:"))

if option == 1:
    add.add_one(input('enter name'),input('enter roll no'),books)

elif option == 2:
    add.update_one(input('enter name'),input('enter roll no'),books)
elif option == 3:
    print("Enjoy your book:"+books+" and dont forget to return after 30 mins")

else:
    print("Incorrect option")

switch()
