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

brunch = []
snax = []
dinner = []
breakfast = []

