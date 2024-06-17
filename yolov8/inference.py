import os
import cv2
from ultralytics import YOLO
model = YOLO(r"models\small_best_openvino_model",task="detect")

def image_loc(foldername):
    fileName = []
    for root, dirs, files in os.walk(os.path.abspath(foldername)):
        for namef in files:
            file_name = os.path.abspath(os.path.join(root, namef))
            fileName.append(file_name)
    return fileName


images=image_loc("Aadhaar_card_dataset_for_training/data/test/images")

for i in images:
    img = cv2.imread(i)

    results = model.predict(img, imgsz = 320, half = True, conf = 0.5, iou = 0.6)
    
    for result in results:
        boxes = result[:5].boxes.numpy() 
        # print("boxes: ", boxes)
        for box in boxes:  
            print("class", box.cls)
            print("xyxy", box.xyxy)
            print("conf", box.conf)

    r = results[0]
    im_array = r.plot() 
    cv2.namedWindow("inference", cv2.WINDOW_NORMAL)  
    cv2.imshow('inference',im_array)
    cv2.waitKey(0)
cv2.destroyAllWindows()












