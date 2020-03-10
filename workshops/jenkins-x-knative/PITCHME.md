### Jenkins X Canary Deployments


## Installing Gloo and Knative

* [Install glooctl](https://docs.solo.io/gloo/latest/installation/knative/#install-command-line-tool-cli)

```bash
glooctl install knative --install-knative-version=0.9.0
```

## Installing Gloo and Knative (!=EKS)

```bash
KNATIVE_IP=$(kubectl --namespace gloo-system \
    get service knative-external-proxy \
    --output jsonpath="{.status.loadBalancer.ingress[0].ip}")
```

## Installing Gloo and Knative (EKS)

```bash
KNATIVE_HOST=$(kubectl \
    --namespace gloo-system \
    get service knative-external-proxy \
    --output jsonpath="{.status.loadBalancer.ingress[0].hostname}")

export KNATIVE_IP="$(dig +short $KNATIVE_HOST | tail -n 1)"
```

## Installing Gloo and Knative

```bash
echo $KNATIVE_IP

echo "apiVersion: v1
kind: ConfigMap
metadata:
  name: config-domain
  namespace: knative-serving
data:
  $KNATIVE_IP.nip.io: \"\"" | kubectl apply --filename -

kubectl get namespaces
```

## Installing Gloo and Knative

```bash
jx edit deploy --team --kind knative --batch-mode
```

## New Serverless Application

```bash
jx create quickstart --filter rollout-app --project-name carsweb \
    --batch-mode

cd carsweb

cat charts/jx-knative/values.yaml

ls -1 charts/carsweb/templates

cat charts/carsweb/templates/deployment.yaml

cat charts/carsweb/templates/ksvc.yaml
```


## New Serverless Application Logs

```bash
jx get activities --filter carsweb --watch

kail
```

## New Serverless Application

```bash
jx get applications --env staging

ADDR=$(kubectl --namespace $NAMESPACE-staging get ksvc carsweb \
    --output jsonpath="{.status.url}")

echo $ADDR

curl "$ADDR"

kubectl --namespace $NAMESPACE-staging get pods
```

## New Serverless Application

```bash
# Wait for a while

kubectl --namespace $NAMESPACE-staging get pods

kubectl --namespace knative-serving describe configmap config-autoscaler

kubectl --namespace $NAMESPACE-staging get pods
```

## New Serverless Application - Run Siege

```bash
kubectl run siege --image yokogawa/siege --generator "run-pod/v1" \
    -it --rm -- --concurrent 300 --time 30S "$ADDR" \
    && kubectl --namespace $NAMESPACE-staging get pods

sed -e \
    's@revisionTemplate:@revisionTemplate:\
        metadata:\
          annotations:\
            autoscaling.knative.dev/target: "3"\
            autoscaling.knative.dev/maxScale: "5"@g' \
    -i charts/carsweb/templates/ksvc.yaml
```

## New Serverless Application - add knative target

```bash
git add .

git commit -m "Added Knative target"

git push --set-upstream origin master

jx get activities --filter carsweb --watch

jx get activities --filter environment-jx-rocks-staging/master --watch

curl "$ADDR/"
```

## New Serverless Application - run siege again

```bash
kubectl run siege --image yokogawa/siege --generator "run-pod/v1" \
    -it --rm -- --concurrent 400 --time 60S "$ADDR" \
    && kubectl --namespace $NAMESPACE-staging get pods \
    --selector serving.knative.dev/service=carsweb

kubectl --namespace $NAMESPACE-staging get pods \
    --selector serving.knative.dev/service=carsweb

kubectl --namespace $NAMESPACE-staging get pods \
    --selector serving.knative.dev/service=carsweb
```

## New Serverless Application - add miniScale

```bash
sed -e \
    's@autoscaling.knative.dev/target: "3"@autoscaling.knative.dev/target: "3"\
            autoscaling.knative.dev/minScale: "1"@g' \
    -i charts/carsweb/templates/ksvc.yaml

git add .

git commit -m "Added Knative minScale"

git push
```


## New Serverless Application - check activities

```bash
jx get activities --filter carsweb --watch

jx get activities --filter environment-jx-rocks-staging/master --watch

kubectl --namespace jx-staging get pods \
    --selector serving.knative.dev/service=carsweb

kubectl --namespace jx-staging get pods \
    --selector serving.knative.dev/service=carsweb
```

## Serverless With Pull Requests

```bash
git checkout -b serverless

echo "A silly change" | tee README.md

git add .

git commit -m "Made a silly change"

git push --set-upstream origin serverless

jx create pullrequest --title "A silly change" --body "What I can say?" \
    --batch-mode
```

## Serverless With Pull Requests

```bash
BRANCH=[...] # e.g., `PR-1`

jx get activities --filter carsweb/$BRANCH --watch

GH_USER=sharepointoscar

PR_NAMESPACE=$(echo jx-$GH_USER-jx-knative-$BRANCH \
  | tr '[:upper:]' '[:lower:]')

echo $PR_NAMESPACE

kubectl --namespace $PR_NAMESPACE get pods
```

## Serverless With Pull Requests - get svc

```bash
PR_ADDR=$(kubectl --namespace $PR_NAMESPACE get ksvc jx-knative \
    --output jsonpath="{.status.url}")

echo $PR_ADDR

curl "$PR_ADDR"
```

