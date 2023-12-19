#!/bin/bash

SAVEIFS=$IFS
IFS=$(echo -en "\n\b")
file=pngs.yaml
echo "---" > $file
for i in $(find . -maxdepth 1 -type f | awk -F '/' '{print $2}' | grep -v .DS_Store | grep png); do
    name_fix=$(echo "$i" | sed 's/ /_SPACE_/g')
    echo "${name_fix}: $(cat $i | base64)" >> $file
done
IFS=$SAVEIFS
