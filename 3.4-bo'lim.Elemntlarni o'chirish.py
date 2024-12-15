"""my_list=['p','r','o','b','l','e','m']
del my_list[2]#bitta elementni o'chirish
print(my_list) #Natija :['p', 'r', 'b', 'l', 'e', 'm']
#bir nechta elementni o'chirish
del my_list[1:5]# 1-indexdan 5-indexgacha o'chiradi
print(my_list) #Natija :['p', 'm']
#Ro'yxatni to'liq o'chirish
del my_list
print(my_list)"""

"""
my_list=['p','r','o','b','l','e','m']
my_list.remove('p')
print(my_list) # Natija: ['r', 'o', 'b', 'l', 'e', 'm']

print(my_list.pop(1)) # Natija :'o'
print(my_list) #Natija: ['r', 'b', 'l', 'e', 'm']
print(my_list.pop()) #Natija: 'm'
print(my_list) #Natija:['r', 'b', 'l', 'e']

#Butunlay tozalash
print(my_list.clear()) #Natija: []
"""

my_list=['p','r','o','b','l','e','m']
my_list[2:3]=[] #'o' elementni o'chiradi
print(my_list)
my_list[2:5]=[]
print(my_list)