
![IMAGE](assets/img/jx-logo.svg)


## Implement Canary @css[text-yellow text-15](@emoji[ ]) Deployments for your App

--- 
@title[Canary Deployments with Jenkins X]
# Agenda

@snap[fragment]
@ul[list-spaced-bullets list-boxed-bullets text-gold text-07]
- Install Istio and Flagger
- Import existing app
- Configure Canary Settings
- View metrics via Prometheus
@ulend
@snapend

---

@title[Canary Benefits]
@snap[north span-100]
## @css[text-yellow](<br>Canary Deployment Benefits   @fa[dove])
@snapend

@snap[fragment](false)
@ul[list-spaced-bullets list-boxed-bullets text-gold text-07]
- Small scoped impact
- Easier Rollbacks
- Load tolerant
- Concurrency
@ulend
@snapend
---

@title[Install Istio and Flagger]
@snap[north span-100]
## @css[text-yellow](Install Istio & Flagger   @fa[github])
@snapend

@snap[center]
@css[text-yellow text-06](visit https://istio.io/docs/setup/getting-started/#download for details.  @fa[external-link-alt])

```bash
# downloa istioctl
curl -L https://istio.io/downloadIstio | ISTIO_VERSION=1.4.3 sh -

# move to bin
mv istio-1.4.3/bin/istioctl /usr/local/bin
chmod +x /usr/local/bin/istioctl

# install istio
istioctl manifest apply --set profile=demo --skip-confirmation

# install flagger
kubectl apply \
    --kustomize github.com/weaveworks/flagger/kustomize/istio

```
@snapend

--- 

@title[Get Istio IP]
@snap[north span-100]
## @css[text-yellow](Get Istio LoadBalancer IP   @fa[github])
@snapend

@snap[fragment]
```bash
ISTIO_HOST=$(kubectl --namespace istio-system \
get service istio-ingressgateway \
--output \
jsonpath='{.status.loadBalancer.ingress[0].ip}')

export ISTIO_IP="$(dig +short $ISTIO_HOST | tail -n 1)"

echo $ISTIO_IP
```

@snap[text-06 text-gold]
View Pods created as a result of installing Istio and Flagger.
@snapend

```bash
kubectl get pods --namespace istio-system

# istio injection is enabled
kubectl describe namespace jx-production

# modify namespace to allow for istio injection
kubectl label namespace jx-production \
  istio-injection=enabled --overwrite
```
@snapend

--- 

@title[Import existing app]
@snap[north span-100]
## @css[text-yellow](Import Existing App   @fa[laptop-code])
@snap[text-center text-06]
@quote[The World did not come to be today. I'm sure you have apps you've developed.](Viktor Farcic - during one of our workshops)
@snapend
@snapend

@snap[span-100 text-17]
```bash
# import the open source sample app
jx import --url https://github.com/jenkins-oscar/skiapp.git \
   --git-public

# monitor initial pipeline
jx get activities -f skiapp -w

# monitor app deployment to staging
jx get activity -f environment-tequila-staging -w
```
@snapend

---

@title[Configure Canary Settings]
@snap[north span-100]
## @css[text-yellow](  <br>Configure Canary Settings   @fa[file-code])
@snapend

@snap[montserrat]
We will deploy our app to production to only 20% of our users while monitoring traffic for 60 seconds.
@snapend


@snap[font-montserrat-medium]
We currently have our app running in staging.  The best place to enable canary is in the **Production** environment repository.
@snapend
---
@title[Configure Canary Settings]
@snap[north span-100]
## @css[text-yellow](Modify Production Env   @fa[laptop-code])
@snapend

```bash
export CANARY_ADDR=production.jx-skiapp.$ISTIO_IP.nip.io

jx get activity \
  --filter environment-$CLUSTER_NAME-production/master \ 
  --watch

git clone \
    https://github.com/jenkins-oscar/environment-$CLUSTER_NAME-production.git

cd environment-$CLUSTER_NAME-production
```
---


@title[Configure Canary Settings]
@snap[north span-100]
## @css[text-yellow](Modify Production Env   @fa[laptop-code])
@snapend

```bash
# we modify the values.yaml as follows
echo "skiapp:
  hpa:
    enabled: true
    minReplicas: 5
  canary:
    enabled: true
    host: $CANARY_ADDR
" | tee -a env/values.yaml

# push our changes to production repo
git add . && git commit -m "Added progressive deployment" && git push
```
---
@title[Configure Canary Settings]
@snap[north span-100]
### @css[text-yellow](Promote app to Prod   @fa[laptop-code])
@snapend

```bash
# promote the version in staging, to production
# NOTE: We will need to later make a change and test said change
# against the 20% of our users.
jx promote --app skiapp --version 0.0.47 --env production
```
---

@title[Test Canary ]
@snap[north span-100]
## @css[text-yellow](Change App Homepage   @fa[laptop-code])
#### Git checkout, make trivial change.
@snapend

```bash
# in root of skiapp dir
git checkout -b homepage-change
# change global nav Contact to Production Change Contact

# modify index.html and check in
git add . && git commit -m "changed globa navigation"

# push to app feature branch
git push --set-upstream origin homepage-change

## promote latest version to production
jx promote --app skiapp --version $VERSION --env production
```
---
@title[Test Canary ]
@snap[north span-100]
## @css[text-yellow](Test App Canary Deployment   @fa[laptop-code])
#### Monitor pipeline from PR on separate terminal
@snapend

```bash
# Open in separate terminal
# We should see 1 out of 5 requests output our grep
while true
do 
    curl $CANARY_ADDR | grep 'Production'
    sleep 0.2
done

```
---

@title[Configure Canary Settings]
@snap[north span-100]
## @css[text-yellow](Verify Canary Settings   @fa[laptop-code])
@snapend

```bash
# get the canary object from kubernetes
kubectl -n jx-production get canaries

# check events for canary, should show success.
kubectl describe canary jx-skiapp -n jx-production

```
---
@title[Configure Canary Settings]
@snap[north span-100]
## @css[text-yellow](<br>Using Grafana  @fa[paint-roller])
#### Visualize canary deployment metrics via Grafana Dashboard
@snapend

@snap[center]
```bash
# first get our public IP
LB_IP=$(kubectl --namespace kube-system \
    get svc jxing-nginx-ingress-controller \
    -o jsonpath="{.status.loadBalancer.ingress[0].ip}")
```
@snapend

---

@title[Configure Canary Settings]
@snap[north span-100]
## @css[text-yellow](<br>Using Grafana  @fa[paint-roller])
#### Visualize canary deployment metrics via Grafana Dashboard
@snapend

@snap[center]
```bash
# create ingress for grafana
echo "apiVersion: extensions/v1beta1
kind: Ingress
metadata:
  annotations:
    kubernetes.io/ingress.class: nginx
  name: flagger-grafana
  namespace: istio-system
spec:
  rules:
  - host: flagger-grafana.$LB_IP.nip.io
    http:
      paths:
      - backend:
          serviceName: flagger-grafana
          servicePort: 80
" | kubectl create -f -
```
@snapend

---
@title[Questions]
@snap[north span-100]
## @css[text-yellow](Got Questions   @fa[question])
@snapend
# Q&A
@emoji[tada]