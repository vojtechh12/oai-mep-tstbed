<img src="./images/logo_cvut_en.jpg" alt="" border=3 width=150>
</img>

# VEC testbed
*This repository is a result of bachelor's project under Czech Technical University in Prague*

The repository contains the code and documentation for VEC tested. The project was forked from [OAI-mep](https://gitlab.eurecom.fr/oai/orchestration/blueprints).

The testbed provides the necessary emulated network infrastructure to enable creating and testing applications for **Vehicular Edge Computing (VEC)**.

## Testbed Features
* MEC platform by OpenAirInterface (OAI)
* OAI 5G network running in docker containers
* OAI Configuration Manager (CM) exposing 5G core network events to MEC platform
* Testbed application demonstrating how to create, containerize, deploy and register a MEC app into MEC platform environment
* MEC application is a Flask app
* in future, the app will both consume and provide services in MEC platform environment

## Deploy the testbed
1. [Deploy the OAI MEP](./mep/README.md)
2. [Deploy the MEC app](./Testbed-proj/README.md)

<img src="./images/oai_final_logo.png" alt="" border=3 height=50 width=150></img>

