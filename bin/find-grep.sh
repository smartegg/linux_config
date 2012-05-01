#! /bin/sh

find $1 -type f -print0 | xargs -0 -e grep -nH --color -e $2
