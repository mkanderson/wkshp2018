#!/usr/bin/env python

import digitalocean
import os
import time

token = '4846991f13b2f0336c189249c09975428dc15bca45fcac032c1e41f81ba609a0'
names = [
        'stan',
        ]
dns_domain = 'elegobox.com'
ids = []
for boxname in names:
    ssh_pubkey = open(os.path.expanduser('~/.ssh/id_rsa.pub'))
    mgr = digitalocean.Manager(token=token)
    token = token

    new_droplet = digitalocean.Droplet(
            token=token,
            name=boxname,
            region='fra1',
            image='debian-9-x64',
            size='1gb',
            ssh_keys=[1765340],
            tags=['rcs_workshop']
            )

    res = new_droplet.create()
    print res
    ids.append(new_droplet.id)

    # # action = digitalocean.Action(id=new_droplet.action_ids[0], token=token, droplet_id=new_droplet.id)
    # # action.load()
    # # action.wait(5)


    print "Creating new box %s with ID: %s" % (new_droplet.name, new_droplet.id)

for id in ids:
    droplet = digitalocean.Droplet.get_object(token, id)

    while (droplet.ip_address == None):
        droplet.load()
        print "Waiting for an ip..."
        time.sleep(1)


    print "IDs created: %s" % ids

    domobj = digitalocean.Domain.get_object(api_token=token, domain_name=dns_domain)
    print domobj


    domobj.create_new_domain_record(
            type='A',
            name=droplet.name,
            data=droplet.ip_address,
            )

    print "Droplet %s.%s created successfully with IP: %s" % (droplet.name, dns_domain, droplet.ip_address)
