#!/usr/bin/env python3

import base64
import sys
import os
import yaml


def png2yaml():
    file = open('png.yaml', 'w')
    file.write('---\n')
    with os.popen('ls *.png') as pipe:
        for line in pipe:
            x = line.strip()
            with open(x, "rb") as file:
                encoded_string = base64.b64encode(file.read())
                file = open('png.yaml', 'a')
                file.write(x + ': ' + encoded_string.decode('ascii')+ '\n')
    file.close()


def yaml2png():
    with open('png.yaml', 'r') as f:
        data = yaml.full_load(f)
        for key in data:
            value = data.get(key)
            value_bytes = value.encode('utf-8')
            with open(key, 'wb') as file_to_save:
                decoded_image_data = base64.decodebytes(value_bytes)
                file_to_save.write(decoded_image_data)
                file_to_save.close()
    f.close()


errmsg = "\n  Expects one of these arguments: png2yaml, yaml2png\n"
try:
    option = sys.argv[1]
    if option == "yaml2png":
        print(option)
        yaml2png()
    elif option == "png2yaml":
        print(option)
        png2yaml()
    else:
        print(errmsg)
except:
    print(errmsg)
