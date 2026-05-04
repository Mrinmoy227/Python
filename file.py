file=open('Sample.txt')
print(file.read())
file.close

#Open file in write mode
file=open('Sample.txt','w')
file.write("File in write mode")
file.close

#Open file in append mode
file=open('Sample.txt','a')
file.write("\n Adding a extra line")
file.close

file=open('Sample.txt','r')
lines=file.readlines()
print(len(lines))