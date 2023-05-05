#!/bin/bash
## The first line has to say this, as a bash script

## Job Name
#SBATCH --job-name=test_python
#SBATCH --mail-user=yibin115@uw.edu

## Partition and Allocation
#SBATCH -p ckpt
#SBATCH -A comdata-ckpt

## Resources
#SBATCH --nodes=1
#SBATCH --time=04:00:00
#SBATCH --ntasks-per-node=30
#SBATCH --mem=48G

## Specify the working directory for this job
#SBATCH --chdir=.
#SBATCH --export=all

## Import any modules here

## Scripts to be executed here
python assign_features.py

## Clean up
exit 0
