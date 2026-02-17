import cv2
import cvzone
import math
from ultralytics import YOLO

cap = cv2.VideoCapture('fall.mp4')

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

model = YOLO('yolov8s.pt')

with open('classes.txt', 'r') as f:
    classnames = f.read().splitlines()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Video ended or failed.")
        break

    frame = cv2.resize(frame, (980, 740))

    results = model(frame)

    for info in results:
        for box in info.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            confidence = float(box.conf[0])
            class_detect = int(box.cls[0])
            class_name = classnames[class_detect]
            conf = math.ceil(confidence * 100)

            height = y2 - y1
            width = x2 - x1
            threshold = height - width

            if conf > 80 and class_name == 'person':
                cvzone.cornerRect(frame, [x1, y1, width, height], l=30, rt=6)
                cvzone.putTextRect(frame, f'{class_name}', 
                                   [x1 + 8, y1 - 12], thickness=2, scale=2)

                if threshold < 0:
                    cvzone.putTextRect(frame, 'Fall Detected',
                                       [x1, y1 - 40], thickness=2, scale=2)

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('t'):
        break

cap.release()
cv2.destroyAllWindows()