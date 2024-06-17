import cv2
import os
import subprocess

def image_loc(foldername):
    file_names = []
    for root, dirs, files in os.walk(os.path.abspath(foldername)):
        for namef in files:
            file_name = os.path.abspath(os.path.join(root, namef))
            file_names.append(file_name)
    return file_names

folder_path = "annotated_data\dob_1\images"
file_names = image_loc(folder_path)

for file_name in file_names:
    print(file_name)
    img = cv2.imread(file_name)
    
    file_name_without_extension = os.path.splitext(os.path.basename(file_name))[0]
    
    save_folder = "annotated_data\dob_1\labels"
    
    label_folder = os.path.join(save_folder)
    os.makedirs(label_folder, exist_ok=True)
    
    save_file = os.path.join(label_folder, file_name_without_extension + ".txt")
                        
    annotation_text = ""
    with open(save_file, 'w') as txt_file: 
        txt_file.write(annotation_text)
    subprocess.Popen(["notepad", save_file], shell = True, stdin = subprocess.PIPE, stdout= subprocess.PIPE, stderr = subprocess.PIPE, close_fds = True) 
    
    cv2.imshow("Annotations", img)
    key = cv2.waitKey(0)
    if key == "q":
        break
    
    ## from terminal
    # annotation_text = input("Write Text: ")
    # try: 
    #     with open(save_file, 'w') as txt_file: 
    #         txt_file.write(annotation_text)
    #         print(save_file) 
    # except Exception as e: 
    #     print("There is a Problem", str(e)) 
    
cv2.destroyAllWindows()