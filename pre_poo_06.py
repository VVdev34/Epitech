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

#Task 2.1

punctuation = '''!()-[]{};:'",<>./?@#$%^&*_~'''

def palindrome(x):
    x = str(x)
    x = x.lower()

    for i in x :
        if i in punctuation:
            x = x.replace(i,"")
        x = x.replace (" ","")
        if len(x) <= 1 and x[0] == x [-1]:
            return palindrome(x[1:-1])
    else : 
        return False 
    
palindrome("Was it a car or a cat I saw")
