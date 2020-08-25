#input check whether entered digit or not
def num():
    num = ''
    while not num.isdigit() :
        num = input("Enter number: ")
    return int(num)

num1 = num()
num2 = num()
print('The addition gives: ',num1+num2)
print('The substraction gives: ',num1-num2)
print('The multiplication gives: ',num1*num2)
print('The division gives: ',num1/num2)