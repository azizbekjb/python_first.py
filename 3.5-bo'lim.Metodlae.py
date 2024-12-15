x=[1,2,3,4,4,4,5]
print(x.index(2)) # 2 elementi 1-indexda joylashgan
print(x.count(4))# 4 elementi soni 3 ta
x=x+[9,6,7]
x.sort() #O'sish tartibida saralaydi.
print(x) #Natija: [1, 2, 3, 4, 4, 4, 5, 6, 7, 9]
x.reverse()# Teskari tartibda saralaydi
print(x) #Natija: [9, 7, 6, 5, 4, 4, 4, 3, 2, 1] 
print(x)