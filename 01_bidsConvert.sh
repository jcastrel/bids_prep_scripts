#!/bin/sh
# Script to convert dicoms to .nii files
# JCastrellon, 11.2017
# updated, 06.2018
#
# Usage: "sh 01_bidsConvert.sh ${HOME_DIR}"
#
# assumes directory structure as:
# ${HOME_DIR}
#	sub-${subjID}
#		|__raw
#			|_dicoms
#				(.PAR/.REC/.dcm, etc.)



HOME_DIR=${1}

cd ${HOME_DIR}
for i in {0..9}; do
	for j in {0..9}; do
		for k in {0..9}; do
			if [ -d "sub-${i}${j}${k}" ]; then
				echo "Running dcm2niix for subject ${i}${j}${k}"
				cd sub-${i}${j}${k}/raw;
				if [ ! -d "nifti" ]; then
					mkdir nifti; 
				fi
				dcm2niix -b y -z y -f sub-${i}${j}${k}_%p -o nifti dicoms/*;
			fi
		done
	done
done
cd ${HOME_DIR};
