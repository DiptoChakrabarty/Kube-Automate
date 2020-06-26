from kube.apis.deployment import create_deployment
from kube.apis.service import create_service

@app.route("/deploy",methods=["POST"])
def deployment():
    data = request.get_json()
    metadata_name = data["metadata_name"]
    replicas = data["replicas"]
    container_name = data["container_name"]
    container_image =  data["container_image"]
    container_port = data["container_port"]
    labels = data["labels"]

    status = create_deployment(metadata_name,labels,container_name,container_image,container_port,replicas)

    ret = {
        "Status": status,
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

    status = create_service(metadata_name,port,target_port,selectors)

    ret = {
        "Status": 200,
        "Msg": "Service up  Successfully"
    }

    return jsonify(ret)

@app.route("/ingress",methods=["POST"])
def ingress():
    data= request.get_json()
    




if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")