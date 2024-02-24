from src.yolo.load_model import load_model
from src.tren.train_model import train_model
from src.yolo.predict import predict

def main():
    model = load_model('D:\Proyects\F-trantcker\AntTracker-1\yolov8n.pt')
    # result = train_model(model, 'D:\Proyects\F-trantcker\AntTracker-1\data.yaml')
    source = r"D:\Proyects\F-trantcker\assets\videos\forrajeo_hormigas_2.mp4"
    predict(source, model)
    
if __name__ == '__main__':
    main()