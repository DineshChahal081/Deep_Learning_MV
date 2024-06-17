import os
import cv2
from ultralytics import YOLO
model = YOLO(r"models\small_best_openvino_model", task="detect")

def image_loc(foldername):
    file_paths = []
    for root, dirs, files in os.walk(os.path.abspath(foldername)):
        for namef in files:
            file_name = os.path.abspath(os.path.join(root, namef))
            file_paths.append(file_name)
    return file_paths

def save_bounding_boxes(images_folder, save_folder):
    images = image_loc(images_folder)
    
    os.makedirs(save_folder, exist_ok=True)
    
    for img_path in images:
        img = cv2.imread(img_path)
        results = model.predict(img, imgsz=320,half=True, conf=0.5, iou=0.6)

        for result in results:
            boxes = result[:5].boxes.numpy()
            for idx, box in enumerate(boxes):
                if box is not None:
                    class_index= int(box.cls)
                    print("class_index: ", class_index)
                    xyxy = box.xyxy
                    print("xyxy: ", xyxy)
                    
                    if len(xyxy) == 1 and len(xyxy[0]) == 4:
                        xyxy = xyxy[0]
                        xmin, ymin, xmax, ymax = map(int, xyxy)
                        roi = img[ymin:ymax, xmin:xmax]
                        
                        class_folder = os.path.join(save_folder, str(class_index))
                        os.makedirs(class_folder, exist_ok=True)
                        save_path = os.path.join(class_folder, f"{os.path.splitext(os.path.basename(img_path))[0]}_{class_index}.jpg")
                        cv2.imwrite(save_path, roi)
                        print(f"Saved: {save_path}")
                    else:
                        print("Invalid format:", xyxy)
                else:
                    print("Invalid class:", class_index)
                    
images_folder = "total_image_data"
save_folder = "bounding_box_areas"
save_bounding_boxes(images_folder, save_folder)
