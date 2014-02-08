from random import *

friends = []
i = 0

print "how many friends "
number = raw_input("> ")

while i < number:
  print "who is the friend "
	friend = raw_input("> ")
	friends.append(friend)
	print friends
	print "%s left to input" % number
	print i
	i += 1
	print i

print "here's all the friends: "
print friends

brunch = []
snax = []
dinner = []
breakfast = []
