#Pass Array as an argument in class and implement element wise calculator using Classes

#CLASS
class calci():
    def __init__(self,a,b):
        self.a = a
        self.b = b

    def add(self):
        self.add = []
        for i in range(len(self.a)):
            self.add.append(a[i]+b[i])
        print(self.add)

    def sub(self):
        self.sub = []
        for i in range(len(self.a)):
            self.sub.append(a[i]-+b[i])
        print(self.sub)
    
    def pro(self):
        self.pro = []
        for i in range(len(self.a)):
            self.pro.append(a[i]*b[i])
        print(self.pro)

    def div(self):
        self.div = []
        for i in range(len(self.a)):
            self.div.append(a[i]/b[i])
        print(self.div)




#List input
a = []
b = []
#List 1 input
print('Enter items for Array 1: ')
for i in range(0,5):
    ele = int(input('Enter the {} element: '.format(str(i))))
    a.append(ele)
#List 2 input
print('Enter items for Array 2: ')
for i in range(0,5):
    ele = int(input('Enter the {} element: '.format(str(i))))
    b.append(ele)

cal = calci(a,b)
#infinite loop depending on user Input
c = 0
while c < 6:
    c = int(input('Enter 1 for addition\nEnter 2 for subtraction\nEnter 3 for multiplication\nEnter 4 for division\nEnter 5 to exit\n'))
    if c == 1:
        cal.add()
        continue
    elif c == 2:
        cal.sub()
        continue
    elif c == 3:
        cal.pro()
        continue
    elif c == 4:
        cal.div()
        continue
    else:
        break
print('Program Terminated!!')