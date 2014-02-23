import random

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
print "there are %s friends" % friendListSize

shuffledFriends = friends
random.shuffle(shuffledFriends)
# had a print statement here that printed out the shuffledfriends

# or should structure MEALS be a dict so that its keys can be called?
# OMG PROBABLY

brunch = []
snax = []
dinner = []
breakfast = []
meals = [brunch, snax, dinner, breakfast]

print meals

k = len(shuffledFriends)
while k > 0:
	for j in meals:
		appender = shuffledFriends[-1]
		j.append(appender)
		list.pop(shuffledFriends)
		k -= 1
		if k <= 0:
			print "brunch fixers: %s \n" % brunch
			print "snax fixers: %s \n" % snax
			print "dinner fixers: %s \n" % dinner
			print "breakfast fixers: %s \n" % breakfast
		elif k > 0:
			pass
		else:
			print "error"
