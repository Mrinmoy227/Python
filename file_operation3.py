with open('codingal.txt','w') as file:
    file.write("Hi! I am Mrinmoy")
file.close()

#split file into words
with open ('codingal.txt','r') as file:
    data=file.readlines()
    for line in data:
        word=line.split()
        print(word)
file.close()

updated=open('updated.txt','w')
repeated=open('repeated.txt','r')

duplicate=set()
for line in repeated:
    if line not in duplicate:
        updated.write(line)
        duplicate.add(line)
repeated.close
updated.close