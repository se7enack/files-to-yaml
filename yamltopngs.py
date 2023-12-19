#!/usr/bin/env python3

import base64
import yaml

with open('pngs.yaml', 'r') as f:
    data = yaml.full_load(f)
    for key in data:
        value = data.get(key)
        value_bytes = value.encode('utf-8')
        with open(key, 'wb') as file_to_save:
            decoded_image_data = base64.decodebytes(value_bytes)
            file_to_save.write(decoded_image_data)
            file_to_save.close()
f.close()
