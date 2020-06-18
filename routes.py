from flask import Flask,request
from kubernetes import client,config

app=Flask(__name__)

@app.route("/deployment",methods=["POST"])
def deployment():
    data = request.get_json()
    metadata_name = data["metadata_name"]
    replicas = data["replicas"]
    container_name = data["container_name"]
    container_image =  data["container_image"]
    container_port = data["container_port"]

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

    #define container
    container = client.V1Container()
    container.name=  container_name
    container.image= container_image
    container. ports = [client.V1ContainerPort(container_port=container_port)]

    #create deployment
    spec.template.spec.containers = [container]
    deployment.spec = spec



if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")