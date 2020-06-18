from flask import Flask,request,jsonify
from kubernetes import client,config

app=Flask(__name__)

@app.route("/deploy",methods=["POST"])
def deployment():
    data = request.get_json()
    metadata_name = data["metadata_name"]
    replicas = data["replicas"]
    container_name = data["container_name"]
    container_image =  data["container_image"]
    container_port = data["container_port"]
    labels = data["labels"]

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

    ret = {
        "Status": 200,
        "Msg": "Deployment Successful"
    }

    return jsonify(ret)

@app.route("/service",methods=["POST"])
def service():
    data = request.get_json()
    metadata_name = data["metadata_name"]
    selectors = data["selectors"]
    port = data["port"]
    target_port = data["target_port"]

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

    spec.ports = [client.V1ServicePort(protocol="TCP",port=port , target_port=target_port)]
    svc.spec = spec

    kube_client.create_namespaced_service(namespace="default",body=svc)

    ret = {
        "Status": 200,
        "Msg": "Service up  Successfully"
    }

    return jsonify(ret)




if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")