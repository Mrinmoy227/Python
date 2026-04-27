import sys
#Create initial phonebook
def initial_phonebook():
    rows,cols=int(input("Please enter initial numbers of contacts")),5
    phone_book=[]

    for i in range(rows):
        print("\n  Enter contatc details"%(i+1))
        temp=[]

        for j in range(cols):
            if j==0:
                temp.append(str(input("Enter your name:")))
                if temp[j]==" ":
                    sys.exit("Name is mandotory!")

            if j==1:
                temp.append(int(input("Enter number:")))

            if j==2:
                temp.append(str(input("Enter e-mail:")))
                if temp[j]==" ":
                   temp[j]=None

            if j==3:
                temp.append(str(input("Enter D.O.B:")))
                if temp[j]==" ":
                   temp[j]=None

            if j==4:
                temp.append(str(input("Enter Category:")))
                if temp[j]==" ":
                   temp[j]=None
        phone_book.append(temp)

#Menu
def Menu():
    print("\n 1.ADD")
    print("2.REMOVE")
    print("3.DELETE ALL")
    print("4.DISPLAY ALL")
    print("Exit")
    return int(input("Enter Choice"))