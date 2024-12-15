my_tuple=(1,2,3,[5,6])
my_tuple[3][0]=9
print(my_tuple) #   (1, 2, 3, [9, 6])
print((1,2,3)+(4,5,6))  #   (1, 2, 3, 4, 5, 6)
print(("repeat",)*3)    #('repeat', 'repeat', 'repeat')