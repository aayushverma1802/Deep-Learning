import cv2
from ultralytics import YOLO

# Load the trained model
model = YOLO(r'C:\\Users\\aayus\\Documents\\Brahmastra\\YOLO SOLO\\Car\\runs\\detect\\train2\\weights\\best.pt')

# Test the model on the video and save the results
results = model.predict(source=r'C:\\Users\\aayus\\Documents\\Brahmastra\\YOLO SOLO\\Car\\testt.mp4', show=True, save=True)

