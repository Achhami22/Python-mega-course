print('Hello Hex')

#Enter first number:
#Enter second number:
#Enter 1 for addition,2 for substraction,3 for multiplication,4 for division and 5 for exist.
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def div(x,y):
    return x/y

while(True):
 num1= float(input('Enter the first number: ')) 
 num2= float(input('Enter the second number: ')) 
 print('Enter:\n1 for Addition\n2 for Subtraction\n3 for multiplication\n4 for division')
 opt= int(input('Enter your choice: '))
 if opt==1:
    res= add(num1,num2)
    print('The sum is ', res)
 if opt==2:
    res= sub(num1,num2)
    print('The difference is ', res)
 if opt==1:
    res= mul(num1,num2)
    print('The multiplication is ', res)
 if opt==1:
    res= div(num1,num2)
    print('The division is ', res)

 if opt==5:
        print('Thank You')
        break
