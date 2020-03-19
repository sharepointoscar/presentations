
![IMAGE](assets/img/jx-logo.svg)


## Implement Canary @css[text-yellow text-15](@emoji[bird]) Deployments for your App
@css[text-06](Live with:<br> Oscar Medina @SharePointOscar<br>  Viktor Farcic @vfarcic )
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
istioctl manifest apply \
--set profile=demo --skip-confirmation

# install flagger
kubectl apply \
  --kustomize \
  github.com/weaveworks/flagger/kustomize/istio

```
@snapend

@snap[south span-100 text-15 text-gold]
@[2,zoom-10](download Istio specific version)
@[5-6,zoom-15](move to bin and make executable)
@[9-10,zoom-15](apply istio demo profile)
@[13-15,zoom-13](Install Flagger)
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

kubectl get pods --namespace istio-system

# istio injection is enabled
kubectl describe namespace jx-production

# modify namespace to allow for istio injection
kubectl label namespace jx-production \
  istio-injection=enabled --overwrite
```
@snap[south span-100 text-15 text-gold]
@[1-4,zoom-10](set env var with Istio load balancer Host IP)
@[6,zoom-10](set env var with Istio public IP)
@[8,zoom-15](verify we have an IP)
@[10,zoom-15](check all pods are provisioned)
@[12-13,zoom-15](see if production namespace has istio injection label)
@[15-17,zoom-15](modify production namespace for istio injection)
@snapend

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

@snap[south span-100 text-15 text-gold]
@[1-3,zoom-10](Import existing app directly from github)
@[5-6,zoom-10](Monitor triggered pipeline that deploys to Staging)
@[8-9,zoom-10](Monitor the staging repo changes.)
@snapend

---

@title[Configure Canary Settings]
@snap[north span-100]
## @css[text-yellow](  <br> Canary Deployment Goals   @fa[project-diagram])
@snapend

@snap[west font-raleway span-50 text-left]
We will deploy new app features to production and to only 20% of our users while monitoring traffic @emoji[chart_with_upwards_trend] for 60 seconds.
@snapend


@snap[east font-raleway span-50 text-left]
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
@snap[south span-100 text-15 text-gold]
@[1,zoom-10](Set environment variable for canary)
@[3-5,zoom-10](Let's monitor the production git repo for changes)
@[7-10,zoom-08](clone production repo and cd into directory)
@snapend

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
@snap[south span-100 text-15 text-gold]
@[1-13,zoom-10](Run this command on our terminal. In root of repo directory.)
@[15-16,zoom-09](Add our changes, commit and push to repo.)

@snapend

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

@title[View Metrics in Grafana - Configure]
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
@title[View Metrics in Grafana - Configure]
## @css[text-yellow](<br>Using Grafana  @fa[paint-roller])

```bash
# create ingress for Grafana
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
          serviceName: grafana
          servicePort: 3000
" | kubectl create -f -

open "http://flagger-grafana.$LB_IP.nip.io"
```


---

@title[View Metrics in Grafana - Configure]
@snap[north span-100]
## @css[text-yellow](<br>Using Grafana  @fa[paint-roller])
#### Configure Dashboard
@snapend

@snap[middle]
@ul[list-spaced-bullets list-boxed-bullets text-gold text-07]
- In Grafana Dashoard, on left nav select **Explore**
- Select Flagger, and pick *flagger_canary_status* , *flagger_canary_weight* and *flagger_canary_total*
- Select any other items you want on the dashboard
@ulend
@snapend

---
@title[Questions]
@snap[north span-100]
## @css[text-yellow](Got Questions   @fa[question])
@snapend
# Q&A
@emoji[tada]