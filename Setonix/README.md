## Setonix nf-core profile 

### Considerations 

* Queues all have external network access 
* Long running queue 96h limit available 
* Need for benchmarking to determine SUs for project allocation 
* Workflows, genomes and datasets have different resource requirements 

### Objectives 

* Simplify process of running nf-core workflows on Setonix HPC
* Address challenges with resource benchmarking for project allocation 

### Solution

* Use beforeScript/afterScript feature 
* Use dynamic retry to manage resource ceilings 
* Apply limitations on job submission for queue 
* Use withLabel and withName scopes to assign resources appropriately 
* Use errorStrategy scope to define exit codes upon which to retry 
* For greedy Java, can use NXF_OPTS='-XmsXg -XmxXg' flags set with env{}

### Resources 

* [Setonix User Guide](https://support.pawsey.org.au/documentation/display/US/Running+Jobs+on+Setonix)
