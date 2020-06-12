# clone cluster config repo, change jx-requirements.yaml
# OSS JX Boot Config Repo only
# https://github.com/jenkins-x/jenkins-x-boot-config.git
git clone \
    https://github.com/cloudbees/cloudbees-jenkins-x-boot-config.git  \
    environment-$CLUSTER_NAME-dev && \ 
cd environment-$CLUSTER_NAME-dev

# Open jx-requirements.yml in an editor
# Set cluster.clusterName to $CLUSTER_NAME
# Set cluster.environmentGitOwner to Github Org
# Set cluster.project to jx-development (in my case)
# Set cluster.zone to us-west1-a (in my case)
# Save & Exit
jx boot