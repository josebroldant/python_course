#SOLOLEARN PYTHON COURSE LESSON 4

#ERROR HANDLING
try:
   num1 = 7
   num2 = 0
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