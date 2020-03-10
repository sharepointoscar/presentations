---?image=assets/img/jx-artwork/jx-robocat.png&position=-28% 15%&size=55% 100%

@snap[ text-right]
## Introduction to Jenkins X
### a beginner's guide
@snapend


---
@title[What is Jenkins X?]

@snap[west]
# What is Jenkins X?
@snapend

@snap[east fragment]
![height=500px,filter=blur,title=Jenkins is NOT Jenkins X](assets/img/jx-artwork/jenkins.png)
@snapend

@snap[east fragment]
@fa[ban fa-10x text-red]
@snapend

---
@title[What is Jenkins X? - why it is not Jenkins X]
---?image=assets/img/jx-artwork/jx-robocat.png&position=-28% 15%&size=55% 100%

@snap[east span-60]
@ol[list-spaced-bullets list-boxed-bullets text-gold text-08]
1. Completely new code-base         @fa[code-branch fa-3x text-yellow]
2. Zero code from Jenkins           @fab[creative-commons-zero fa-3x text-yellow]
3. Kubernetes Native                @fa[dharmachakra fa-3x text-yellow]
4. Different architecture           @fa[vihara fa-3x text-yellow]
@olend
@snapend


---
@title[What is Jenkins X? - why it is not Jenkins X]

@snap[east fragment]
![half,height=500px,filter=blur,title=Jenkins is NOT Jenkins X](assets/img/jx-artwork/jenkins-v-jenkinsx.png)
@snapend
@snap[east fragment]
![half,height=500px,title=Jenkins is NOT Jenkins X](assets/img/jx-artwork/jenkins-v-jenkinsx.png)
@snapend


@snap[west span-55]
@quote[Jenkins X is Jenkins’ spiritual counterpart for the cloud-native world](CloudBees)
@snapend

---
@title[Jenkins X - Kubernetes Native CI/CD]
---?image=assets/img/jx-artwork/jx-captain.png&position=-15% 15%&size=55% 100%

@snap[east span-69]
 @css[jx-header text-uppercase text-20 text-shadow](Jenkins) @css[jx-header text-uppercase text-bold text-20 text-shadow](X)  
## is an @css[text-bold](opinionated)

@css[font-lato-light](Kubernetes @fa[dharmachakra text-yellow] native)

##  CI/CD platform
@css[text-10 thin-text](Comprised of many open-source frameworks)
@snapend

---
@title[What is Jenkins X? - Multi Cloud]

@snap[east]
## Runs on the Three Leading Clouds
@snapend

@snap[west span-80 fragment]
![width=300,title=Azure](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Microsoft_Azure_Logo.svg/1200px-Microsoft_Azure_Logo.svg.png)
@snapend

@snap[east-south span-88 fragment]
![width=200,title=GCP](https://seeklogo.com/images/G/google-cloud-logo-6B950E8ADB-seeklogo.com.png)
@snapend

@snap[west-south span-90 fragment]
![height=280px,title=AWS,position=60%](https://www.sinefa.com/wp-content/uploads/2019/03/AWS-Logo-White.png)
@snapend

---

@title[What is Jenkins X? - Tekton as Pipeline Exec Engine]
---?image=assets/img/jx-artwork/jx-tekton-engine.png&position=-28% 15%&size=55% 100%

@snap[east]
## Tekton is the @fa[heartbeat fa-3x pulsingheart] 
## of the Pipeline
## Execution Engine
@snapend

@title[What is Jenkins X? - Diagram]
---?image=assets/img/jx-artwork/jx-tekton-engine.png&position=-28% 15%&size=55% 100%

@snap[east span-80]
#### Jenkins X Abstracts you from Tekton Intricacies 
![height=450px](assets/img/jxpipeline-to-tekton.png)
@snapend

@title[Jenkins X - Preview Environments]
---?image=assets/img/jx-artwork/jx-xoltar.png&position=left 45%&size=40%

@snap[east span-70]
##  Preview Environments give you a glimpse into the future!

#### PMs and Designers preview your work.  You make sure your code is working.

@css[text-06 thin-text text-italic]([ Namespaced Ingress, Pod running your latest app version ] )

@snap[west-south]
![height=100px](assets/img/k8s-icons/resources/labeled/ns.svg)
![height=100px](assets/img/k8s-icons/resources/labeled/ing.svg)
![height=100px](assets/img/k8s-icons/resources/labeled/pod.svg)
@snapend

@snapend