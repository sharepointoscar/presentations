from diagrams import Cluster, Diagram
from diagrams.k8s.compute import Pod, StatefulSet, Deployment, Cronjob, ReplicaSet
from diagrams.k8s.network import Service
from diagrams.k8s.group import Namespace
from diagrams.k8s.storage import PV, PVC, StorageClass

diagram_attr = {
    "fontsize": "65",
    "fontcolor": "#ffffff",
    "bgcolor": "transparent"
}
with Diagram("Cron Jobs and Deployments", filename="jx_kubernetes_cluster", 
show=False,outformat="svg",direction="LR",graph_attr=diagram_attr):

    with Cluster("Jenkins X"):
        jx_namespace = Namespace("jx")
    
        with Cluster("CronJobs"):
            [Cronjob("gcactivities"),
                Cronjob("gcpods"),
                Cronjob("gcpreviews")] >> jx_namespace


        with Cluster("Deployments"):
            [Deployment("Crier"),Deployment("Hook"),Deployment("Deck"),
                Deployment("Horologium"),Deployment("chartmuseum"),
                Deployment("controllerbuild"),Deployment("controllerrole"),
                Deployment("heapster"),Deployment("nexus"),
                Deployment("pipeline")] >> jx_namespace
        
        with Cluster("ReplicaSets",direction="TB"):

            [ReplicaSet("Crier"),ReplicaSet("Deck"),
                    ReplicaSet("Hook"),ReplicaSet("Horologium")] >> jx_namespace
