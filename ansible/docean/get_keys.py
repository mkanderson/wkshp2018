#!/usr/bin/env python

import digitalocean
import os

token = '425daf680847a06e41dbf0d09ab8f8d2bc34f04f2f80fa1646d6392c45848985'

mgr = digitalocean.Manager(token=token)
keys = mgr.get_all_sshkeys()

print keys
