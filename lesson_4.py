"""
SOLOLEARN PYTHON COURSE LESSON 4
"""

#EXCEPTIONS


try:
   num1 = 7
   num2 = 1
   print (num1 / num2)
   print("Done calculation")
#SPECIFIES ERROR TYPE
except ZeroDivisionError:
   print("An error occurred")
   print("due to zero division")
except (ValueError, TypeError):
   print("Error occurred")
#FOR ANY EXCEPTION THAT HAS OCURRED
except:
   print("An error occurred")
#FOR RUNNING THE CODE EVEN IF A LOT OF EXCEPTIONS HAD OCURRED
finally:
   print("This code will run no matter what")



#RAISING EXCEPTIONS

print(1)
raise ValueError
print(2)
#CUSTOM RAISE ERRORS
name = "123"
raise NameError("Invalid name!")
#RAISE CAN BE USED ALONE INSIDE EXCEPT BLOCKS
try:
   num = 5 / 0
except:
   print("An error occurred")
   raise


#ASSERTIONS ARE ANIITY CHECKS THAT CAN BE TURNED ON OR OFF DURING CODING


print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)
#CUSTOM ASSERTS
temp = 36
assert (temp >= 0), "Colder than absolute zero!"


#USING FILES


# write mode
open("text.txt", "w")

# read mode
open("text.txt", "r")
open("text.txt")

# binary write mode
open("text.txt", "wb")


file = open("text.txt", "r+")
file.write("This has been written to a file")
print(file.readlines())
file.close()
#print(file.read(250))#reads an specific number of bytes of the file

#after reading all file, if you try to read it again it will return an empty string list

msg="primera linea"
file = open("newfile.txt", "w")
amount_written = file.write(msg)#this method returns the number of bytes written
print(amount_written)
file.close()

#good practices when using files
try:
   f = open("newfile.txt")
   print(f.read())
finally:
   f.close()

#using with statement
with open("newfile.txt") as f:#this treats the file as f variable
   print(f.read())


