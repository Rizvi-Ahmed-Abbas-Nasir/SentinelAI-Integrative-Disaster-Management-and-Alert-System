
from ultralytics import YOLO
import cv2

def main():


    while True:

        model = YOLO("best.pt")



        results = model.predict(source=1, show = True)
        print(results[0])
        for i in results:
            print(i)

        if results == "Box":
            print("Firedetect")
        else:
            print("No")

if __name__ == "__main__":
    main()