# nf-core/configs: PROFILE Configuration

nf-core pipelines have been successfully configured for use on the [Gadi HPC](https://opus.nci.org.au/display/Help/Gadi+User+Guide) at the National Computational Infrastructure, Canberra, Australia. 

To run an nf-core pipeline at NCI Gadi, run the pipeline with `-profile nci_gadi`. This will download and launch the [`nci_gadi.config`](../conf/nci_gadi.config) which has been pre-configured with a setup suitable for the NCI Gadi HPC cluster. Using this profile, a docker image containing all of the required software will be downloaded, and converted to a Singularity image before execution of the pipeline.

## Access to NCI Gadi

Please be aware that you will need to have a user account, be the member of an Gadi project, and have a service unit allocation to your project in order to use this infrastructure. See the [NCI user guide](https://opus.nci.org.au/display/Help/Getting+Started+at+NCI) for details on getting access to Gadi. 

## Launch an nf-core pipeline on Gadi

### Prerequisites 

Before running the pipeline you will need to load Nextflow and Singularity, both of which are globally installed modules on Gadi. You can do this by running the commands below:

```bash
module purge
module load nextflow singularity
```

### Cluster considerations 

Please be aware that as of July 2023, NCI Gadi HPC queues **do not** have external network access. This means you will not be able to pull the workflow code base or containers if you submit your `nextflow run nf-core/..` command as a job on any of the standard job queues. We currently recommend you download a local copy of the nf-core pipeline and run your Nextflow head job either in a GNU screen or tmux session from the login node or submit it as a job to the [copyq](https://opus.nci.org.au/display/Help/Queue+Structure). 

This config currently determined which Gadi queue to submit your task jobs to based on the amount of memory required. For the sake of resource and cost (service unit) efficiency, the following rules are applied by this config: 

* Jobs requesting **less than 128 Gb** will be submitted to the normalbw queue
* Jobs requesting **more than 128 Gb and less than 190 Gb** will be submitted to the normal queue
* Jobs requesting **more than 190 Gb and less than 1020 Gb** will be submitted to the hugemembw queue 

See the NCI Gadi [queue limit documentation](https://opus.nci.org.au/display/Help/Queue+Limits) for details on charge rates for each queue. 

### Project accounting 

This config uses the PBS environmental variable `$PROJECT` to assign a project code to all task job submissions for billing purposes. If you are a member of multiple Gadi projects, you should confirm which project will be charged for your pipeline execution. You can do this using: 

```
echo $PROJECT
```

The version of Nextflow installed on Gadi has been modified to make it easier to specify resource options for jobs submitted to the cluster. See [here](https://opus.nci.org.au/display/DAE/Nextflow) for more details. You can manually override the $PROJECT specification by editing your local copy of the `nci_gadi.config` and replacing $PROJECT with your project code in the `process{}` scope. For example if I wanted to manually specify the proect aa00, I would edit my copy of the `nci_gadi.config` as follows: 

```
process {
    executor = 'pbspro'
    project = 'aa00'
    storage = 'scratch/aa00+gdata/aa00'
    ...
}
```

## Additional config features 

The NCI Gadi HPC config creates a verbose resource trace file that can be used to calculate service unit costs and job efficiency. You can use the script at SIH GitHub to calculate job efficiency and the per-task and total cost of your pipeline run. This is useful for resource benchmarking. 
