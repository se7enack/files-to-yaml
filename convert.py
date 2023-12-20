#!/usr/bin/env python3

import base64
import sys
import os
import yaml
import time

filesdir = "files"
yamlfile = (filesdir + "/inventory.yaml")
filetype = "ico"


def setup():
    os.popen('mkdir -p ' + filesdir)
    check_file = os.path.isfile(yamlfile)
    if check_file == False:
        os.popen('touch ' + yamlfile)
        time.sleep(1)    
    errmsg = "\n  Expects 2 arguments: (\"ext2yaml\" OR \"yaml2ext\") followed by a file extention. i.e. \"png\"\n"    
    try:
        option = sys.argv[1]
        if option == "yaml2ext":
            yaml2ext()
        elif option == "ext2yaml":
            if sys.argv[2]:
                ext2yaml()
            else:
                errmsg = "\n  Expects 2 arguments: (\"ext2yaml\" OR \"yaml2ext\") followed by a file extention. i.e. \"png\"\n"
                exit(1)
        else:
            print(errmsg)
    except:
        print(errmsg)

      
def ext2yaml():
    try:
        if any(File.endswith("." + filetype) for File in os.listdir(filesdir)):
            file = open(yamlfile, 'w')
            file.write('---\n')
            with os.popen('ls '+ filesdir + '/*.' + filetype) as pipe:
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
        print("\n  Coundn't find any *." + filetype, "files in", filesdir, "\n")


def yaml2ext():
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
