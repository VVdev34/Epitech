#Task 1.1 ---------------------------

(42>42) # 42 est supérieur à 12
(12 = 12) # 12 est égale à 12
(12 == 12) # 12 est strictement égal à 12
("hello" == "world") # Str hello est stricetement égal à str world 
( ("a".upper() == "A")) # Methode upper() "a" est strictement égal à A
(1*2*3*4 <= 9) # Inférieur ou égal 
("z" in "azerty") # "z" appartient à "azerty"

#Task 1.2 ---------------------------
a = int(input("Write a integer "))
if a == 42:
    print("Correct answer")
else:
    print("Wrong answer")

#Task 1.3 ---------------------------

a = int(input("Write a integer "))
if a % 2 == 0:
    print("The integer it's even")

#else: 
    print("This integer it's odd")

#Task 1.4 ---------------------------

a = input("Write a string ") 
if a == "Open sesame":
    print("Acces granted")
elif a == "Will you open, you Goddamn fuck":
    print("Access fucking granted")
else : print("permission denied")

#Task 1.5 ---------------------------

a = int(input("Write a integer"))
if a == 42:
    print("OK")
elif a <= 21: 
    print("OK")
elif a % 2 == 0 and a % 2 < 21:
    print("OK")
elif a % 3 and a >= 45:
    print("OK")
else : print("You got wrong my poor friend!")

#Task 1.6 ----------------------------

a = 42
b = 41
if a == b:
    print("A and B are the same")
if b <= a:
    print ("B is equal or lower than A")
if b != a:
    print("B is different from A")

#Task 2.1 ---------------------------

a = 0 
for a in range (1000):
    a = a +1 
    print(a)

#Task 2.2 -------------------------

a = input("Write a string")
res = ""
for i in a:
    res += i*2
print(res)

#Task 2.3 -------------------------

for i in range(1,1000):
    if i%7 == 0:
        print("Ces numeros sont divisible par 7 :", i)
        i += 1

#Task 2.4 -------------------------

for i in range(-30,30):
    if i %3 == 0:
        print("Fizz")
    elif i %5 == 0:
        print("Buzz")
    elif i %5 == 0 and i%3 == 0:
        print ("FizzBuzz")
    else: print(i)

#Task 2.5 ----------------------------

for i in range(99, 0, -1):
    if(i == 1):
        print("{} bottle of beer on the wall, {} bottle of beer, take one down, pass it around, no bottles of beer on the wall".format(i, i))
    else:
       print("{} bottles of beer on the wall, {} bottles of beer, take one down, pass it around, {} bottles of beer on the wall".format(i, i, i-1))

#Task 2.6 ---------------------------

n = int(input("Write number")) 
for i in range(2, n//2 + 1):
        multiples = []
        for m in range(i, n, i):
            multiples.append(m)
        print(multiples[::-1])

# Challenge ------------------------   

def challenge():
    ask_int = int(input("Write nbr : "))
    ask_str = input("Write str : ") 
    vowels = str(["a", "e", "i","o","u","y"])
    if ask_int == 0: 
        exit(challenge())
    elif ask_int >= 42:
            print(ask_int)
    for vowel in vowels:
        if vowel in ask_str:
            print(ask_int)
       
    else : print(ask_str) 
challenge()

