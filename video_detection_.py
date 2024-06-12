import torch
import cv2
import os

# Path to the trained YOLOv5 model
model_path = 'yolov5/runs/train/exp/weights/best.pt'
#model_path = '/home/data/Videos/park-analyzer/yolov5/#runs/train/exp28/weights/best.pt'

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'custom', path=model_path, force_reload=True)

# Path to the input video file
input_video_path = 'path/to/your/video.mp4'

# Path to the output video file
output_video_path = 'path/to/output/video_output.mp4'

# Initialize video capture
cap = cv2.VideoCapture(input_video_path)

# Get video properties
frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Initialize video writer
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))

frame_count = 0
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Perform inference
    results = model(frame)

    # Render results on the frame
    frame = results.render()[0]

    # Write the frame to the output video
    out.write(frame)

    frame_count += 1
    print(f"Processed frame {frame_count}/{total_frames}")

cap.release()
out.release()
cv2.destroyAllWindows()

print(f"Video analysis complete. Output saved to {output_video_path}")

