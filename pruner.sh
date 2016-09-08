#!/bin/sh

while true; do
  echo "Pruning old deployments"
  oc adm prune deployments --orphans --confirm
  echo

  echo "Pruning old builds"
  oc adm prune builds --orphans --confirm
  echo

  echo "Pruning old images from registry"
  oc adm prune images --confirm
  echo

  sleep 3600
done
