#!/bin/bash

python ./main.py

list=`cat ./blacklist.json`

if [ "$list" == "[\"\"]" ]; then
	echo "`date`: nothing to blacklist" >> debug.log
else
	echo "`date`: /path/to/ansible-script ./blacklist.json" >> debug.log
	#/path/to/ansible-script ./blacklist.json
fi