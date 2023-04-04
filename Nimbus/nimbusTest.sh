#!/bin/bash

materials=/home/ubuntu/nf-coreConfigs/materials

nextflow run ../rnaseq/main.nf \
    --input $materials/samplesheet.csv \
    --outdir results \
    --gtf $materials/mm10_reference/mm10_chr18.gtf \
    --fasta $materials/mm10_reference/mm10_chr18.fa \
    --star_index $materials/mm10_reference/STAR \
    -c pawsey_nimbus.config -profile singularity,c2r8 