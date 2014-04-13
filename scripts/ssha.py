#!/usr/bin/env python3

# generates ssha1 password hashs for freeradius2

import hashlib
import base64
import os
import sys

if len(sys.argv) < 2:
    print("Usage: ssha username")
    sys.exit(1)

username = sys.argv[1]

password = base64.b64encode(os.urandom(32)) # base64 so we have a sane input
salt = os.urandom(32)

hash = hashlib.sha1()
hash.update(password)
hash.update(salt)

# concat digest and salt and base64 encode to get the password hash for the database
print("Configuration: " + username + "\tSSHA-Password := \""
        + base64.b64encode(hash.digest() + salt).decode("utf-8")
        + "\""
    )

print("User password: " + password.decode("utf-8"))

sys.exit(0)
