# files-to-yaml

## Description
Convert your small to medium-sized binary files (like images) to yaml for better source control in git

## Details
Put files of the extention you wish to convert to yaml into the files/ directory

## Example
To send your *.png files to yaml:
~~~
cd files/
./convert.py ext2yaml png
~~~

To retrieve files from yaml:
~~~
./convert.py yaml2ext
~~~
