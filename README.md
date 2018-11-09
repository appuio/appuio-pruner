# APPUiO Pruner

This repository contains an Ansible role to install the **APPUiO object
pruner**, a set of 3 cronjobs which clean up old deployments, builds and images
respectively.


## What does it do?

It runs `oc adm prune XXX`.

## Service Account

The pruner jobs access the OpenShift API using the service account which the job
was started with. The playbook will create the required service account, roles
and role bindings for the jobs to do their job.

## Requirements

* [OpenShift Container Platform][ocp] 3.9 or later, or
* [OKD] 3.9 or later

## Role variables

| Name                    | Default value  | Description |
|-------------------------|----------------|-------------|
| appuio_pruner_namespace | `appuio-infra`  | Namespace to install the APPUiO pruner into |
| appuio_pruner_image     | `"docker.io/appuio/oc:{{ openshift_release }}"`  | Image for the pruner job |
| appuio_pruner_schedule  | `@hourly`  | Schedule in [Cron] format |


[ocp]: https://www.openshift.com/
[OKD]: https://www.okd.io/
[Cron]: https://en.wikipedia.org/wiki/Cron

## Dependencies

* <https://github.com/appuio/ansible-module-openshift>


## Example Usage

`playbook.yml`:

```yaml
roles:
  - role: appuio-pruner
    appuio_pruner_namespace: appuio-pruner
```
