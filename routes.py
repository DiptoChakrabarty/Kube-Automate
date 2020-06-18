from flask import Flask,request
from kubernetes import client,config

app=Flask(__name__)

@app.route("/deployment",methods=["POST"])
def deployment():
    data = request.get_json()



    if os.getenv('KUBERNETES_SERVICE_HOST'):
        config.load_incluster_config()
    else:
        config.load_kube_config()
    kube_client = client.ApiClient()

    deploy = client.V1Deployment()

    deploy.api_version = "apps/v1"
    deploy.kind = "Deployment"
    deploy.metdata = client.V1ObjectMeta(name=metadata_name)


    spec = client.V1DeploymentSpec()
    spec.replicas = replicas 




if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")