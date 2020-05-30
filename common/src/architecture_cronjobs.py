from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Pod, StatefulSet, Deployment, Cronjob, ReplicaSet
from diagrams.k8s.network import Service
from diagrams.k8s.group import Namespace
from diagrams.k8s.rbac import ClusterRole
from diagrams.k8s.rbac import ClusterRoleBinding
from diagrams.k8s.others import CRD
from diagrams.k8s.storage import PV, PVC, StorageClass
import subprocess
import os, json
from kubernetes import client, config

diagram_attrib = {
    "labelloc": "t",
    "fontsize": "65",
     "penwidth": "2.5",
   # "bgcolor": "transparent",
    "fontname": "Helvetica Neue"
}       

node_attrib = {
    "fontsize": "15",
    "fontname": "Helvetica Neue Medium"

}
edge_attrib = {
    "style": "bold",
    "color": "#4a4e52"
}

with Diagram("Cron Jobs and CRDs", filename="cronjobs_crds",show=True,outformat="png",direction="TB",graph_attr=diagram_attrib):

    with Cluster("Jenkins X"):
        jx_namespace = Namespace("jx")
    
        with Cluster("CronJobs"):
            [Cronjob("gcactivities"),
                Cronjob("gcpods"),
                Cronjob("gcpreviews")] >> jx_namespace

        with Cluster("CRDs"):
            with Cluster("Tekton"):

                [CRD("clustertasks.tekton.dev"),CRD("conditions.tekton.dev"),CRD("extensions.dashboard.tekton.dev"),
                CRD("pipelineresources.tekton.dev"),CRD("pipelineruns.tekton.dev"),CRD("pipelines.tekton.dev"),
                CRD("taskruns.tekton.dev"),CRD("tasks.tekton.dev")] >> jx_namespace

            with Cluster("jenkins-x",direction="RL"):
                crds = []
                cmd = ["kubectl get crds","-n jx", "-o json","| jq -r '.items[] | select(.spec?) | select(.spec.group == \"jenkins.io\") .metadata.name '"]
                crd_json = subprocess.run(" ".join(cmd),stdout=subprocess.PIPE,shell=True,universal_newlines=False)
            
                # store cluster roles in array
                for crd in crd_json.stdout.decode('utf-8').splitlines():
                    #print(crd)
                    crds.append(CRD(crd))
                
                #  add array to namespace
                crds >> jx_namespace
        
        with Cluster("Cluster Roles"):
            cluster_roles = []
            cmd = ["kubectl get clusterrole", "-n jx", "-o json","| jq -r '.items[] | select(.metadata.annotations[] | contains(\"jenkins.io/chart\") ) .metadata.name '"]
            response_json = subprocess.run(" ".join(cmd),stdout=subprocess.PIPE,shell=True,universal_newlines=False)
           
            # store cluster roles in array
            for role in response_json.stdout.decode('utf-8').splitlines():
                cluster_roles.append(ClusterRole(role))
             
            #  add array to namespace
            cluster_roles >> jx_namespace






