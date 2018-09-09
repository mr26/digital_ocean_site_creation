#!/usr/bin/python


### prints all droplets



import digitalocean

manager = digitalocean.Manager(token='38843b913b1b1c864bacc6c5959a0654e72349bb89f2728d9750e38ca9ef2188')


for i in manager.get_all_droplets():
	print(i)


