# create cluster in GKE, replace <CLUSTER_NAME>
# with whatever yours is.
export CLUSTER_NAME='tequila' && \
jx create cluster gke \
    -n $CLUSTER_NAME --skip-installation --min-num-nodes=6 --max-num-nodes=8