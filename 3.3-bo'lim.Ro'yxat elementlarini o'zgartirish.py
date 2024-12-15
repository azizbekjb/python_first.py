#Ro'yxatdagi xato elementlarni to'g'irlymiz
x=[1,2,3,4]
x[0]=0
print(f"natija {x}") #[0, 2, 3, 4]
x[1:4]=[3,5,7]
print(x)#[0, 3, 5, 7]
odd=[1,3,5]
odd.append(7)
print(odd)#[1, 3, 5, 7]
#bir nechta element qo'shish
odd.extend([9,11,13])
print(odd)#[1, 3, 5, 7, 9, 11, 13]
print(odd+[2,4,6,8])#[1, 3, 5, 7, 9, 11, 13, 2, 4, 6, 8]
print(["a"]*3)#['a', 'a', 'a']
#istalgan joyiga kiritish
y=[1,9]
y.insert(1,3)
print(y)#[1, 3, 9]
#y.insert(0,4)
#print(y)#[4, 1, 3, 9]
y[2:2]=[5,7]
print(y)
