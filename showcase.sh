#!/bin/bash

backup() {
    cp pelicanconf.py pelicanconf.py.bak
}

restore() {
    mv pelicanconf.py.bak pelicanconf.py
}

preview() {
    THEME=`basename $1`
    OUTPUT_PATH="output/$THEME"
    pelican-themes -i $1
    sed -i "s/THEME =.*/THEME = \"$THEME\"/g" pelicanconf.py
    pelican content -o $OUTPUT_PATH -s pelicanconf.py
}

pushd $2
backup
for i in $(find $1 -maxdepth 1 -mindepth 1 -type d ! -path  "*.git*")
do
    preview "$i"
done
restore
popd

python gen.py $1
cp -r gallery $2/output
cp $2/output/gallery/index.html $2/output/index.html
