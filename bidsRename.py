#! /usr/bin/python
###########################################
##### Use script to rename BIDS files #####
## J.Castrellon, Duke University, 11.2017##
###########################################

import os, shutil, fnmatch
import sys
from sys import argv
print sys.argv[1]

subj = str(sys.argv[1])
print 'Begining Subject ' + subj

# Get subject names and set input/output directories
# ----------------------------------------------------------------------- 
base_dir = '/Users/jaimecastrellon/Desktop/dnd/'
#subjects = [i for i in os.listdir(base_dir)]
#subjects.remove('.DS_Store')
s = '%s'%subj

# ----------------------------------------------------------------------- 
# Change file names for anatomical
# ----------------------------------------------------------------------- 	
# Make anat directory
#if not os.path.exists(os.path.join(base_dir, s, 'anat')):
#	os.makedirs(os.path.join(base_dir, s, 'anat'))
#if not os.path.exists(os.path.join(base_dir, s, 'dwi')):
 #   os.makedirs(os.path.join(base_dir, s, 'anat'))


# ----------------------------------------------------------------------- 
# Change file names for diffusion
# ----------------------------------------------------------------------- 
dwi = [f for f in os.listdir(os.path.join(base_dir, s, 'Diffusion'))]
[os.rename(os.path.join(base_dir, s, 'Diffusion', d), os.path.join(base_dir, s, 'dwi', s + '_dwi.bvec')) for d in dwi if d.endswith('.bvec')]
[os.rename(os.path.join(base_dir, s, 'Diffusion', d), os.path.join(base_dir, s, 'dwi', s + '_dwi.bval')) for d in dwi if d.endswith('.bval')]
[os.rename(os.path.join(base_dir, s, 'Diffusion', d), os.path.join(base_dir, s, 'dwi', s + '_dwi.nii.gz')) for d in dwi if d.endswith('.nii.gz')]
[os.rename(os.path.join(base_dir, s, 'Diffusion', d), os.path.join(base_dir, s, 'dwi', s + '_dwi.json')) for d in dwi if d.endswith('.json')]
 
shutil.rmtree(os.path.join(base_dir, s, 'Diffusion'))

# ----------------------------------------------------------------------- 
# Change file names for T1w
# ----------------------------------------------------------------------- 
t1 = [f for f in os.listdir(os.path.join(base_dir, s, 'T1w'))]
	#t1.remove('.DS_Store')

t1_json = fnmatch.filter(t1, '*.json')
[os.rename(os.path.join(base_dir, s, 'T1w', t1_json[d]), os.path.join(base_dir, s, 'anat', s + '_T1w' + '.json')) for d in range(len(t1_json))]

t1_nifti = fnmatch.filter(t1, '*.nii.gz')
[os.rename(os.path.join(base_dir, s, 'T1w', t1_nifti[d]), os.path.join(base_dir, s, 'anat', s + '_T1w' + '.nii.gz')) for d in range(len(t1_nifti))]

shutil.rmtree(os.path.join(base_dir, s, 'T1w'))


# ----------------------------------------------------------------------- 
# Change file names for PD (Proton Density)
# ----------------------------------------------------------------------- 
pd = [f for f in os.listdir(os.path.join(base_dir, s, 'PD'))]
	#t1.remove('.DS_Store')

pd_json = fnmatch.filter(pd, '*.json')
[os.rename(os.path.join(base_dir, s, 'PD', pd_json[d]), os.path.join(base_dir, s, 'anat', s + '_PD' + '.json')) for d in range(len(pd_json))]

pd_nifti = fnmatch.filter(pd, '*.nii.gz')
[os.rename(os.path.join(base_dir, s, 'PD', pd_nifti[d]), os.path.join(base_dir, s, 'anat', s + '_PD' + '.nii.gz')) for d in range(len(pd_nifti))]

shutil.rmtree(os.path.join(base_dir, s, 'PD'))

# ----------------------------------------------------------------------- 	
# Change file names for task
# -----------------------------------------------------------------------  	

#TASK 01
task = [f for f in os.listdir(os.path.join(base_dir, s, 'task'))]
	# task.remove('.DS_Store')
task01_json = fnmatch.filter(task, '*Effort*.json')
[os.rename(os.path.join(base_dir, s, 'task', task01_json[d]), os.path.join(base_dir, s, 'func', s + '_task-ProbEffort_run-0' + str(d+1) + '_bold' + '.json')) for d in range(len(task01_json))]

task01_nifti = fnmatch.filter(task, '*Effort*.nii.gz')
[os.rename(os.path.join(base_dir, s, 'task', task01_nifti[d]), os.path.join(base_dir, s, 'func', s + '_task-ProbEffort_run-0' + str(d+1) + '_bold' + '.nii.gz')) for d in range(len(task01_nifti))]

#TASK 02
task02_json = fnmatch.filter(task, '*MID*.json')
[os.rename(os.path.join(base_dir, s, 'task', task02_json[d]), os.path.join(base_dir, s, 'func', s + '_task-ProbMID_run-0' + str(d+1) + '_bold' + '.json')) for d in range(len(task02_json))]

task02_nifti = fnmatch.filter(task, '*MID*.nii.gz')
[os.rename(os.path.join(base_dir, s, 'task', task02_nifti[d]), os.path.join(base_dir, s, 'func', s + '_task-ProbMID_run-0' + str(d+1) + '_bold' + '.nii.gz')) for d in range(len(task02_nifti))]


#REST 01
rest_json = fnmatch.filter(task, '*Resting*.json')
[os.rename(os.path.join(base_dir, s, 'task', rest_json[d]), os.path.join(base_dir, s, 'func', s + '_task-rest' + '_bold' + '.json')) for d in range(len(rest_json))]

rest_nifti = fnmatch.filter(task, '*Resting*.nii.gz')
[os.rename(os.path.join(base_dir, s, 'task', rest_nifti[d]), os.path.join(base_dir, s, 'func', s + '_task-rest' + '_bold' + '.nii.gz')) for d in range(len(rest_nifti))]


shutil.rmtree(os.path.join(base_dir, s, 'task'))

# ----------------------------------------------------------------------- 
# Change file names for field maps
# ----------------------------------------------------------------------- 
# fmap = [f for f in os.listdir(os.path.join(base_dir, s, 'fmap'))]
#     #fmap.remove('.DS_Store')
#
# fmap_json = fnmatch.filter(fmap, '*.json')
# [os.rename(os.path.join(base_dir, s, 'FieldMap', fmap_json[d]), os.path.join(base_dir, s, 'fmap', s + '_T1w' + str(d+1) + '.json')) for d in range(len(fmap_json))]
#
# fmap_nifti = fnmatch.filter(fmap, '*.nii.gz')
# [os.rename(os.path.join(base_dir, s, 'FieldMap', fmap_nifti[d]), os.path.join(base_dir, s, 'fmap', s + '_T1w' + str(d+1) + '.nii.gz')) for d in range(len(fmap_nifti))]
#
# shutil.rmtree(os.path.join(base_dir, s, 'FieldMap'))
#
    
# ----------------------------------------------------------------------- 
# ----------------------------------------------------------------------- 
    
    