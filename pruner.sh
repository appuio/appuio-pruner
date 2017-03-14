#!/bin/bash

while true; do
  date
  echo

  echo "Pruning old deployments"
  oc adm prune deployments --orphans --confirm
  echo

  echo "Pruning old builds"
  oc adm prune builds --orphans --confirm
  echo

  # Only prune images at 3:15 in the morning to prevent
  # triggering bug deleting blobs which are pushed during prune.
  if [ $(date +%H) -eq 3 ]; then
    echo "Pruning old images from registry"
    oc adm prune images --confirm
    echo
  fi

  echo "----------------------------------------"

  # Wait till it's 15 past for the next time
  sleep $(( ( 75 - $(date +%-M) ) % 60 ))m
done
