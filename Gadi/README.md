## Gadi nf-core profile 

### Considerations 

* Queues do not have external network access and limit of 48hrs 
* Workaround is to submit head job to the copyq which has external network access but limit of 10 hours
* Need for benchmarking to determine SUs for project allocation 
* Workflows, genomes and datasets have different resource requirements 
* Nextflow Java virtual machines can request a large amount of memory sometimes

### Objectives 

* Identify resource requirements of popular workflows - is this specified in documentation? 
* Simplify process of running nf-core workflows on Gadi HPC
* Address challenges with resource benchmarking for project allocation 

### Solution

* Use beforeScript/afterScript feature 
* Use dynamic retry to manage resource ceilings 
* Apply limitations on job submission for queue 
* Use withLabel and withName scopes to assign resources appropriately 
* Use errorStrategy scope to define exit codes upon which to retry 
* For greedy Java, can use NXF_OPTS='-XmsXg -XmxXg' flags set with env{}

### Resources 

* [NCI SU definition](https://opus.nci.org.au/pages/viewpage.action?pageId=119964320)
* [NCI Nextflow documentation](https://opus.nci.org.au/display/DAE/Nextflow)
* [Useful PBS env variables](https://opus.nci.org.au/display/Help/Useful+PBS+Environment+Variables)
* [Nextflow env variables](https://www.nextflow.io/docs/latest/config.html#environment-variables)

