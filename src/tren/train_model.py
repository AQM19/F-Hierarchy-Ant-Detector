def train_model(model, data):
    results = model.train(data=data, epochs=100, imgsz=640)
    
    return results