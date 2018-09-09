#!/usr/bin/python

### Code used to create droplet


import digitalocean

manager = digitalocean.Manager(token='XXXXXXXXXX')
keys = manager.get_all_sshkeys()

droplet = digitalocean.Droplet(token='XXXXXXXXXXXXXXXX',
				name='mywebsite',
				region='nyc1',
				image='34487567',
				size_slug='s-1vcpu-1gb',
				backups=True,
				ssh_keys=keys
				)

droplet.create()


