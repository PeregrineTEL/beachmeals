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

k = friendListSize
for j in meals:
	appender = shuffledFriends[-1]
	j.meals(appender)
	list.pop(shuffledFriends)
	print meals
	# ha ha shit this exploded
