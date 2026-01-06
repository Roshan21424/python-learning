try:
  
 # this part contains the code which may occour error if 
 # it is excecuted
 a = int(input('Enter a number: '))
 b = int(input('Enter a number: '))

 c = a/b
 print('result: ', c)

 #this part is dipalyed if above code gives error"""
except ZeroDivisionError:
 print('value of b can not be zero!')
except ValueError:
 print('invalid input!')
else:
 #if error not occured this will displayed
 print('No exception occurred!!!')
finally:
 #this will execute in all situations
 print('This is executed compulsory!!!')
