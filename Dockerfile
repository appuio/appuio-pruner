FROM registry.access.redhat.com/rhel7:latest

LABEL io.k8s.display-name="APPUiO Pruner" \
      io.k8s.description="The APPUiO Pruner prunes old builds, deployments and images."

RUN cd /usr/local/bin && \
    curl -k -O ${OC_URL:-https://console.appuio.ch/console/extensions/clients/linux/oc} && \
    chmod 755 oc

ENV HOME /tmp/

COPY pruner.sh /tmp/
COPY jobs-cleaner.py /tmp/

ENTRYPOINT ["/tmp/pruner.sh"]
