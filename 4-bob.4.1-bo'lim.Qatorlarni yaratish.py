#Qatorlarni har xil turlari
#   1)Bo'sh qator:
my_tuple=()
print(my_tuple) #()
#   2)Butun sonli qator:
my_tuple=(1,2,3)
print((my_tuple)) #(1, 2, 3)
#   3)Turli ma'lumot turiga ega qatorlar
my_tuple=(1,4.6,"Hello")
print(my_tuple) #(1, 4.6, 'Hello')
#   4)Ichma ich qatorlar
my_tuple=("mouse",[1,2,3],(4,5,6))
print(my_tuple) #('mouse', [1, 2, 3], (4, 5, 6))

#Qatorlarni qadoqlash
my_tuple=3,4.6,"dog"
print(my_tuple) #(3, 4.6, 'dog')
#Qatorlarni qadoqdan chiqarish
a,b,c=my_tuple
print(a) #3
print(b) #4.6
print(c) #'dog'

# 1 ta elementli qator hosil qilish
my_tuple=("hello")
print(type(my_tuple)) #<class 'str'>
my_tuple=("hello",)
print(type(my_tuple)) #<class 'tuple'>
#qavslar ixtiyoriy bo'lishi mumkin
my_tuple="hello",
print(type(my_tuple)) #<class 'tuple'>
