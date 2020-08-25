def add(x,y):
    add_list = []
    add_mean = 0
    for i in range(0,len(x)):
        add_list.append(x[i]+y[i])
        add_mean += (x[i]+y[i])
    print('The addition list gives: ',add_list)
    print('The mean result of addition is: '+str(add_mean/5))
    var_add = sum((xi - sum(add_list)/5) ** 2 for xi in add_list) / 5
    print('The variance for addition the result is: ',var_add)
def sub(x,y):
    sub_list = []
    sub_mean = 0
    for i in range(0,len(x)):
        sub_list.append(x[i]-y[i])
        sub_mean += (x[i]-y[i])
    print('The subtraction list gives: ',sub_list)
    print('The mean result of subtraction is: '+str(sub_mean/5))
    var_sub = sum((xi - sum(sub_list)/5) ** 2 for xi in sub_list) / 5
    print('The variance for the subtraction result is: ',var_sub)
def pro(x,y):
    pro_list = []
    pro_mean = 0
    for i in range(0,len(x)):
        pro_list.append(x[i]*y[i])
        pro_mean += (x[i]*y[i])
    print('The multiplication list gives: ',pro_list)
    print('The mean result of multiplication is: '+str(pro_mean/5))
    var_pro = sum((xi - sum(pro_list)/5) ** 2 for xi in pro_list) / 5
    print('The variance for the multiplication result is: ',var_pro)
def div(x,y):
    div_list = []
    div_mean = 0
    for i in range(0,len(x)):
        div_list.append(x[i]/y[i])
        div_mean += (x[i]/y[i])
    print('The division list gives: ',div_list)
    print('The mean result of division is: '+str(div_mean/5))
    var_div = sum((xi - sum(div_list)/5) ** 2 for xi in div_list) / 5
    print('The variance for the division result is: ',var_div)

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
c = 0

while c < 6:
    c = int(input('Enter 1 for addition\nEnter 2 for subtraction\nEnter 3 for multiplication\nEnter 4 for division\nEnter 5 to exit\n'))
    if c == 1:
        add(a,b)
        continue
    elif c == 2:
        sub(a,b)
        continue
    elif c == 3:
        pro(a,b)
        continue
    elif c == 4:
        div(a,b)
        continue
    else:
        break