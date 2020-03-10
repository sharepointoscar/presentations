kubectl create secret generic github-auth --from-literal=clientID='383489389' --from-literal=clientSecret='55858' --namespace jx

git checkout -b add-k8s-secrets
