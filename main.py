import random

friends = []
i = 0

print "how many friends "
howmany = int(raw_input("> "))

while i < howmany:
	print "who is the friend "
	friend = raw_input("> ")
	friends.append(friend)
	print friends
	i = i + 1

print "here's all the friends: "
print friends
friendListSize = len(friends)
print "there are %s friends" % friendListSize
#so now all the friends are in.  this can probably be shortened
#NOW I want to lump them all into meal assignments

newIndex = friendListSize
friendForIndex = []
friendForIndex = random.shuffle(friends)
print friendForIndex
friendForIndex[-1]
brunch = []
snax = []
dinner = []
breakfast = []


while newIndex > 0:

	friendForIndex[-1]
	brunch.append(appender)
	print "adding guy above to brunch"
	list.pop(friendForIndex)
	newIndex = newIndex - 1
	print brunch

	if newIndex > 0:
		print friendForIndex[-1]
		appender = friendForIndex[-1]
		dinner.append(appender)
		print "adding guy above to dinner"
		list.pop(friendForIndex)
		newIndex = newIndex - 1
		print dinner
