![IMAGE](assets/img/jx-logo.svg)

## Continuous Delivery with Jenkins X

---
@title[Continuous Delivery with Jenkins X - Agenda]
# Agenda

@snap[fragment]
@ul[list-spaced-bullets list-boxed-bullets text-gold text-07]
- Creating a GKE Cluster
- Install Jenkins X
- Explore built-in QuickStarts
- Importing an existing app (https://github.com/jenkins-oscar/skiapp)
- Customizing the declarative YAML pipeline
- Working with Pull Requests and Preview Environments
- Promote app to Production
@ulend
@snapend

@snap[fragment text-right south-east span-55]
@box[bg-orange text-white text-right rounded box-padding](@fa[info-circle fa-2x] About Our Schedule Today#The agenda only a rough estimation. Depending on how fast we progress, we might be able to cover more or less of the items listed below.<br><br>There will be an hour break for lunch, and shorter periodic breaks approximatelly once an hour.)
@snapend


---
@title[Hands on Time!]

@snap[text-shadow text-yellow text-30 font-raleway-heavy]
Lab @fa[hourglass-start fa-1x] Time!
@snapend
@css[font-quicksand](the terminal is going to be your BFF @emoji[sparkling_heart] for a while...)

---
@title[Install CLI]

## Install JX CLI   @css[text-yellow](@fa[terminal])

@code[bash zoom-12 code-reveal-slow code-wrap](workshops/continuous-delivery-jx/install-cli.sh)

@snap[south span-100 text-15 text-gold]
@[3,zoom-06](download cli, untar it.)
@[6,zoom-15](move binary to bin.)
@[9-16,zoom-06]()
@snapend

---
@title[Create GKE Cluster]
@snap[north span-100]
## @css[text-yellow](Create a GKE Cluster   @fa[server])
@snapend
@code[bash zoom-12 code-wrap](workshops/continuous-delivery-jx/create-cluster.sh)

@snap[fragment text-right south-east span-55]
@box[bg-orange text-white rounded box-padding](@fa[info-circle fa-2x] Cluster Provisioning...#You can use Terraform or any other method, you do not need to use the JX CLI.)
@snapend

--- 

@title[Install Jenkins X]

@snap[north span-100]
## @css[text-yellow](Install Jenkins X   @fa[github])
@snapend

@snap[south span-100]
@code[bash ](workshops/continuous-delivery-jx/boot-cluster.sh)
@snapend
@snap[south span-100 text-gold]
@[1](set $CLUSTER_NAME environment variable.)
@[3-7](clone config repo and cd into it.)
@[9-14](change `jx-requirements.yaml` fields.)
@[15]
@snapend

--- 

@title[Create QuickStart]

@snap[north span-100]
## @css[text-yellow](Jenkins X QuickStarts   @fa[skiing])
@snapend

@snap[text-center text-06]
QuickStarts allow you to go fast...
@snapend


@code[bash zoom-13 code-wrap](workshops/continuous-delivery-jx/create-quickstart.sh)

@snap[south span-100 text-15 text-gold]
@[3,zoom-18](create quickstart using a Wizard.)
@[5](pass parameters and just do it!)
@[9,zoom-20](Let's view pipeline activity.)
@[12,zoom-20]()
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
jx import --url https://github.com/jenkins-oscar/skiapp.git
```
@snapend

---
@title[Customize Pipeline]
@snap[north span-100]
## @css[text-yellow](Customize YAML Pipeline   @fa[wrench])

@snap[text-center text-06 span-100]
@css[text-bold](SCENARIO:) we add a k8s secret, then retrieve it in the pipeline.
@snapend
@snapend

@code[bash zoom-13 code-wrap](workshops/continuous-delivery-jx/pr-custom-pipeline.sh)

@snap[south span-100 text-15 text-gold]
@[1,zoom-13](add secret to kubernetes, jx and jx-staging namespaces)
@[3,zoom-13](create feature branch)
@snapend

---

@title[Customize Pipeline]
@snap[north span-100]
## @css[text-yellow](Closer look at the YAML   @fa[wrench])
@snapend

@code[yaml zoom-05 code-max](workshops/continuous-delivery-jx/pipeline.yaml)

@snap[south span-100 text-15 text-gold]
@[4-8,zoom-20](Store ClientID in ENV VAR)
@[9-13,zoom-20](Store ClientSecret in ENV VAR)
@[20-21,zoom-10](Output clientID value to logs)
@[22-23,zoom-10](Output clientSecret value to logs)
@snapend

---

@title[Working with Pull Requests & Preview Envs]

@snap[north-west span-45]
@box[bg-green text-white box-padding](1. Create Feature Branch#Create feature branch, make changes, Preview Environment created, folks comment.)
@snapend

@snap[north-east span-35]
@box[bg-orange text-white rounded box-padding](2. Feature Complete?#Submit PR, ChatOps kicks in as PR is not approved by default, needs others to review.)
@snapend

@snap[south-east span-35]
@box[bg-pink text-white box-padding](3. PR Approved#Someone who is an Approver finally approves PR.)
@snapend

@snap[south-west span-35]
@box[bg-blue text-white waved box-padding](4. Promote to Staging#After PR is approved, pipeline is triggered to promote app to *Staging* environment.)
@snapend

@snap[midpoint]
@fa[refresh fa-3x]
@snapend

---

@title[Promote an App to Production]
@snap[north span-100]
## @css[text-yellow](Promote App to Production   @fa[laptop-code])
@snapend

---

@title[Creating Custom Build-Packs]
@snap[north span-100]
## @css[text-yellow](Creating Custom Build Packs   @fa[laptop-code])
@snap[text-center text-06]
If you have specific needs, build a custom build pack and reuse it!
#https://blog.testproject.io/2019/10/29/create-custom-build-packs-for-jenkins-x/
@snapend
@snapend

---