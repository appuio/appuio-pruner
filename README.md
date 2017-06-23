# appuio-pruner
The APPUiO pruner prunes old builds, deployments and registry images from an OpenShift cluster.

## Installation

    oc new-project appuio-infra
    oc new-app https://github.com/appuio/appuio-pruner
    oc adm policy add-cluster-role-to-user edit system:serviceaccount:appuio-infra:default
    oc adm policy add-cluster-role-to-user system:image-pruner system:serviceaccount:appuio-infra:default

## Ansible Role

This repository contains an Ansible role for automatic installation of the APPUiO pruner.

### Requirements

One of:

* OpenShift Enterprise 3.2
* OpenShift Container Platform 3.3 or later
* OpenShift Origin M5 1.3 or later.

### Role Variables

| Name            | Default value                                                 | Description                                                                           |
|-----------------|---------------------------------------------------------------|---------------------------------------------------------------------------------------|
| src             | *role_src*, https://github.com/appuio/appuio-pruner.git       | Source repository of the APPUiO pruner                                                |
| version         | *role_version*, master                                        | Version of the pruner to build, i.e. Git ref of repo above                            |
| deployment_type | *openshift_deployment_type*, openshift-enterprise             | OpenShift deployment type (`openshift-enterprise` or `origin`), determines base image |
| oc_url          | https://console.appuio.ch/console/extensions/clients/linux/oc | URL of OpenShift client (oc)                                                          |
| namespace       | appuio-infra                                                  | namespace to install pruner into                                                      |
| timezone        | *appuio_container_timezone*, UTC                              | Timezone of the container                                                             |

In case of multiple default values the first defined value is used.

### Dependencies

* <https://github.com/appuio/ansible-module-openshift>

### Example Usage

`playbook.yml`:

```yaml
roles:
- role: appuio-pruner
```
