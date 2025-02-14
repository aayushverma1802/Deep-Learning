from ultralytics import YOLO

model = YOLO('yolov8n.pt') 

# Train the model
model.train(data="C:\\Users\\aayus\\Documents\\Brahmastra\\YOLO SOLO\\Car\\Cairo-Car-v3-5\\data.yaml", epochs=15,batch=16)

