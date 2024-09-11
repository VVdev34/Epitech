#Task 1.1 ----------
v = "Hello world"
#print(v)

#Task 1.2 ----------
v = "Hello world"
first_char = v[0]
fith_char = v[4]
#print("Prmeiere lettre :", first_char , "Cinquieme lettre:", fith_char)

#Task 1.3 ----------
v = "Hello world"
last_char = v[-1]
#print("Derniere lettre :", last_char)

#Task 1.4 -----------
v = "Hello world"
fith_to_tenth = v[4:9] # Sliced ":" sur string
#print("Cinquieme a la dixieme:", fith_to_tenth)

#Task 2.1 ------------- 
v = "hello WORLD"
lower = v.lower()
#print(lower)
# methode chr() permet de recupérer un indice et automatiquement le mettre en lowercase

#Task 2.2 ----------
v = "tutu on the tuki-taka"
v_rep = v.replace("tutu", "tata")
#print(v_rep)

#Task 2.3 ---------------
#Fonction find() trouve la position de l'element dans une chaine de charactere

#string = "hello world"
#position = string.find("a")
#print(position)
print("--------------------")
#On trouve une position negative car il n'y a pas de "a" dans la chaine de charactere

#Task 2.4 ------------
p = "abcdefghij"
p[::-2][:5][::-1][3:] # "hj"
p[::-2] # "jhfdb"
p[:5] # "abcde"
p[::-1] # "jihgfedcba"
p[3:] # "defghij"



#Task 2.5 --------------

p ="thevelvetunderground"
#print(p[::-2][:5][::-1][3:])
#print(p[-3::2]) # Resultat 

#Task 2.6 --------------

#v = "Hello world"
#for _ in range(10):
    #print(v) 

#Task 2.7 ---------------
#print("Hello world"*10)

#Task 2.8 ---------------
s1 = "Hello"
s2 = 42
concat = s1 + str(s2)
#print(concat)

#Task 2.9 ---------------
string1 = "42"
string2 = "is"
string3 = "the answer"
#print("The string", string1, string2, string3 , "contains 16 caracter")

#Challenge 

string = "thE Cat's tactic wAs tO surpRISE thE mIce tHE gArden"
lower_string = string.lower()
wild = ["cat", "mice", "garden"]
nb = 0 

for words in wild:
    nb += lower_string.count(words)
    nb += lower_string.count(words[::-1])
    
#print(nb)

#Task 3.1 --------------
#username = input("Enter you name:")
#print ("Hello", username)

#Task 3.2 --------------
#username = input("Enter your name ")
#print ("Hello", username[0].capitalize()+username[1:])

#Task 3.3 ------------
#first_nbr = input("Right down your first number ")
#second_nbr = input("Right down your second number ")
#print("The sum of the two provided numbers is", int(first_nbr)+int(second_nbr))

#Task 3.4 -------------
#question = input("Enter your number ")
#print(type(int(question)))

#task 3.5 --------------
#first_str = "This is a test"
#second_str = "Is it possible to fly ?"
#third_str = "Good things come to those who never give up"

#first_split = first_str.split()
#second_split = second_str.split()
#third_split = third_str.split()

#print(first_split[0], second_split[0].lower(), third_split[0].lower())

#Task 3.6  ------------ 

car = [ ' ' , ',' , ':' , ';' , '.' , "'" , '-' , '!' , '?' ]
def frequence(text):
    dict = {}
    for letter in text:
        if letter not in dict:
            if letter not in car:
                dict[letter] = 1
            else:
                dict[letter] += 1
    return dict 

text = "Salut comment tu vas"

L = sorted(frequence(text).items(), key = lambda colonne: colonne[1], reverse = True)

for i in L:
    print('{} : {}'.format(i[0],i[1]))