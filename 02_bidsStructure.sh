#!/bin/sh
# creates the bids structure
# JCastrellon, 11.2017
# updated, 06.2018
#
# Usage: "sh 02_bidsStructure.sh ${HOME_DIR}"
#

HOME_DIR=${1}

cd ${HOME_DIR}

for i in {0..9}; do
	for j in {0..9}; do
		for k in {0..9}; do
			if [ -d "sub-${i}${j}${k}" ]; then
				cd sub-${i}${j}${k};
		
				#final anatomical directory
				if [ ! -d "anat" ]; then
					mkdir anat;
				fi
		
				#temporary T1 anatomical directory
				if [ ! -d "T1w" ]; then
					mkdir T1w;
				fi
		
				#temporary PD anatomical directory
				if [ ! -d "PD" ]; then
					mkdir PD;
				fi
				
				#final functional directory
				if [ ! -d "func" ]; then
					mkdir func;
				fi
		
				#temporary functional directory
				if [ ! -d "task" ]; then
					mkdir task;
				fi
		
				#final field map directory
				if [ ! -d "fmap" ]; then
					mkdir fmap;
				fi
		
				#temporary field map directory
				if [ ! -d "FieldMap" ]; then
					mkdir FieldMap;
				fi
		
				#final diffusion directory
				if [ ! -d "dwi" ]; then
					mkdir dwi;
				fi
		
				#temporary diffusion directory
				if [ ! -d "Diffusion" ]; then
					mkdir Diffusion;
				fi
		
				echo "Copying files for subject ${i}${j}${k}"
		
				#anatomical T1 - change file pattern as needed
				cp raw/nifti/*T1* T1w/.
		
				cp raw/nifti/*T1* anat/.
		
				
				#anatomical PD - change file pattern as needed
				cp raw/nifti/*PD* PD/.
		
				cp raw/nifti/*PD* anat/.
				
				#functional - change file pattern as needed
				cp raw/nifti/*Effort* task/.
				cp raw/nifti/*MID* task/.
				cp raw/nifti/*Resting* task/.
		
				cp raw/nifti/*Effort* func/.
				cp raw/nifti/*MID* func/.
				cp raw/nifti/*Resting* func/.
		
				#field map - change file pattern as needed
				cp raw/nifti/*B0* fmap/.
		
				cp raw/nifti/*B0* FieldMap/.
	
				#diffusion - change file pattern as needed
				cp raw/nifti/*dti* Diffusion/.

				cp raw/nifti/*dti* dwi/.
			fi
		done
	done
	cd ${HOME_DIR}
done