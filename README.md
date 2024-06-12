# ObjectAnalyzer

ObjectAnalyzer is a tool to help you train and use a YOLOv5 model to detect and analyze specific objects in images. It includes scripts for preparing data, training the model, and real-time detection using a webcam or video file. The goal is to create a flexible and efficient system for object detection using machine learning, which you can train to identify anything you want.
## Features

- **Data Preparation**: Split images into training and validation sets, and automate initial annotations using a pre-trained YOLOv5 model.
- **Model Training**: Train a YOLOv5 model with custom datasets.
- **Real-Time Detection**: Perform real-time object detection using a webcam or video file.

## Setup

### 1. Install Dependencies

1.1. Install required Python packages:

```bash
pip install torch torchvision torchaudio
pip install opencv-python opencv-python-headless
pip install pandas seaborn
pip install pyyaml
1.2. Clone YOLOv5 Repository

Clone the YOLOv5 repository and install its dependencies:

bash
Copy code
git clone https://github.com/ultralytics/yolov5
cd yolov5
pip install -r requirements.txt
cd ..
2. Install LabelImg
Install LabelImg for manual annotation refinement:

bash
Copy code
pip install labelImg
To run LabelImg:

bash
Copy code
labelImg
3. Prepare Your Dataset

The more images you add from difference places and angels adn lights the more acurate it will be. 
Place your images in dataset/images/all.
Run the script to split the dataset into training and validation sets and generate initial annotations.
4. Split Dataset and Generate Initial Annotations
bash
Copy code
python split_dataset.py ( you can also do this manualy using only labelImg, you need to plae about 70-80% in train foldr and 20% in the val for validation)
python semi_annotation.py ( used for automatic annotaion , but is not still finish don 't use it)
5. Refine Annotations
Use LabelImg to manually refine the annotations generated.
6. Model Training
Train the model:

bash
Copy code
python train.py --img 640 --batch 16 --epochs 50 --data data.yaml --weights yolov5s.pt
7. Real-Time Detection
Run real-time detection:

bash
Copy code
python realtime_detection.py
Usage
Dataset: Prepare and annotate your dataset.
Training: Train the model using the prepared dataset.
Detection: Use the trained model for real-time detection.
Example Commands
bash
Copy code
# Split dataset and generate annotations
python split_dataset.py
python semi_annotation.py

# Train the model
python train.py

# Run real-time detection
python realtime_detection.py
