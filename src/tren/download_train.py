from roboflow import Roboflow
import os
from dotenv import load_dotenv

def download_train():
    roboflow_private_api = os.getenv("ROBOFLOW_PRIVATE_API")
    roboflow_workspace = os.getenv("ROBOFLOW_WORKSPACE")
    roboflow_project = os.getenv("ROBOFLOW_PROJECT")

    if roboflow_private_api is None:
        print("ROBOFLOW_PRIVATE_API no está definida en el archivo .env")
        return

    if roboflow_workspace is None:
        print("ROBOFLOW_WORKSPACE no está definida en el archivo .env")
        return

    if roboflow_project is None:
        print("ROBOFLOW_PROJECT no está definida en el archivo .env")
        return

    rf = Roboflow(api_key=roboflow_private_api)
    project = rf.workspace(roboflow_workspace).project(roboflow_project)
    dataset = project.version(1).download("yolov8")