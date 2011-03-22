#!/bin/bash

IFILE="$1"
OFILE="$(basename $IFILE '.py')_n.py"

sed -e 'y/abgdezhqiklmnxoprVstufcywJ/αβγδεζηθικλμνξοπρςστυφχψωϑ/' $1 |
sed -e 'y/ABGDEZHQIKLMNXOPRSTUFCYW/ΑΒΓΔΕΖΗΘΙΚΛΜΝΞΟΠΡΣΤΥΦΧΨΩ/' |
sed -e 'y/Со/Χο/' >$OFILE

# 0x0EE - о (русская)
# 0x0D1 - С (русская)
