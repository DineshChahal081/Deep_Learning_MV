import random
import os
import shutil
random.seed(42)

dataset_folder = "numeric_data"
train_ratio = 0.73
validation_ratio = 0.24
test_ratio = 0.03
labels_folder = os.path.join(dataset_folder, 'labels')
images_folder = os.path.join(dataset_folder, 'images')
train_labels_folder = os.path.join(dataset_folder, 'train', 'labels')
train_images_folder = os.path.join(dataset_folder, 'train', 'images')
validation_labels_folder = os.path.join(dataset_folder, 'validation', 'labels')
validation_images_folder = os.path.join(dataset_folder, 'validation', 'images')
test_labels_folder = os.path.join(dataset_folder, 'test', 'labels')
test_images_folder = os.path.join(dataset_folder, 'test', 'images')
os.makedirs(train_labels_folder, exist_ok=True)
os.makedirs(train_images_folder, exist_ok=True)
os.makedirs(validation_labels_folder, exist_ok=True)
os.makedirs(validation_images_folder, exist_ok=True)
os.makedirs(test_labels_folder, exist_ok=True)
os.makedirs(test_images_folder, exist_ok=True)
label_files = os.listdir(labels_folder)
random.shuffle(label_files)
num_samples = len(label_files)
num_train = int(train_ratio * num_samples)
num_validation = int(validation_ratio * num_samples)
train_files = label_files[:num_train]
validation_files = label_files[num_train:num_train + num_validation]
test_files = label_files[num_train + num_validation:]
def move_files(files, source_folder, dest_labels_folder, dest_images_folder):
    for filename in files:
        image_filename = filename.replace('.txt', '.jpg')  # Assuming image files have the same name as label files with different extensions
        source_label_path = os.path.join(labels_folder, filename)
        source_image_path = os.path.join(images_folder, image_filename)
        dest_label_path = os.path.join(dest_labels_folder, filename)
        dest_image_path = os.path.join(dest_images_folder, image_filename)
        shutil.copyfile(source_label_path, dest_label_path)
        shutil.copyfile(source_image_path, dest_image_path)
move_files(train_files, labels_folder, train_labels_folder, train_images_folder)
move_files(validation_files, labels_folder, validation_labels_folder, validation_images_folder)
move_files(test_files, labels_folder, test_labels_folder, test_images_folder)
print("Dataset split into train, validation, and test sets.")