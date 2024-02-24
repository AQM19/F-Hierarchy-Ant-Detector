from ultralytics import YOLO

def predict(source, model):
    results = model(source, show=True, stream_buffer=True, save=True)