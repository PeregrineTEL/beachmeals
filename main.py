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
	print "brunch folxxx: %s" % brunch

# now the question becomes, can I use the same variable if I just redefine it a bunch
# actually I think the question is will it keep looping the if var below?
# I don't think it will.

	if newIndex > 0:
		appender = friendForIndex[-1]
		dinner.append(appender)
		print "adding guy above to dinner"
		list.pop(friendForIndex)
		newIndex = newIndex - 1
		print "dinner folxxx: %s" % dinner

	if newIndex > 0:
		appender = friendForIndex[-1]
		breakfast.append(appender)
		print "adding guy above to breakfast"
		list.pop(friendForIndex)
		newIndex = newIndex - 1
		print "breakfast folxxx: %s" % breakfast

	if newIndex > 0:
		appender = friendForIndex[-1]
		snax.append(appender)
		print "adding guy above to snack duty"
		list.pop(friendForIndex)
		newIndex = newIndex - 1
		print "snaxfolxxx: %s" % snax

print "people on brunch: %s" % brunch
print "people on snax: %s" % snax
print "people on dinner: %s" % dinner
print "people on breakfast: %s" % breakfast 
