#   1)Satrlar ustida amallar.Birlashtirish
str = 'Hello'
str1 = 'World'
str+=str1
print(str)
#   ikkinchi satrni 3 marta chop etish
print(str1*3)
#   2)Satr bo'yicha iteratsiya qilish
count = 0
for letter in "Hello World":
    if (letter == 'l'):
        count+=1
print(count)

str2 = "Mening satrim"
print(['m' for x in str2 if 'm' in str2])

#   4)Satr bilan ishlydigan funksiyalar
str3 = 'cold'
list_enumerate = list(enumerate(str3))
print('list(enumerate(str3)):',list_enumerate)
#Natija: [(0, 'c'), (1, 'o'), (2, 'l'), (3, 'd')]
#satr uznligi:
print(len(str3))