#Task 1.1 ------------------ 

#l = [1,2,3,4,5]

#Task 1.2 ------------------

#print(l[-1])

#Task 1.3 ------------------

#l.append(6)

#Task 1.4 ------------------

#print(l)

#Task 1.5 ------------------

#l.remove(6)
#print(l)

#Task 1.6 ------------------

#l.insert(0,13)
#print(l)

#Task 1.7 ------------------

#print(l[2:5])

#Task 1.8 ------------------

#l = [1,2,3,4,5]
#l_2= []
#l.reverse()
#l_2.extend(l)
#print(l_2)

#Task 1.9 ------------------

#print(l_2[::2])

#Task 1.10 ------------------

#l_3 =[]
#for i in range(0,17):
#    i += 1
#    l_3.append(i)
#print(l_3)

#Task 1.11 ------------------

#my_first_list = [4,5,6]
#my_second_list = [1,2,3]
#my_first_list.extend(my_second_list)
#print(my_first_list)

#Same with

#my_first_list = [4,5,6]
#my_second_list = [1,2,3]
#my_first_list = [*my_first_list, *my_second_list]
#print(my_first_list)

#Task 2.1 ------------------


#l = []
#for i in range(0,10):
#    i += 1
#    l.append(i)
#print(l)

#r=1
#for element in l:
#    r *= element
#print(r)

#Task 2.2 ----------------

#print([x + 10 for x in [3,2,6,7,1,4]])

#Task 2.3 ----------------

#print(list(map(lambda x: x*x, [3,2,6,7,1,4])))
# Multpilie l'element par lui meme

#task 2.4 ---------------

#l = []
#for i in range(0,10):
#    i += 1
#    l.append(i)
#print(l)

#print(min(l), max(l))

#Task 2.5 --------------

#print(l[:6])

#Task 2.6 --------------

#l.reverse()
#print(l)

#Task 2.7 --------------
#print([x // 2 if x %2 == 0 else x *2 for x in [42,3,4,18,3,10]]) 
# Si le nombre est divisible par 2 on le divise par 2 sinon on multiplie par 2

#Task 2.8 ---------------
#print(list(filter(lambda x : x > 10, [42, 3, 4, 18, 3, 10])))
# Affiche les elements superieur à 10

#Task 2.9 ---------------

#print([*enumerate([42,3,4,18,10])])
#Affiche la position de l'element et sa valeur entre parentheses

#Task 2.10 ---------------
#first_name = ["Jackie", "Bruce", "Arnold", "Sylvester"]
#last_name = ["Stallone", "Scharzenegger", "Willis", "Chan"]

#magic = [*zip(first_name, last_name[::-1])]

#print(magic[0])
#print(magic[3])
#print(magic[1][0])
#print(magic[0][1])
#print(magic[2])

# Rassemble les liste entre elle en inversant la seconde

#Challenge 

#l = []
#for i in range(0,100000):
#    i += 1
#    l.append(i)
#print(l)

#Task 3.1 / 3.2 --------------------

student = {
    "name" : "Vincent",
    "academic_year" : "2024",
    "units" : [
        {
            "name" : "Web Developpement",
            "credits" : 3,
            "grade" : "A"
        }
        ,
        {
            "name" : "Java",
            "credits" : 2,
            "grade" : "B" 
        }
        ,
        {
            "name" : "network_and_system_administration",
            "credits" : 1,
            "grade" : "C" 
        }       

    ]
    
}

#Task 3.3 -------------------

grade_weight_mapping = {"A":4,"B":3,"C":2,"D":1,"E":0}

x=0
y=0
credits = 0
for unit in student["units"]:
    x += unit["credits"]
    y = grade_weight_mapping[unit["grade"]]
    total_credit = x 
    student["total_credit"] = total_credit
    credits = credits + y
print(credits)

p = credits / len(student['units'])

print(p)
    