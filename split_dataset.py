import os
import shutil
import random

def split_dataset(image_dir, label_dir, train_ratio=0.8):
    if not os.path.exists(image_dir):
        print(f"Image directory {image_dir} does not exist.")
        return

    if not os.path.exists(label_dir):
        print(f"Label directory {label_dir} does not exist.")
        return

    images = [f for f in os.listdir(image_dir) if f.lower().endswith('.jpg')]
    if not images:
        print(f"No images found in {image_dir}")
        return

    class_images = {}
    for image in images:
        class_name = image.split('_')[0]
        if class_name not in class_images:
            class_images[class_name] = []
        class_images[class_name].append(image)

    train_images, val_images = [], []
    for class_name, imgs in class_images.items():
        random.shuffle(imgs)
        train_size = int(len(imgs) * train_ratio)
        train_images.extend(imgs[:train_size])
        val_images.extend(imgs[train_size:])
    
    os.makedirs('/home/data/Videos/park-analyzer/dataset/images/train', exist_ok=True)
    os.makedirs('/home/data/Videos/park-analyzer/dataset/images/val', exist_ok=True)
    os.makedirs('/home/data/Videos/park-analyzer/dataset/labels/train', exist_ok=True)
    os.makedirs('/home/data/Videos/park-analyzer/dataset/labels/val', exist_ok=True)
    
    for image in train_images:
        shutil.copy(os.path.join(image_dir, image), os.path.join('/home/data/Videos/park-analyzer/dataset/images/train', image))
        label = image.replace('.jpg', '.txt').replace('.JPG', '.txt')
        label_src_path = os.path.join(label_dir, label)
        label_dst_path = os.path.join('/home/data/Videos/park-analyzer/dataset/labels/train', label)
        if os.path.exists(label_src_path):
            shutil.copy(label_src_path, label_dst_path)
        else:
            print(f"Warning: Label file {label_src_path} does not exist.")
    
    for image in val_images:
        shutil.copy(os.path.join(image_dir, image), os.path.join('/home/data/Videos/park-analyzer/dataset/images/val', image))
        label = image.replace('.jpg', '.txt').replace('.JPG', '.txt')
        label_src_path = os.path.join(label_dir, label)
        label_dst_path = os.path.join('/home/data/Videos/park-analyzer/dataset/labels/val', label)
        if os.path.exists(label_src_path):
            shutil.copy(label_src_path, label_dst_path)
        else:
            print(f"Warning: Label file {label_src_path} does not exist.")
    
    print(f"Dataset split completed: {len(train_images)} images in train, {len(val_images)} images in val.")

image_dir = '/home/data/Videos/park-analyzer/dataset/images/all'
label_dir = '/home/data/Videos/park-analyzer/dataset/labels/all'
split_dataset(image_dir, label_dir)

