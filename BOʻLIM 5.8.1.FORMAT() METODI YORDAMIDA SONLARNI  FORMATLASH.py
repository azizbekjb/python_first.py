#   1-namuna:Sonlarni formatlashning soddda usuli:
#       butun sonli argumentlar:
print("This number is:{:d}".format(123))
#Natija:    This number is:123

#       kasr sonli argumentlar
print("The float number is:{:f}".format(11234.56789))
#Natija:    The float number is:11234.567890

#       ikkilik,sakkizlik va o'n oltilik sonlar
print("Bin: {0:b}, Oct: {0:o} and Hex: {0:x}".format(123))
#Natija:   Bin: 1111011, Oct: 173 and Hex: 7b


#   2-namuna:Butun va kasr sonlarni qo'shimcha bilan formatlash
#       minimum kenglikdagi butun sonlar
print("{:5d}".format(12))
#Natija:    "   12"

#        to’ldirilayotgan o’lchamdan katta bo’lgan sonlar uchun kenglik ishlamaydi
print("{:2d}".format(1234))
#Natija:    1234

#       Kasr sonlarni to'ldirish:
print("{:8.3f}".format(12.5657))
#Natija:    " 12.566"

#       nol bilan to'ldirilishi mumkin bo'lgan minimum kengliklar
print("{:05d}".format(12))
#Natija:    00012

#       kasr sonlarni 0 bilan to'ldirish
print("{:08.3f}".format(12.345))
#Natija:   0012.345


#   3-namuna:ishorali sonlarni formatlash
#       + ishorasini ko'rsatish
print("{:+f} {:+f}".format(12.34, -12.34))
#Natija:    +12.340000 -12.340000

#       faqat - ishorasini ko'rsatish
print("{:-f} {:-f}".format(12.34,-12.34))
#Natija:    12.340000 -12.340000

#       + ishorasini bo'shliqqa almashtirish
print("{: f} {: f}".format(12.34, -12.34))
#Natija:    12.340000 -12.340000


#       Sonlarning joylashuvuni tartiblash
#       4-namuna:Sonlarni chap,o'ng va markaziy o'rinlarda formatlash
#   O'ngga formatlash
print("{:5d}".format(12))
#Natija:    "   12"

#   Markazga formatlash
print("{:10.3f}".format(12.3456))
#Natija:    12.346

#   chapga nol bilan to'ldirib formatlash
print("{:<05d}".format(12))
#Natija:    12000

#   kasr sonlari markazga   formatlash
print("{:=8.3f}".format(-12.2346))
#Natija:    - 12.235
