import os
import sys
import yaml
sys.path.append('./yolov5')  # Ensure the YOLOv5 path is correct
from yolov5 import train

def main():
    # Configuration parameters for training
    args = {
        'img_size': 640,           # Input image size
        'batch_size': 16,          # Batch size for training
        'epochs': 50,              # Number of training epochs
        'data': 'data.yaml',       # Path to the data.yaml file
        'weights': 'yolov5s.pt',   # Path to pre-trained weights
        'hyp': 'hyp.yaml',         # Path to hyperparameters file (if any)
    }
    
    # Print the configuration for verification
    print("Training configuration:")
    for key, value in args.items():
        print(f"{key}: {value}")

    # Load hyperparameters
    with open(args['hyp'], 'r') as f:
        hyp = yaml.safe_load(f)
    print("Loaded hyperparameters:")
    for key, value in hyp.items():
        print(f"{key}: {value}")

    # Run the training
    train.run(**args)

if __name__ == "__main__":
    main()

