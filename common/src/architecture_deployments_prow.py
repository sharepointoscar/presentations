from diagrams import Cluster, Diagram, Edge, Node, custom
from diagrams.k8s.compute import Pod, StatefulSet, ReplicaSet, Deployment
from diagrams.k8s.network import Service, Ingress
from diagrams.onprem.network import Nginx
from diagrams.k8s.storage import PV, PVC, StorageClass
from diagrams.k8s.podconfig import Secret, ConfigMap
from diagrams.k8s.rbac import ServiceAccount
from diagrams.gcp.devtools import GCR 
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

with Diagram("Deployments",outformat="svg",filename="deployments_prow",show=True,
graph_attr=diagram_attrib,node_attr=node_attrib,edge_attr=edge_attrib,direction="TB"):
    with Cluster("Deployments",graph_attr={"fontsize": "67"}):
        ing_chartmuseum = Nginx("Ingress") 
        #ing_deck = Nginx("deck") 
        #ing_hook = Nginx("hook")
        #ing_crier = Nginx("crier")

        with Cluster("Registries",graph_attr={"fontsize": "47"}):
            with Cluster("Nexus"):
                svc_nexus = custom.Custom("Nexus","assets/img/logos/logo_nexus.png")

                pod_nexus = Pod("nexus")
                secret_nexus = Secret("nexus")
                token_nexus = Secret("default-token")
                sa_nexus = ServiceAccount("default")
                data_volume = PVC("nexus-data-volume")
                config_volume_nexus = PV("nexus")
                configmap_nexus = ConfigMap("nexus")

                pod_nexus - Edge(color="gray", style="dashed") - secret_nexus - Edge(color="gray", style="dashed")  - token_nexus - Edge(color="gray", style="dashed")  - sa_nexus
                pod_nexus - Edge(color="gray", style="dashed") - config_volume_nexus

                svc_nexus >> pod_nexus

            with Cluster("Chartmusem"):
                svc_chartmuseum = custom.Custom("Chartmuseum","assets/img/logos/logo_chartmuseum.png")

                pod = Pod("chartmuseum")
                secret = Secret("chartmuseum")
                token = Secret("default-token")
                sa = ServiceAccount("default")    

                pod - Edge(color="gray", style="dashed")  - secret  - Edge(color="gray", style="dashed")  - token  - Edge(color="gray", style="dashed")  - sa
                svc_chartmuseum >> pod

            with Cluster("Docker"):
                svc_docker_registry = custom.Custom("Docker Registry","assets/img/logos/logo_docker.png")

        with Cluster("Prow",graph_attr={"fontsize": "47"}):
           # logo_node = custom.Custom("","assets/img/logos/logo_prow.png")
            with Cluster("Tide"):
                svc_tide = Service("tide")

                pod_tide = Pod("tide")
                secret_tide = Secret("tide")
                token_tide = Secret("default-token")
                sa_tide = ServiceAccount("default")
                oauth_volume_tide = PV("oauth")
                config_volume_tide = PV("config")

                pod_tide - Edge(color="gray", style="dashed") - secret_tide - Edge(color="gray", style="dashed")  - token_tide - Edge(color="gray", style="dashed")  - sa_tide
                pod_tide - Edge(color="gray", style="dashed") - oauth_volume_tide - Edge(color="gray", style="dashed") - config_volume_tide

                svc_tide >> pod_tide
                
            with Cluster("Crier"):
                svc_crier = Service("crier")

                pod_crier = Pod("hook")
                secret_crier = Secret("hook")
                token_crier = Secret("default-token")
                sa_crier = ServiceAccount("default")
                oauth_volume_crier = PV("oauth")
                config_volume_crier = PV("config")

                pod_crier - Edge(color="gray", style="dashed") - secret_crier - Edge(color="gray", style="dashed")  - token_crier - Edge(color="gray", style="dashed")  - sa_crier
                pod_crier - Edge(color="gray", style="dashed") - oauth_volume_crier - Edge(color="gray", style="dashed") - config_volume_crier

                svc_crier >> pod_crier
                
            with Cluster("Deck"):
                svc_deck = Service("deck")

                pod_deck = Pod("deck")
                secret_deck = Secret("deck")
                token_deck = Secret("default-token")
                sa_deck = ServiceAccount("default")
                config_volume_deck = PV("config")

                pod_deck - Edge(color="gray", style="dashed") - secret_deck - Edge(color="gray", style="dashed")  - token_deck - Edge(color="gray", style="dashed")  - sa_deck
                pod_deck - Edge(color="gray", style="dashed") - config_volume_deck
                svc_deck >> pod_deck

            with Cluster("Hook"):
                svc_hook = Service("hook")

                pod_hook = Pod("hook")
                secret_hook = Secret("hook")
                token_hook = Secret("default-token")
                hmac_token_hook = Secret("hmac-token")
                oauth_token_hook = Secret("oauth-token")
                sa_hook = ServiceAccount("default")

                pod_hook - Edge(color="gray", style="dashed") - secret_hook - Edge(color="gray", style="dashed")  - hmac_token_hook - Edge(color="gray", style="dashed")  - token_hook - Edge(color="gray", style="dashed") - oauth_token_hook - Edge(color="gray", style="dashed")  - sa_hook
                svc_hook >> pod_hook


        with Cluster("Horologium"):
            svc_horologium = Service("horologium")

            pod_horologium = Pod("horologium")
            secret_horologium = Secret("horologium-token")
            sa_horologium = ServiceAccount("horologium")

            pod_horologium - Edge(color="gray", style="dashed") - secret_horologium - Edge(color="gray", style="dashed") - sa_horologium
            svc_horologium >> pod_horologium

        with Cluster("Pipeline"):
           
            pod_pipeline = Pod("pipeline")
            token_pipeline = Secret("pipeline-token")
            sa_pipeline = ServiceAccount("pipeline")
            config_volume_pipeline = PV("config")

            pod_pipeline- Edge(color="gray", style="dashed") - token_pipeline  
            pod_pipeline - Edge(color="gray", style="dashed") - sa_pipeline 
            pod_pipeline - Edge(color="gray", style="dashed") - config_volume_pipeline

            Deployment("pipeline") << Edge(style="bold") << pod_pipeline << Edge(color="orange",style="bold") << ReplicaSet("pipeline")  << Edge(style="bold")

        with Cluster("Controllerbuild"):
            svc_controllerbuild = Service("controllerbuild")

            pod_controllerbuild = Pod("controllerbuild")
            secret_controllerbuild = Secret("controllerbuild-token")
            sa_controllerbuild = ServiceAccount("controllerbuild")

            pod_controllerbuild - Edge(color="gray", style="dashed") - secret_controllerbuild - Edge(color="gray", style="dashed")  - Edge(color="gray", style="dashed")  - sa_controllerbuild
            svc_controllerbuild >> pod_controllerbuild

        with Cluster("Controllerrole"):
            svc_controllerrole = Service("controllerrole")

            pod_controllerrole = Pod("controllerrole")
            secret_controllerrole = Secret("controllerrole-token")
            sa_controllerrole = ServiceAccount("controllerrole")

            pod_controllerrole - Edge(color="gray", style="dashed") - secret_controllerrole - Edge(color="gray", style="dashed")  - Edge(color="gray", style="dashed")  - sa_controllerrole
            svc_controllerrole >> pod_controllerrole


        with Cluster("Heapster"):
            svc_heapster = Service("heapster")

            pod_heapster = Pod("heapster")
            secret_heapster = Secret("heapster-token")
            sa_heapster = ServiceAccount("heapster")

            pod_heapster - Edge(color="gray", style="dashed") - secret_heapster - Edge(color="gray", style="dashed")  - Edge(color="gray", style="dashed")  - sa_heapster
            svc_heapster >> pod_heapster

    # TOD: confirm with core team if we use one ingress with annotations vs multiple ingress resources
    # for now, use one ingress
        svc_crier << Edge(color="orange",style="bold") << ReplicaSet("jenkins-x-crier")  << Edge(style="bold") << Deployment("jenkins-x-crier")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_chartmuseum << Edge(color="orange",style="bold") << ReplicaSet("chartmuseum") << Edge(style="bold")  << Deployment("chartmuseum")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_deck << Edge(color="orange",style="bold") << ReplicaSet("jenkins-x-deck")  << Edge(style="bold") << Deployment("jenkins-x-deck")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_hook << Edge(color="orange",style="bold") << ReplicaSet("jenkins-x-hook")  << Edge(style="bold") << Deployment("jenkins-x-hook")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_tide << Edge(color="orange",style="bold") << ReplicaSet("tide")  << Edge(style="bold") << Deployment("tide")
        
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_horologium << Edge(color="orange",style="bold") << ReplicaSet("horologium")  << Edge(style="bold") << Deployment("horologium")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_controllerbuild << Edge(color="orange",style="bold") << ReplicaSet("controllerbuild")  << Edge(style="bold") << Deployment("controllerbuild")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_controllerrole << Edge(color="orange",style="bold") << ReplicaSet("controllerrole")  << Edge(style="bold") << Deployment("controllerrole")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_heapster << Edge(color="orange",style="bold") << ReplicaSet("heapster")  << Edge(style="bold") << Deployment("heapster")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_nexus << Edge(color="orange",style="bold") << ReplicaSet("nexus")  << Edge(style="bold") << Deployment("nexus")
