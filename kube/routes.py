from kube.apis.deployment import create_deployment,delete_deployment
from kube.apis.service import create_service,delete_service

@app.route("/deploy/create",methods=["POST"])
def deployment_create():
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

@app.route("/deploy/delete",methods=["POST"])
def deployment_delete():
    data=request.get_json()
    deployment_name=data["name"]

    status = delete_deployment(deployment_name)
    msg="Deleted deployment"
    if status!=200:
        msg="Deployment not present"


    ret = {
        "Status": status,
        "Msg": msg
    }

    return jsonify(ret)



@app.route("/service/create",methods=["POST"])
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


@app.route("/service/delete",methods=["POST"])
def service_delete():
    data=request.get_json()
    svc_name=data["name"]

    status = delete_service(svc_name)
    msg="Service deleted"

    if status!=200:
        msg = "Service not present"
    
    ret = {
        "Status": status,
        "Msg": msg
    }

    return jsonify(ret)

    




if __name__ == "__main__":
    app.run(debug=True,host="0.0.0.0")