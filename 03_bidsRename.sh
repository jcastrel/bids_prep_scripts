#!/bin/sh
# renames the bids files
# JCastrellon, 11.2017
# updated, 06.2018
#
# Usage: "sh 03_bidsRename.sh ${HOME_DIR}"
#

HOME_DIR=${1}

cd ${HOME_DIR}

for i in {0..9}; do
	for j in {0..9}; do
		for k in {0..9}; do
			if [ -d "sub-${i}${j}${k}" ]; then
				echo "Renaming files for sub-${i}${j}${k}";
				python ${HOME_DIR}/bids_prep_scripts/bidsRename.py sub-${i}${j}${k};
			fi
		done
	done
done