# download binary for CJXD (CloudBees Jenkins X Distro)
# https://docs.cloudbees.com/docs/cloudbees-jenkins-x-distribution 
curl -L https://storage.googleapis.com/artifacts.jenkinsxio.appspot.com/binaries/cjxd/latest/jx-darwin-amd64.tar.gz | tar xzv

# move to bin
sudo mv jx /usr/local/bin

# test
jx version
NAME               VERSION
jx                 2.0.1192+cjxd.7
Kubernetes cluster v1.14.10-gke.17
kubectl            v1.16.0
helm client        Client: v2.13.1+g618447c
git                2.21.0
Operating System   Mac OS X 10.14.6 build 18G3020