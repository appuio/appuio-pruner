#!/bin/sh

while true; do
  echo "Pruning old deployments"
  oadm prune deployments --orphans --confirm
  echo

  echo "Pruning old builds"
  oadm prune builds --orphans --confirm
  echo

  echo "Pruning old images from registry"
  oadm prune images --confirm
  echo

  sleep 3600
done

