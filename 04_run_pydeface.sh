#!/bin/sh
# defaces (anonymizes) the anatomical T1
# JCastrellon, 11.2017
# updated, 06.2018
#
# Usage: "sh 04_run_pydeface.sh ${HOME_DIR}"
#

#Loop through subjects to deface structural T1 images

HOME_DIR=${1}


for i in {0..9}; do
	for j in {0..9}; do
		for k in {0..9}; do
			cd ${HOME_DIR}
			if [ -d "sub-${i}${j}${k}" ]; then
				echo "defacing subject ${i}${j}${k}";
				pydeface.py sub-${i}${j}${k}/anat/sub-${i}${j}${k}_T1w.nii.gz;
				mv sub-${i}${j}${k}/anat/sub-${i}${j}${k}_T1w_defaced.nii.gz sub-${i}${j}${k}/anat/sub-${i}${j}${k}_T1w.nii.gz
			fi
		done
	done
done
