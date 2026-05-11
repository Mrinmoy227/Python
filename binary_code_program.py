text = """
Coding is basically the computer language used to develop apps, websites, and software.

Without coding, technologies like Facebook, smartphones, and web browsers would not exist.
Code tells the computer what to do.

Computers only understand binary signals:
1 = ON
0 = OFF

Programming languages were created to make coding easier for humans.
"""

# Write data into a file
with open("computer_info.txt", "w") as file:
    file.write(text)

print("Text written successfully into computer_info.txt")

# Read data from the file
with open("computer_info.txt", "r") as file:
    content = file.read()

print("\nReading from the file:\n")
print(content)