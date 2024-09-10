#Task 1.1
print(1+1);
print(30+12);
print(777+(-735));
print(1+2+3+5+7+11+13);

#Task 1.2
print(84-2);
print(0-(-42));
print((-6)*(-7));
print(2+5*8);
print((3+(3*4-2*2)*3-2)*2-3);

# Task 1.3
print(84/2); # Division entiers 
print(84//2);

#Task 1.4
#print(84/(8+(-3)+(-7)+2)); # Division par 0

#Task 2.1

res = 0
i = 1
while i < 10:
    res += int('1'*i)
    i = i +1
    print (res)


res = 0
for i in range(1,10):
    res += int('1'*i)
print(res)

#Task 2.2 
print(17**1024)

#Task 3.1
print(42%4)

#Task 3.2
num= 3
if num % 2 == 0:
    print('Odd')
else:
    print('Even') 

#Task 3.3

sum = 0
numbers = 123434565
for num in str(numbers) :
    sum += int(num)
print(sum)


#Task 3.4
print(int(12.24))
print(int(424242.8412))

#Task 3.5


a = 12.24
b = a - int(a)
print(b)

a = 424242.8412
b = a - int(a)
print(b)

 



#Challenge 
a = 12.24
b = a - int(a)
print (format(b, ('.2f'))) 

a = 424242.8412
b = a - int(a)
print (format(b, ('.2f'))) 

#Task 4.1

#precision = 1
#for _ in range(30):
#   print(1/precision)
#  precision += 2






    


