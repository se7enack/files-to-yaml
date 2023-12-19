#!/usr/bin/env python3

import base64
import os

file = open('pngs.yaml', 'w')
file.write('---\n')
with os.popen('ls *.png') as pipe:
    for line in pipe:
        x = line.strip()
        with open(x, "rb") as file:
            encoded_string = base64.b64encode(file.read())
            file = open('pngs.yaml', 'a')
            file.write(x + ': ' + encoded_string.decode('ascii')+ '\n')
file.close()
