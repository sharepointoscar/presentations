---?image=assets/img/jx-artwork/jx-robocat.png&position=-28% 15%&size=55% 100%

@snap[text-right]
## Intro to @css[jx-header]( Jenkins X)
### a beginner's guide
@snapend

---
@title[Let me take you on a Jenkins X Boat Tour]

@snap[center]
## Lets explore Jenkins X!!
@snapend

@snap[center]
![height=500px,title=Jenkins is NOT Jenkins X](assets/img/jx-artwork/jx-boat-tours.png)
@snapend

---
@title[What is Jenkins X?]
@transition[fade]

@snap[west]
# What is Jenkins X?
@snapend

@snap[east fragment]
![height=500px,title=Jenkins is NOT Jenkins X](assets/img/jx-artwork/jenkins.png)
@snapend

@snap[east fragment]
@fa[ban fa-10x text-red]
@snapend

---
@title[What is Jenkins X? - why it is not Jenkins X]
@transition[fade]
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
@transition[fade]
@snap[east fragment]
![half,height=500px,title=Jenkins is NOT Jenkins X](assets/img/jx-artwork/jenkins-v-jenkinsx.png)
@snapend


@snap[west text-smallcaps font-lato-thin span-55]
@css[](Jenkins X is Jenkins’ spiritual counterpart for the cloud-native world)

The concept of pipelines and extensibility is what they have in common.  

@css[text-bold text-gold text-15](That is it!)
@snapend


---
@title[Jenkins X - Kubernetes Native CI/CD]
---?image=assets/img/jx-artwork/jx-captain.png&position=-15% 15%&size=55% 100%

@snap[east span-69]
 @css[jx-header text-uppercase text-20 text-shadow](Jenkins) @css[jx-header text-uppercase text-bold text-20 text-shadow](X)  
## is an @css[text-bold](opinionated)

@css[font-lato-light](Kubernetes @fa[dharmachakra text-yellow] native)

##  CI/CD platform
@css[text-10 thin-text](Comprised of many open-source technologies)
@snapend

---
@title[What is Jenkins X? - Multi Cloud]
---?image=assets/img/jx-artwork/jx-tour-poster.png&position=2% 45%&size=25%

@snap[center-north text-right]
## Runs on the Three Leading Clouds
@snapend

@snap[west-south span-66 fragment]
![height=280px,title=AWS,position=5px](https://www.sinefa.com/wp-content/uploads/2019/03/AWS-Logo-White.png)
@snapend

@snap[east-north span-88 fragment]
![width=200,title=GCP](https://seeklogo.com/images/G/google-cloud-logo-6B950E8ADB-seeklogo.com.png)
@snapend

@snap[south-east fragment]
![width=300,title=Azure](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Microsoft_Azure_Logo.svg/1200px-Microsoft_Azure_Logo.svg.png)
@snapend

---

@title[What is Jenkins X? - Tekton as Pipeline Exec Engine]
---?image=assets/img/jx-artwork/jx-tekton-engine.png&position=-28% 15%&size=55% 100%

@snap[east]
## Tekton is the @fa[heartbeat fa-3x pulsingheart] 
## of the Pipeline
## Execution Engine
@snapend


@title[What is Jenkins X? - Pipelines]
---?image=assets/img/jx-artwork/jx-tekton-engine.png&position=-28% 15%&size=55% 100%

@snap[east span-78]
@ol[list-spaced-bullets list-boxed-bullets text-gold text-08]
1. Pipelines are declarative (YAML)             @fa[code fa-3x text-yellow]
2. Stages run on their own ephemeral pod        @fa[box fa-3x text-yellow]
3. Kubernetes Native                            @fa[dharmachakra fa-3x text-yellow]
@olend
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

@title[Jenkins X - Preview Environments]
---?image=assets/img/jx-artwork/jx-robocat.png&position=left 45%&size=40%

@snap[east span-70]
##  ChatOps

#### Jenkins X Bot automatically comments on your Commits, Issues and Pull Requests

@css[text-06 thin-text text-italic]([ Use your Git Provider built-in UI ] )

@snap[west-south text-blue]
@fa[git-square fa-3x] @fa[github-square fa-3x]
@snapend

@snapend


@title[Jenkins X - QuickStarts]
---?image=assets/img/jx-artwork/jx-robocat.png&position=left 45%&size=40%

@snap[east span-70]
##  QuickStarts

#### Kick the tires without writing a single line of code.

@css[text-06 thin-text text-italic]([ Namespaced Ingress, Pod running sampled app ] )

@snap[west-south]
![height=100px](assets/img/k8s-icons/resources/labeled/ns.svg)
![height=100px](assets/img/k8s-icons/resources/labeled/ing.svg)
![height=100px](assets/img/k8s-icons/resources/labeled/pod.svg)
@snapend

@snapend

@title[Jenkins X - DevPods]
---?image=assets/img/jx-artwork/jx-devpods.png&position=left 45%&size=40%

@snap[east span-70]
##  DevPods

#### develop in the cloud via a kubernetes devpod.

@css[text-06 thin-text text-italic]([   Ingress, Pod with your project files synched, modify live ] )

@snap[west-south]
![height=100px](assets/img/k8s-icons/resources/labeled/ns.svg)
![height=100px](assets/img/k8s-icons/resources/labeled/ing.svg)
![height=100px](assets/img/k8s-icons/resources/labeled/pod.svg)
@snapend

@snapend

@title[Jenkins X - Build Packs]
---?image=assets/img/jx-artwork/jx-robocat.png&position=left 45%&size=40%

@snap[east span-70]
##  Build Packs

#### pipeline templates based on the language your app runs.

@css[text-06 thin-text text-italic]([ Namespaced Ingress, Pod running your latest app version ] )

@snap[west-south]
![height=100px](assets/img/k8s-icons/resources/labeled/ns.svg)
![height=100px](assets/img/k8s-icons/resources/labeled/ing.svg)
![height=100px](assets/img/k8s-icons/resources/labeled/pod.svg)
@snapend

@snapend

@title[Jenkins X - Serverless Deployments]
---?image=assets/img/jx-artwork/jx-serverless.png&position=left 45%&size=40%

@snap[east span-70]
##  Serverless Deployments

#### Knative spin up/down based on traffic demand.

@css[text-06 thin-text text-italic]([ Namespaced Ingress, Pods running your latest app version ] )

@snap[west-south]
![height=100px](assets/img/k8s-icons/resources/labeled/ns.svg)
![height=100px](assets/img/k8s-icons/resources/labeled/ing.svg)
![height=100px](assets/img/k8s-icons/resources/labeled/pod.svg)
@snapend

@snapend

@title[Jenkins X - GitOps]
---?image=assets/img/jx-artwork/jx-gitops.png&position=left 45%&size=40%

@snap[east span-70]
##  GitOps

#### git as single source of truth for everything.
@css[text-06 text-gold]( jx uses gitops to manage its own config)

@css[text-06 thin-text text-italic]([ git repositories hold all configuration ] )

@snap[west-south text-blue]
@fa[git-square fa-3x] @fa[github-square fa-3x]
@snapend

@snapend

---

@title[Questions]
@snap[north span-100]
## @css[text-yellow](Got Questions   @fa[question])
@snapend
# Q&A
@emoji[tada]