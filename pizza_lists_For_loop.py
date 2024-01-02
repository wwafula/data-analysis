pizzas=['pepino','pepperoni','vegetable','vegan']
for pizza in pizzas:
    message='i love '
    print(message + pizza +'\n')
print('i really love pizza')

#assignment 
mammals=['cat','cheetah','lion','tiger']
for mammal in mammals:
  message=' has paws and whiskers '
  print ( mammal + message + '.\n')
print('they all can be referred to as cats')

#copying a list
my_pizza=['pepino','pepperoni','vegetable','vegan']
friend_pizza=my_pizza[:]
print ('my favorite pizza are:')
print(my_pizza)

print('my friends favorite pizza are:')
print(friend_pizza)

#prove they are not same list
my_pizzaz=['pepino','pepperoni','vegetable','vegan']
friend_pizzaz=my_pizzaz[:]
my_pizzaz.append('lickys')
friend_pizzaz.append('lambas')
for pizza in my_pizzaz:
 print(my_pizza)

print('my friends favorite pizza are:')
print(friend_pizza)

