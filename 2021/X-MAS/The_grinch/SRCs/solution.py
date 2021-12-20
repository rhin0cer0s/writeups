#! /usr/bin/env python3

# Form1.what <> secret
secret = [150, 172, 240, 25, 157, 250, 202, 61, 162, 237, 147, 118, 224, 175, 202, 48, 161, 222, 212, 43, 145, 232, 201, 103, 179]

# Known plain text
knownText = "X-MA"

# Compute the key from the known text
# Form1.k <> key
key = []
for idx, char in enumerate(knownText) :
    key.append(ord(char) ^ secret[idx])

# Reveal the secret
output = ""
for idx, value in enumerate(secret) :
    output += chr(value ^ key[idx % 4])
print("Flag : {}".format(output))