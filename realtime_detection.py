import torch
import cv2
import numpy as np

# Load  trained model called best.pt ( this can be in exp1 or expt2 or exp20 ... when the train.py ends you will see output with corret exp)
model = torch.hub.load('ultralytics/yolov5', 'custom', path='yolov5/runs/train/exp29/weights/best.pt')

# Initialize video capture (0 for webcam, or provide video file path)
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Inference
    results = model(frame)
    
    # Render results
    frame = np.squeeze(results.render())
    
    # Display
    cv2.imshow('Real-time Costume Detection', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

