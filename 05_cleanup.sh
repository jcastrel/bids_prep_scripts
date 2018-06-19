#!/bin/sh
# cleans up folders
# JCastrellon, 11.2017
# updated, 06.2018
#
# Usage: "sh 05_cleanup.sh ${HOME_DIR}"
#


HOME_DIR=${1}

cd ${HOME_DIR};

if [ ! -d "raw" ]; then
	mkdir raw
fi

for i in {0..9}; do
	for j in {0..9}; do
		for k in {0..9}; do
			
			if [ -d "sub-${i}${j}${k}" ]; then
				if [ ! -d "raw/sub-${i}${j}${k}" ]; then
					mkdir raw/sub-${i}${j}${k};
				fi
				mv sub-${i}${j}${k}/raw raw/sub-${i}${j}${k}/.
		
				rm sub-${i}${j}${k}/*/*WIP*.nii.gz
				rm sub-${i}${j}${k}/*/*WIP*.json
				rm sub-${i}${j}${k}/*/*WIP*.bval
				rm sub-${i}${j}${k}/*/*WIP*.bvec
			fi
			cd ${HOME_DIR}
		done
	done
done