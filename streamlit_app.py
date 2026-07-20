import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import tempfile
import os

st.set_page_config(
    page_title="YOLOv8 Object Detection",
    layout="wide"
)

st.title("YOLOv8 Object Detection and Tracking")


@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")


model = load_model()

option = st.selectbox(
    "Choose Mode",
    ["Image Detection", "Video Detection"]
)

# ---------------- Image Detection ----------------
if option == "Image Detection":

    file = st.file_uploader(
        "Upload Image",
        type=["jpg", "jpeg", "png"]
    )

    if file:
        image = Image.open(file).convert("RGB")

        st.image(image, caption="Original Image")

        img = np.array(image)

        with st.spinner("Running detection..."):
            result = model(img)

        output = result[0].plot()

        st.image(
            output,
            channels="BGR",
            caption="Detection Result"
        )

# ---------------- Video Detection ----------------
else:

    file = st.file_uploader(
        "Upload Video",
        type=["mp4", "avi", "mov"]
    )

    if file:
        temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
        temp.write(file.read())
        temp.close()

        cap = cv2.VideoCapture(temp.name)

        if not cap.isOpened():
            st.error("Could not open video file.")
        else:
            display = st.empty()
            stop_button = st.button("Stop")

            while cap.isOpened():
                ret, frame = cap.read()

                if not ret or stop_button:
                    break

                results = model.track(frame, persist=True)
                output = results[0].plot()

                display.image(output, channels="BGR")

            cap.release()

        # clean up temp file after processing
        os.unlink(temp.name)