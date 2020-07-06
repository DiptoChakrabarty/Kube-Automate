from kubernetes import client,config

def create_ingress():
    if os.getenv('KUBERNETES_SERVICE_HOST'):
        config.load_incluster_config()
    else:
        config.load_kube_config()
    kube_client = client.ApiClient()

    ingress = client.ExtensionV1betaApi()
    namespace= "default"
    
