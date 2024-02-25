from utils.Utils import Utils
from utils.YoloUtils import YoloUtils

def main():
    print("Seleccionando archivo...")
    video_source = Utils.select_file()

    if not video_source:
        print("No se seleccionó ningún archivo.")
        return
    
    YoloUtils.predict(source=video_source)
    
if __name__ == '__main__':
    main()