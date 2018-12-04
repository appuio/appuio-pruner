FROM docker.io/appuio/oc:v3.6

LABEL io.k8s.display-name="APPUiO Pruner" \
      io.k8s.description="The APPUiO Pruner prunes old builds, deployments and images."

ENV HOME /tmp/

COPY pruner.sh /tmp/
COPY jobs-cleaner.py /tmp/

ENTRYPOINT ["/tmp/pruner.sh"]
