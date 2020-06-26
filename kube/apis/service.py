from kubernetes import client,config

def create_service(metadata_name,port,target_port,selectors):
    if os.getenv('KUBERNETES_SERVICE_HOST'):
        config.load_incluster_config()
    else:
        config.load_kube_config()
    kube_client = client.ApiClient()

    svc = client.V1Service()

    svc.api_version = "v1"
    svc.kind = "Service"
    #metadata name
    svc.metadata = client.V1ObjectMeta(name = metadata_name)

    spec = client.V1ServiceSpec()
    spec.selector = selectors
    #add port details
    spec.ports = [client.V1ServicePort(protocol="TCP",port=port , target_port=target_port)]
    svc.spec = spec

    kube_client.create_namespaced_service(namespace="default",body=svc)

    return 200