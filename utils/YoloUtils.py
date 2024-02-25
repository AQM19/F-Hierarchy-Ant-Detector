import os
from ultralytics import YOLO
import cv2

class YoloUtils():
    @staticmethod
    def train_model() -> bool:
        model = YOLO('yolov8n.pt')

        current_directory = os.getcwd()
        yaml_path = os.getenv("PROJECT_YAML")

        if yaml_path is None:
            print("PROJECT_YAML no está definida como variable de entorno.")
            return None

        data = f"{current_directory}{yaml_path}"

        if not os.path.exists(data):
            print("No existe el archivo yaml de entrenamiento.")
            return False

        print("Entrenando modelo...")
        results = model.train(data=data, epochs=100, imgsz=640)
        print(results)
        return True

    @staticmethod
    def load_model() -> YOLO | None:
        pt_path = os.getenv("PT_MODEL")

        if pt_path is None:
            print("PT_MODEL no está definida como variable de entorno.")
            return None

        current_directory = os.getcwd()
        pt = f"{current_directory}{pt_path}"

        if not os.path.exists(pt):
            print("Entra aqui")
            is_trained = YoloUtils.train_model()
            if not is_trained:
                return None

        print("Obteniendo modelo...")
        model = YOLO(model=pt)
        return model
    
    @staticmethod
    def predict(source):
        model = YoloUtils.load_model()

        if model is None:
            print("No se ha podido cargar ningún modelo.")
            return

        print("Prediciendo resultados...")
        results = model(source, show=True, stream_buffer=True, save=True)
        print(results)