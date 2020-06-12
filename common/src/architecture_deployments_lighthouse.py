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

with Diagram("Deployments",outformat="svg",filename="deployments_lighthouse",show=True,
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

        with Cluster("Lighthouse",graph_attr={"fontsize": "47"}):
           # logo_node = custom.Custom("","assets/img/logos/logo_prow.png")
            with Cluster("foghorn"):
                svc_foghorn_hook = Service("hook")
                pod_foghorn = Pod("foghorn")
                secret_foghorn = Secret("foghorn")
                token_foghorn = Secret("hmac-token")
                token_oauth_foghorn = Secret("oauth-token")
                sa_foghorn = ServiceAccount("lighthouse")
   
                pod_foghorn - Edge(color="gray", style="dashed") - secret_foghorn - Edge(color="gray", style="dashed")  - token_foghorn- Edge(color="gray", style="dashed")  - sa_foghorn
                svc_foghorn_hook >> pod_foghorn
                
            with Cluster("Keeper"):
                svc_keeper = Service("keeper")

                pod_keeper = Pod("keeper")
                secret_keeper = Secret("keeper")
                token_oauth_keeper = Secret("oauth-token")
                sa_keeper = ServiceAccount("keeper")

                pod_keeper - Edge(color="gray", style="dashed") - secret_keeper - Edge(color="gray", style="dashed")  - token_oauth_keeper - Edge(color="gray", style="dashed")  - sa_keeper

                svc_keeper >> pod_keeper
                
            with Cluster("Webhooks"):
                svc_hook = Service("hook")

                pod_hook = Pod("hook")
                secret_hook = Secret("hook")
                token_hook = Secret("webhooks-token")
                hmac_token_hook = Secret("hmac-token")
                oauth_token_hook = Secret("oauth-token")
                sa_hook = ServiceAccount("webhooks")

                pod_hook - Edge(color="gray", style="dashed") - secret_hook - Edge(color="gray", style="dashed")  - hmac_token_hook - Edge(color="gray", style="dashed")  - token_hook - Edge(color="gray", style="dashed") - oauth_token_hook - Edge(color="gray", style="dashed")  - sa_hook
                svc_hook >> pod_hook


        with Cluster("Tekton Controller"):
            tekton_controller = custom.Custom("Tekton","assets/img/logos/tekton.png")
            pod_tekton_controller = Pod("tekton")
            token_tekton_controller = Secret("tekton-pipeline-token")
            sa_tekton_controller = ServiceAccount("tekton-pipeline")
            config_volume_tekton_controller  = PV("config-logging")

            pod_tekton_controller - Edge(color="gray", style="dashed") - token_tekton_controller  
            pod_tekton_controller  - Edge(color="gray", style="dashed") - sa_tekton_controller 
            pod_tekton_controller  - Edge(color="gray", style="dashed") - config_volume_tekton_controller 

            Deployment("tekton-pipeline-controller") << Edge(style="bold") << pod_tekton_controller  << Edge(color="orange",style="bold") << ReplicaSet("tekton")  << Edge(style="bold")

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

        with Cluster("Vault-Operator"):
            svc_vault_operator  = custom.Custom("vault-operator","assets/img/logos/vault.png")
            
            pod_vault_operator = Pod("vault")
            secret_vault_operator = Secret("vault-token")
            sa_vault_operator = ServiceAccount("vault")

            pod_vault_operator - Edge(color="gray", style="dashed") - secret_vault_operator - Edge(color="gray", style="dashed")  - Edge(color="gray", style="dashed")  - sa_vault_operator
            svc_vault_operator >> pod_vault_operator

        with Cluster("Vault-Configurator"):
            svc_vault_configurator  = custom.Custom("vault-configurator","assets/img/logos/vault.png")
            
            pod_vault_configurator = Pod("vault")
            secret_vault_configurator = Secret("jx-vault")
            secret_token_vault_configurator = Secret("jx-vault-token")
            sa_vault_configurator = ServiceAccount("jx-vault")

            pod_vault_configurator - Edge(color="gray", style="dashed") - secret_vault_configurator - Edge(color="gray", style="dashed") - secret_token_vault_configurator - Edge(color="gray", style="dashed")  - sa_vault_configurator
            svc_vault_configurator >> pod_vault_configurator


    # TOD: confirm with core team if we use one ingress with annotations vs multiple ingress resources
    # for now, use one ingress
        svc_vault_operator << Edge(color="orange",style="bold") << ReplicaSet("vault-operator")  << Edge(style="bold") << Deployment("vault-operator")
        svc_keeper << Edge(color="orange",style="bold") << ReplicaSet("keeper")  << Edge(style="bold") << Deployment("keeper")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_chartmuseum << Edge(color="orange",style="bold") << ReplicaSet("chartmuseum") << Edge(style="bold")  << Deployment("chartmuseum")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_hook << Edge(color="orange",style="bold") << ReplicaSet("webhooks")  << Edge(style="bold") << Deployment("webhooks")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_foghorn_hook << Edge(color="orange",style="bold") << ReplicaSet("foghorn")  << Edge(style="bold") << Deployment("foghorn")
        
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_controllerbuild << Edge(color="orange",style="bold") << ReplicaSet("controllerbuild")  << Edge(style="bold") << Deployment("controllerbuild")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_controllerrole << Edge(color="orange",style="bold") << ReplicaSet("controllerrole")  << Edge(style="bold") << Deployment("controllerrole")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_heapster << Edge(color="orange",style="bold") << ReplicaSet("heapster")  << Edge(style="bold") << Deployment("heapster")
        ing_chartmuseum >> Edge(color="darkgreen",style="bold") >> svc_nexus << Edge(color="orange",style="bold") << ReplicaSet("nexus")  << Edge(style="bold") << Deployment("nexus")
