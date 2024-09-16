#Task 1.1 -------------------

#def f (x):
#    return 2*x+1

#def g():
#    return 7 

#y = f(2)
#print(y)

#y = f(5) + g()
#print(y)

#Task 1.2 --------------------

#def bread():
#   return  "<//////////>" 

    

#def lettuce():
#   return "~~~~~~~~~~~~"
   

#def tomato():
#   return  "O O O O O O"
 

#def ham():
#    return  "============"


#bread()
#lettuce()
#tomato()
#ham()
#ham()
#bread()

#Task 1.3 -------------------

#for i in range(0,42):
#    bread()
#    lettuce()
#    tomato()
#    ham()
#    bread()

#Task 1.4 -------------------

#def sandwich(): 
#    print(bread())
#    print(lettuce())
#    print(tomato())
#    print(ham())
#    print(bread())

#Task 1.5 -----------------------------

#def sandwich_veggie():
#    print(bread())
#    print(lettuce())
#    print(tomato())
#    print(lettuce())
#    print(tomato())
#    print(bread())

#def sandwiches(x,v):
#    if v  >= 1 :
#        for y in range(0, x):
#            sandwich_veggie()
#    else :
#        if x >= 1:
#            for i in range(0, x):
#                sandwich()
#        else :
#            print("I can't do this") 

#sandwiches(0,0)

#Task 1.5 ------------------ look up 

#Challenge -----------------

#x = 84
#for i in range(0, x):
#    res =  42 ** x
#print(res)

#Task 2.1 -------------------

#punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''

#def palindrome(x):
#    x = str(x)
#    x = x.lower()

#    for i in x :
#        if i in punctuation:
#            x = x.replace(i,"")
#        x = x.replace (" ","")

#    print(x == x[::-1])
    
    
#palindrome("Kayak")

#Task 2.2 ---------------------


def lower(x,y):
    total = 0
    for letter in x:
        total += letter.islower()
    return total >= y



def upper(x,y):
    total = 0
    for letter in x:
        total += letter.isupper()
    return total >= y



def characters(x,y):
    total = 0
    for letter in x:
        total += len(letter)
    return total >= y




def special(x,y):
    symbols = "!@#$%^&*()-+?_=,<>"
    total = 0
    for symbol in x:
        if symbol in symbols:
            total += 1
    return total >= y
    



def number(x,y):
    total = 0
    for number in x:
        total += number.isdigit()
    return  total >= y




#Task 3.2 ------------------------
def check_password(option,x,y):
  return option(x,y)

print(check_password(lower, "secretpassword", 4))
print(check_password(special,'secretpassword', 2))













