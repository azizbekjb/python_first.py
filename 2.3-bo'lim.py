"""
#2.3-bo'lim 4-namuna:Birxillikkni tekshirish
x1 = 5
y1 = 5
x2 = "Hello"
y2 = "Hello"
x3 = [1,2,3]
y3 = [1,2,3]
#Natija : False
print(x1 is not y1)
#Natija:True
print(x2 is y2)
#Natija: False
print(x3 is y3)
"""


#5-namuna:A'zolikni tekshirish
"""
x='Hello Tutorials.uz'
y={1:'a',2:'b'}#Bu lug'at
#Natija: True
print('H' in x)
#Natija: True
print('hello' not in x)
#Natija: True
print(1 in y)
#Natija: False
print('a' in y)
"""
#2.5-bo'lim:Satrlar
x='\t Bu satr abzasdan boshlanadi'
y='\n bu satr yangi qatordan boshlaydi'
print(x,y)
z="E'lon(bu yerda bekslesh ishlatilmaydi"
d='E\nlo (bu yerda beksleshsiz ish bitmaydi)'
e="Bu \"belgini ekranlashtirish shart"
f= 'Bu "belgini yolgiz sihlatish mumkin'
print(z,d,e,f)