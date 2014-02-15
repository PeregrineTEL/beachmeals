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
friendForIndex = friends
brunch = []
snax = []
dinner = []
breakfast = []

#so here I'll just make each list append a random friend
#there is CERTAINLY a better way to do this, probably
#involving a big list of lists, like, "pick a list & add
#the friend to it,"
#### but the issue there is that the pigeonhole will fail!
#### and it won't be even!  god, I guess I could do some
#### kind of gnarly conditional "if len(brunch) > len(snax)"
#### and every possible combination for every random friend
#### choice add, oh my god that is a terrible idea ok no.

while newIndex > 0:
	friendChoice = random.choice(friendForIndex)
	print "adding %s to brunch which already contains %s" % (friendChoice, brunch)
	brunch.append(friendChoice)
	friendForIndex = friendForIndex - friendChoice
	print "adding %s to snax which already contains %s" % (friendChoice, snax)
	snax.append(friendChoice)
	friendForIndex = friendForIndex - friendChoice
	print "adding %s to dinner which already contains %s" % (friendChoice, dinner)
	dinner.append(friendChoice)
	friendForIndex = friendForIndex - friendChoice
	print "adding %s to breakfast which already contains %s" % (friendChoice, breakfast)
	breakfast.append(friendChoice)
	friendForIndex = friendForIndex - friendChoice
