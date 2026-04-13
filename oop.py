class Parrot:
    species='bird'

    def __init__(self,name,age):
        self.name=name
        self.age=age

bluey=Parrot("Bluey",10)

print(bluey.name,"is",bluey.age,"years")

louis=Parrot("Louis",11)

print(louis.name,"is",louis.age,"years")

#code 2

class Student:
    stream='coding'

    def __init__(self,roll,address):
        self.roll=roll
        self.address=address

Student1=Student(58,"JamalKhan,Chattogram")
print("Student's roll no is",Student1.roll,"Student's address is",Student1.address)