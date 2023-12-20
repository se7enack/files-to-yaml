#!/usr/bin/env python3

import base64
import sys
import os
import yaml
import time


filesdir = "files"
yamlfile = (filesdir + "/inventory.yaml")


def setup():
    os.popen('mkdir -p ' + filesdir)
    check_file = os.path.isfile(yamlfile)
    if check_file == False:
        os.popen('touch ' + yamlfile)
        time.sleep(1)    
    errmsg = "\n  Expects one of these arguments: png2yaml, yaml2png\n"
    try:
        option = sys.argv[1]
        if option == "yaml2png":
            yaml2png()
        elif option == "png2yaml":
            png2yaml()
        else:
            print(errmsg)
    except:
        print(errmsg)        

         
def png2yaml():
    try:
        if any(File.endswith(".png") for File in os.listdir(filesdir)):
            file = open(yamlfile, 'w')
            file.write('---\n')
            with os.popen('ls '+ filesdir + '/*.png') as pipe:
                for line in pipe:
                    x = line.strip()
                    with open(x, "rb") as file:
                        encoded_string = base64.b64encode(file.read())
                        file = open(yamlfile, 'a')
                        file.write(x + ': ' + encoded_string.decode('ascii')+ '\n')
            file.close()
        else:
            exit(1)
    except:
        print("\n  Coundn't find any *.png files in", filesdir, "\n")


def yaml2png():
    with open(yamlfile, 'r') as f:
        try:
            data = yaml.full_load(f)
            for key in data:
                value = data.get(key)
                value_bytes = value.encode('utf-8')
                with open(key, 'wb') as file_to_save:
                    decoded_image_data = base64.decodebytes(value_bytes)
                    file_to_save.write(decoded_image_data)
                    file_to_save.close()
        except:
            print("\n  Looks like nothing is in", yamlfile, "\n")
    f.close()


setup()
