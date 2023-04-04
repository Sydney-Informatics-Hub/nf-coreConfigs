# nf-coreConfigs

Development and testing nf-core configs for Australian national HPC and cloud platforms. 

## Infrastructures 
* Pawsey Nimbus cloud 
* Pawsey Setonix HPC
* NCI Nirin cloud   
* NCI Gadi HPC

## Testing instructions 

1. Clone this repository and change into it 

```
git clone https://github.com/Sydney-Informatics-Hub/nf-coreConfigs.git && cd $_
```

2. Clone the nf-core/rnaseq workflow

```
git clone https://github.com/nf-core/rnaseq.git 
```

3. Download the test data

```
wget -O nfcore_materials.tar.gz https://cloudstor.aarnet.edu.au/plus/s/gIBdDhKEwfq2j58/download
tar -zxvf nfcore_materials.tar.gz
```

4. Run and edit the provided bash script for the infrastructure being tested. For example:
```
bash Nimbus/nimbusTest.sh
```

Workflow should take ~17 minutes to run. 