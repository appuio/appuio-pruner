# appuio-pruner
The APPUiO pruner prunes old builds, deployments and registry images from an OpenShift cluster.

## Installation

    oc new-project appuio-infra
    oc new-app https://github.com/appuio/appuio-pruner
    oc adm policy add-cluster-role-to-user edit system:serviceaccount:appuio-infra:default
    oc adm policy add-cluster-role-to-user system:image-pruner system:serviceaccount:appuio-infra:default
