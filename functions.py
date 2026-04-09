def greet(name):
    print("Hello " + name +".Good morning" )
greet('Sahil')
greet('Shopnil')

print('finding absolute number')
def absolute_num(num):
    if num>=0:
        return num
    else:
        return -num
print("Absolute value of the number is" ,absolute_num(98))
print("Absolute value of the number is" ,absolute_num(-198))

print('Finding out palindromes')
def palindrome(word):
   if word==word[::-1]:
       return True
   else:
       return False
  
if palindrome('Mrinmoy'):
  print('The word is palindrome')
else:
  print('The word is not palindrome')