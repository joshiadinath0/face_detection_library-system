print("LIBRARY MANAGEMENT SYSTEM")
print("Press 1 to Start a program \n press 2 to register your face \n press 3 to train faces \n press 4 to generate qr code for books \n press 5 to create a database first time")
def switch():
    print("")
option= int(input("your option : "))
if option == 1:
    exec(open('face_recognition.py').read())
elif option == 2:2
    exec(open('Face_dataset.py').read())
elif option == 3:
    exec(open('face_training.py').read())
elif option == 4:
    exec(open('makecode.py').read())
elif option == 5:
    exec(open('datatbs.py').read())
else:
    print("Incorrect option")
switch()

print("Press 1 to Start again \n and 2 to exit program")

def switch2():
    print("")
option1= int(input("your option : "))

if option1 == 1:
    exec(open('app.py').read())
else:
    print("Library Management System is exited")
switch2()