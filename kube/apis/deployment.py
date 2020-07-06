from kubernetes import client,config

def create_deployment(metadata_name,labels,container_name,container_image,container_port,replicas):
    if os.getenv('KUBERNETES_SERVICE_HOST'):
        config.load_incluster_config()
    else:
        config.load_kube_config()
    kube_client = client.ApiClient()

    deploy = client.V1Deployment()

    deploy.api_version = "apps/v1"
    deploy.kind = "Deployment"
    deploy.metdata = client.V1ObjectMeta(name=metadata_name)

    #define spec
    spec = client.V1DeploymentSpec()
    spec.replicas = replicas 

    spec.template = client.V1PodTemplateSpec()
    spec.template.metadata = client.V1ObjectMeta(labels=labels)
    spec.template.spec = client.V1PodSpec()

    #define container
    container = client.V1Container()
    container.name=  container_name
    container.image= container_image
    container. ports = [client.V1ContainerPort(container_port=container_port)]

    #create deployment
    spec.template.spec.containers = [container]
    deployment.spec = spec

    kube_client.create_namespaced_deployment(namespace="default",body=deployment)

    return 200

def delete_deployment(deployment_name):
    if os.getenv('KUBERNETES_SERVICE_HOST'):
        config.load_incluster_config()
    else:
        config.load_kube_config()
    kube_client = client.ApiClient()

    try:
        deploy = kubecli.AppsV1Api()
        deploy.delete_namespaced_deployment(name=deployment_name, 
        namespace="default", body=kubecli.V1DeleteOptions(propagation_policy="Foreground", grace_period_seconds=5))
        return 200
    except Exception as e:
        print(e)
        return 400

