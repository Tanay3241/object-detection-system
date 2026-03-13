from ultralytics import YOLO
import cv2

# Load YOLOv8 model
model = YOLO("yolov8n.pt")

# Image path
image_path = "images/sample.jpg"

results = model(image_path)

annotated_frame = results[0].plot()

cv2.imshow("Image Detection", annotated_frame)

cv2.waitKey(0)
cv2.destroyAllWindows()
