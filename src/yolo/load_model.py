from ultralytics import YOLO

def load_model(pt):
    model = YOLO(pt)
    return model