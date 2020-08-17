#SOLOLEARN PYTHON COURSE LESSON 2

#booleans, True and False are sensitive, always with mayus
x=True
print(2==3)
print(x)
#arithmetical operators != < > <= >= ==
print('x'!='y')
#if else statements
if 4>5:
    print('correcto')
else:
    print('incorrecto')
    if 'a'!='b':
        print('a is different than b')
    else:
        print('that\'s wrong')
#elif statement
num=-56
print(num)
if num<=50:
    print('the number is less or equal than 50')
elif num>=50:
    print('the number is greater or equal than 50')   
else:
    print('Please insert a valid number') 
#logical operators and, or , not
if (1==1) and (4>3):
    print('ok')
else:
    print('not ok')
    
#python functions same as the normal mathematical laws with priority for multipliactions and divisions 
#and also for the resolve of parenthesis and keys

# ~ is for the complement, // floor division, & bitwise and, ^ bitwise exclusive or, | bitwise or
# << >> left and right bitwise shift

#LISTS (ARRAYS IN JS OR C++)
lista=['puto', 'el que', 'lo lea']
print(lista[0])
print(lista[1])
print(lista[2])
#lists can have multiple types of variables inside them, including other lists
great_list=[0,'uno',2,['tres',4,'cinco']]
print(great_list[1])
print(great_list[3][0])#navigates inisde the list of the list
#strings can be indexed as lists
word='saludos'
print(word[3])
#data inside lists can be reasigned
lista[1]='cerdo el que'
print(lista)
#operations in lists
print(lista+['hoy y','siempre'])
nums=[1,2,3]
print(nums*3)#triplicates the list, if we want to multiply each element by 3, that must be by separated
#check if an item is in the list
print(1 in nums)
print(56 not in nums)
#.append method adds an item at the end of the list
nums.append(4)
print(nums)
#len method returns the size of the list
print(len(nums))
#.insert method lets us puta new item in any spot of the list
ix=2
nums.insert(ix, 69)
print(nums)
#the .index method returns the index of a occurrence of an item of the list
print(nums.index(69))

#WHILE LOOPS

#infinite loop
#while True:
#    print('it does not stop morty')

i=0
while True:
    i=i+1
    print(i)
    #continue #continue statement jumps to the begin of the cycle, instead of finishing it
    if i==5:
        print('stop it')
        break#stops the cycle
print('finished')

#FOR LOOPS

words = ["hello", "world", "spam", "eggs"]
for word in words:
  print(word + "!")
for e in range(0, 20, 2):#also remenber params range(start, stop, step)
    print(e)
