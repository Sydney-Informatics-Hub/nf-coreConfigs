#!/bin/bash -l 

#Load singularity and nextflow modules. The specific version numbers may change over time. 
#Check what modules are available with `module spider <tool_name>`

module load singularity/3.11.4-slurm
module load nextflow/23.04.3

#Run the pipeline
nextflow run ../rnaseq/main.nf \
    --outdir ./results \
    -c pawsey-setonix.config \
    -profile singularity,test