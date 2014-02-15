import random

friends = []
print "how many friends "
howmany = int(raw_input("> "))

i = 0
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


friendForIndex = friends
random.shuffle(friendForIndex)
print friendForIndex
friendForIndex[-1]

brunch = []
snax = []
dinner = []
breakfast = []

newIndex = friendListSize
while newIndex > 0:

	appender = friendForIndex[-1]
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
