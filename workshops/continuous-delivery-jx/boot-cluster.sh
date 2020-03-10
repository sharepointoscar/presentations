# set cluster name env var
export CLUSTER_NAME='tequila'

# clone cluster config repo, change jx-requirements.yaml
git clone \
    https://github.com/jenkins-x/jenkins-x-boot-config.git  \
    environment-$CLUSTER_NAME-dev && \
    
cd environment-$CLUSTER_NAME-dev

# Open jx-requirements.yml in an editor
# Set cluster.clusterName to $CLUSTER_NAME
# Set cluster.environmentGitOwner to Github Org
# Set cluster.project to jx-development (in my case)
# Set cluster.zone to us-west1-a (in my case)
# Save & Exit
jx boot