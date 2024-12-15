pow2=[2**x for x in range(10)]
print(pow2)
#Natija: [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]



pow2=[]
for x in range(10):
    pow2.append(2**x)
print(pow2)
print([x+y for x in ['Python ','C '] for y in ['Language','Programming']])