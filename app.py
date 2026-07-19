from flask import Flask, render_template, request, Response
from ultralytics import YOLO
from werkzeug.utils import secure_filename
import cv2
import os


app = Flask(__name__)


UPLOAD_FOLDER = "static/uploads"
RESULT_FOLDER = "static/results"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)


model = YOLO("yolov8n.pt")


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")



# ---------------- IMAGE DETECTION ----------------

@app.route("/image", methods=["POST"])
def image_detection():

    file = request.files["file"]

    filename = secure_filename(file.filename)

    path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(path)


    results = model(path)

    output = results[0].plot()


    result_path = os.path.join(
        RESULT_FOLDER,
        filename
    )

    cv2.imwrite(
        result_path,
        output
    )


    return render_template(
        "index.html",
        result=result_path
    )



# ---------------- VIDEO DETECTION ----------------

@app.route("/video", methods=["POST"])
def video_detection():

    file = request.files["file"]

    filename = secure_filename(file.filename)

    input_path = os.path.join(
        UPLOAD_FOLDER,
        filename
    )

    file.save(input_path)



    cap = cv2.VideoCapture(input_path)


    width = int(
        cap.get(cv2.CAP_PROP_FRAME_WIDTH)
    )

    height = int(
        cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
    )

    fps = int(
        cap.get(cv2.CAP_PROP_FPS)
    )


    output_name = "output.mp4"


    output_path = os.path.join(
        RESULT_FOLDER,
        output_name
    )


    writer = cv2.VideoWriter(
        output_path,
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (width,height)
    )


    while True:

        ret, frame = cap.read()

        if not ret:
            break


        results = model.track(
            frame,
            persist=True
        )


        result_frame = results[0].plot()


        writer.write(
            result_frame
        )


    cap.release()
    writer.release()


    return render_template(
        "index.html",
        video=output_path
    )



# ---------------- WEBCAM ----------------

camera = cv2.VideoCapture(0)


def generate_frames():

    while True:

        success, frame = camera.read()

        if not success:
            break


        results = model.track(
            frame,
            persist=True
        )


        frame = results[0].plot()


        ret, buffer = cv2.imencode(
            ".jpg",
            frame
        )


        frame = buffer.tobytes()


        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"
            + frame +
            b"\r\n"
        )



@app.route("/webcam")
def webcam():

    return render_template(
        "webcam.html"
    )



@app.route("/video_feed")
def video_feed():

    return Response(
        generate_frames(),
        mimetype=
        "multipart/x-mixed-replace; boundary=frame"
    )



if __name__=="__main__":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )