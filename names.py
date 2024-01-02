#names list work
name=['righathi','ruto','masika','mudavadi']
#print (names[0])
#print (names[1])
#print (names[2])
#print (names[3])

#adding some messages to the created names
greetings= 'hello dear '
#message=(greetings +name[0]/n)
#print (greetings +name[0].title())
#print (greetings +name[1].title())
#print (greetings +name[2].title())
#print (greetings +name[3].title())

#own assignment on lists
cars = ['honda','bugati','maserati','camry',]
#append
cars.append ('civic')
#insert
cars.insert(3, 'sportage')
message= 'i woul like to own a '
print (cars)
#sort
cars.sort()
#reverse
cars.reverse()
#pop
cars.pop(0)
popped= cars.pop(0)

print (message.title()+ popped.title()+'.\n')
#the for loop
for car in cars:
   #print(car)
   print (message.title()+ car +'.\n')
   #message after for loop
print('this are all great cars'.title())