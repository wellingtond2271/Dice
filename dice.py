# Name:Damien Wellington
# Period 4th
# Dice Rolling Simulator
import random

rolls = int(input("How many rolls?"))
 
aa = 0
ab = 0
ac = 0
ad = 0
ae = 0
af = 0
x = 1

while x <= rolls:
 	rand = random.randint(1,6)
 	print("roll numbers:" + str(x) + "rolled a" + str(rand))
 	if rand == 1:
 		aa = aa +1
 	elif rand == 2:
 		ab = ab +1
 	elif rand == 3:
 		ac = ac + 1
 	elif rand == 4:
 		ad = ad +1
 	elif rand == 5:
 		ae = ae +1
 	else:
 		af = af +1

 	x = x + 1
print("number of rolls = " + str(x-1))

print("number of 1s = " + str(aa))
print("number of 2s = " + str(ab))
print("number of 3s = " + str(ac))
print("number of 4s = " + str(ad))
print("number of 5s = " + str(ae))
print("number of 6s = " + str(af))

Z = 100/(int(aa)+int(ab)+int(ac)+int(ad)+int(ae)+int(af))
print("Percent of 1s = " + str(aa*Z)+'%')
print("Percent of 2s = " + str(ab*Z)+'%')
print("Percent of 2s = " + str(ac*Z)+'%')
print("Percent of 2s = " + str(ad*Z)+'%')
print("Percent of 2s = " + str(ae*Z)+'%')
print("Percent of 2s = " + str(af*Z)+'%')