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
print shuffledFriends

k = len(shuffledFriends)
while k > 0:
	for j in meallist:
		appender = shuffledFriends[-1]
		j.append(appender)
		list.pop(shuffledFriends)
		k = k - 1
		if k > 0:
			pass
		elif k <= 0:
			# print "%s fixers: %s \n" % (***1stmealname??***, appender)
			print "brunch fixers: %s \n" % brunch
			print "snax fixers: %s \n" % snax
			print "dinner fixers: %s \n" % dinner
			print "breakfast fixers: %s \n" % breakfast
			print "good job now make the food you dooks"
			exit(0)
		else:
			break
