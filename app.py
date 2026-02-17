from flask import Flask, render_template, Response, jsonify
import cv2
import cvzone
import math
from ultralytics import YOLO

app = Flask(__name__)

# Load YOLO model
model = YOLO("yolov8s.pt")

# Video source
cap = cv2.VideoCapture("fall.mp4")

if not cap.isOpened():
    print("Error: Could not open video.")
    exit()

fall_detected = False


def generate_frames():
    global fall_detected

    while True:
        success, frame = cap.read()
        if not success:
            break

        frame = cv2.resize(frame, (980, 740))
        results = model(frame)

        fall_detected = False

        for info in results:
            for box in info.boxes:
                x1, y1, x2, y2 = map(int, box.xyxy[0])
                confidence = float(box.conf[0])
                class_id = int(box.cls[0])
                conf = math.ceil(confidence * 100)

                height = y2 - y1
                width = x2 - x1

                # class_id == 0 means person in YOLO
                if conf > 80 and class_id == 0:
                    cvzone.cornerRect(frame, [x1, y1, width, height], l=20, rt=3)

                    if width > height:
                        fall_detected = True
                        cvzone.putTextRect(
                            frame,
                            "FALL DETECTED",
                            [x1, y1 - 40],
                            thickness=2,
                            scale=2
                        )

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/video')
def video():
    return Response(generate_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/status')
def status():
    global fall_detected
    return jsonify({"fall": fall_detected})


if __name__ == "__main__":
    app.run(debug=True)