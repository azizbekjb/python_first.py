'''#   Standart belgilash
default_order = "{}, {} and {}".format('John','Bill','Sean')
print('\n--- Deault Order ---')
print(default_order)
#Natija:     John, Bill and Sean
#   pozitsion argumentlardan foydalanib tartiblash
positional_order = "{1}, {0} and {2}".format('John','Bill','Sean')
print('\n--- Positional Order ---')
print(positional_order)
#Natija:    Bill, John and Sean

#   Nomlanga argumentlardan foydalanib tartiblash
keyword_order = "{s}, {b} and {j}".format(j='John',b='Bill',s='Sean')
print('\n--- Keyword Order ---')
print(keyword_order)
#Natija:    Sean, Bill and John
'''

'''
#   Butun sonlarni formatlash
b="{0} sonining ikkilik sanoq tizimidagi ko'rinishi - {0:b}".format(12)
print(b)
#Natija:12 sonining ikkilik sanoq tizimidagi ko'rinishi - 1100

#   Kasrlarni formatlash
k = "Eksponent ko'rinishi: {0:e}".format(1566.345)
print(k)
#Natija:    Eksponent ko'rinishi: 1.566345e+03

#   Yaxlitlash
c = "Bir taqsim uch: {0:.3f}".format(1/3)
print(c)
#Natija:    Bir taqsim uch: 0.333

#   Satrlarni o'rnini belgilash
S = "| {:<10} | {:^10} | {:>10} ".format('bread','butter','Ham')
print(S)
'''




#   1-namuna:   Standart, pozitsion va nomlangan argumentlar uchun asosiy formatlash namunalari"
#   Standart argumentlar
print("Hello mister {}, your balance is: {}".format("Azizbek",439000))

#   pozitsion argumentlar
print("Hello mister {0}, your balance is: {1}".format("Azizbek",439000))

#   Nomlangan argumentlar
print("Hello mister {name}, your balance is: {blc}".format(name = "Azizbek",blc = 439000))

#   Aralash argumentlar
print("Hello mister {0}, your balance is: {blc}".format("Azizbek",blc = 439000))

#   2-namuna:   Bo'shliq o'rnini to'ldirish va joylashuviga ko'ra formatlar
#   Chapga joylashtirish
print("{:5}".format("cat"))

#   O'ngga joylashtirish
print("{:>5}".format("cat"))

#   Satrni markazga joylashtirish
print("{:^5}".format("cat"))

#   hamda "*" belgisi bilan to'ldirish
print("{:*^5}".format("cat"))