#!/usr/bin/python

### code used to import SSH key from workstation/jumpbox to droplet


from digitalocean import SSHKey

user_ssh_key = open('/home/myuser/.ssh/id_rsa.pub').read()

key = SSHKey(token='XXXXXXXXX',
	     name='my_website_key',
	     public_key=user_ssh_key )
		
	    

key.create()
