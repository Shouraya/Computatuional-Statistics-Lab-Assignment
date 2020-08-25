a = []
b = []
add_list = []
sub_list = []
pro_list = []
div_list = []
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
#printing addition,substraction,multiplication and division result in list form
for i in range(0,5):
    add_list.append(a[i]+b[i])
    sub_list.append(a[i]-b[i])
    pro_list.append(a[i]*b[i])
    div_list.append(a[i]/b[i])
var_add = sum((xi - sum(add_list)/5) ** 2 for xi in add_list) / 5
var_sub = sum((xi - sum(sub_list)/5) ** 2 for xi in sub_list) / 5
var_pro = sum((xi - sum(pro_list)/5) ** 2 for xi in pro_list) / 5
var_div = sum((xi - sum(div_list)/5) ** 2 for xi in div_list) / 5
#addition
print('\nThe addition of the entered lists gives: ', add_list)
print('The mean vector for addition result is: ' + str(sum(add_list)/5)) 
print('The variance for addition the result is: ',var_add)
#subtraction
print('\nThe substraction of the entered lists gives: ', sub_list) 
print('The mean vector for subtraction result is: ' + str(sum(sub_list)/5))
print('The variance for the subtraction result is: ',var_sub)
#multiplication
print('\nThe multiplication of the entered lists gives: ', pro_list)
print('The mean vector for multiplication result is: ' + str(sum(pro_list)/5))
print('The variance for the multiplication result is: ',var_pro)
#division
print('\nThe division of the entered lists gives: ', div_list)
print('The mean vector for division result is: ' + str(sum(div_list)/5))
print('The variance for the division result is: ',var_div)