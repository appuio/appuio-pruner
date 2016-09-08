FROM registry.access.redhat.com/rhel7:latest

LABEL io.k8s.display-name="APPUiO Pruner" \
      io.k8s.description="The APPUiO Pruner prunes old builds, deployments and images."

RUN cd /tmp && \
    curl -O http://upx.sourceforge.net/download/upx-3.91-amd64_linux.tar.bz2 && \
    tar xvfj upx-3.91-amd64_linux.tar.bz2 && \
    cd /usr/local/bin && \
    curl -O https://console.appuio.ch/console/extensions/clients/linux/oc && \
    /tmp/upx-3.91-amd64_linux/upx /usr/local/bin/oc && \
    rm -rf /tmp/upx-*

COPY pruner.sh /tmp/

ENTRYPOINT ["/tmp/pruner.sh"]
