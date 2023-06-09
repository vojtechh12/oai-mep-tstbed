<img src="./images/logo_cvut_en.jpg" alt="" border=3 width=150>
</img>

# VEC testbed
*This repository is a result of bachelor's project under Czech Technical University in Prague*

* contains the code and documentation for VEC tested
* forked from [OAI-mep](https://gitlab.eurecom.fr/oai/orchestration/blueprints)
* The testbed provides the necessary emulated network infrastructure to enable creating and testing applications for **Vehicular Edge Computing (VEC)**

## Testbed Features
* MEC platform by OpenAirInterface (OAI)
* OAI 5G network running in docker containers
* OAI Configuration Manager (CM) exposing 5G core network events to MEC platform
* OAI Radio Network Information Service (RNIS) running as a MEC app
* Testbed application demonstrating how to create, containerize, deploy and register a MEC app into MEC platform environment
* MEC application is a Flask app
* in future, the app will both consume and provide services in MEC platform environment

## Deploy the testbed
clone this project:
```shell
git clone https://github.com/vojtechh12/oai-mep-tstbed.git
```
1. [Deploy the OAI MEP](./mep/README.md)
2. [Deploy the MEC app](./sample_app/README.md)


