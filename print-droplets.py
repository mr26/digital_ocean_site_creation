#!/usr/bin/python


### prints all droplets



import digitalocean

manager = digitalocean.Manager(token='')


for i in manager.get_all_droplets():
	print(i)


