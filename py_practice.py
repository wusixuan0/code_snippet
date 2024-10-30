print('hello world')
x = 3              # a whole number                   
f = 3.1415926      # a floating point number              
name = "Python"    # a string

print(x)
print(f)
print(name)

combination = name + " " + name
print(combination)

sum = f + f
print(sum)

x = "Hello"
print(x)
print(x[0])
print(x[5]) #error

x = "hello world"
s = x[0:3] #hel
print(s)
s = x[:3]
print(s)
s = x[-1] #d

s = "Hello World"
s = s.replace("World","Universe")
print(s)

s = "Hello World World World"
s = s.replace("World","Universe",1) # replaces only the first item
print(s)

s = "That I ever did see. Dusty as the handle on the door"

index = s.find("Dusty")
print(index)

if "Dusty" in s:
    print("query found")

index = s.find("Dusty") #the find method returns the index if a word is found. If not found, it returns -1
print(index)

words = ["How","are","you","doing","?"]
sentence = ' '.join(words)
print(sentence)

s = "Its to easy"
words = s.split() # split into list
print(words)

name = input('What is your name? ')
if <condition>:
    <statement>
    <statement>
    <statement>

<statement>  # not in block

#Create a loop that counts from 0 to 100
for number in range(100):
    print(number)

for number in range(0, 100, 3): #range(start, stop, step)
    print(number)

def f(x,y):
    return x*y

print(f(3,4))

x = [3,4,5]
x.append(6)
print(x)
x.append(7)
print(x)
x.pop()
print(x)

pizza="pizza"
slice = pizza[0:2] #a copy of pizza
print(slice)

#!/usr/bin/python
persons = [ "John", "Marissa", "Pete", "Dayton" ]

slice = persons[0:2]
print(slice)

try:
    <do something>
except Exception:
    <handle the error>

try: 
    1 / 0
except ZeroDivisionError: 
    print('Divided by zero')

print('Should reach here')