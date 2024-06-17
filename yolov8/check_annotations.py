import os
import cv2
def get_label_text(label_folder, image_name):
    label_path = os.path.join(label_folder, image_name + ".txt")
    if os.path.exists(label_path):
        with open(label_path, 'r') as file:
            return file.read().strip()
    else:
        return None

image_folder = "annotated_data\dob_1\images"
label_folder = "annotated_data\dob_1\labels"

window_width = 300
window_height = 150
for image_file in os.listdir(image_folder):
    if image_file.endswith(".jpg"):
        image_name = os.path.splitext(image_file)[0]
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)
        label_text = get_label_text(label_folder, image_name)
        print("label_text: ", label_text, image_name)
        
        resized_image = cv2.resize(image, (window_width, window_height - 50))
        
        cv2.imshow("Image with Text", resized_image)
        key = cv2.waitKey(0)
        if key == "q":
            break
        cv2.destroyAllWindows()