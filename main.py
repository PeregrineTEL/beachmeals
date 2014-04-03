# Creative Commons 2014 Rachel Kelly
# A way to assign meal preparation to randomized 
# groups of people

import random

mealchoice = 1
meallist = []
while mealchoice == 1:
	print "what meals? "
	whichmeal = raw_input("> ")
	newmealname = [whichmeal]
	meallist.append(newmealname)
	print "add another? y/n "
	qchoice = raw_input("> ")
	if qchoice == "y":
		mealchoice = 1
	else:
		break

print meallist

friends = []
print "how many friends "
howmany = int(raw_input("> "))

i = 0
while i < howmany:
	print "who is the friend "
	friend = raw_input("> ")
	friends.append(friend)
	i = i + 1

print "here's all the friends: "
print friends
friendListSize = len(friends)
print "there are %s friends, here they are shuffled: " % friendListSize

shuffledFriends = friends
random.shuffle(shuffledFriends)
print "%s \n" % shuffledFriends

k = len(shuffledFriends)
while k > 0:
	for j in meallist:
		appender = shuffledFriends[-1]
		j.append(appender)
		mealname = str(j)
		list.pop(shuffledFriends)
		k = k - 1
		if k > 0:
			pass
		elif k <= 0:
			for l in meallist:
				print l
			print "good job now make the food you dooks"
			exit(0)
