import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import tempfile


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="YOLOv8 Object Detection & Tracking",
    layout="wide"
)


st.title("YOLOv8 Object Detection and Tracking System")

st.write(
    "AI-based Computer Vision application using YOLOv8, OpenCV and Streamlit"
)


# ---------------- SIDEBAR ----------------

st.sidebar.title("Project Information")

st.sidebar.write(
"""
Features:

- Image Detection
- Video Detection
- Object Tracking
- Confidence Score Display

Technologies:

Python
YOLOv8
OpenCV
Streamlit
"""
)


# ---------------- LOAD MODEL ----------------

@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")


model = load_model()


# ---------------- MENU ----------------

option = st.selectbox(
    "Select Detection Mode",
    [
        "Image Detection",
        "Video Detection"
    ]
)


# ---------------- IMAGE DETECTION ----------------

if option == "Image Detection":

    uploaded_image = st.file_uploader(
        "Upload Image",
        type=["jpg", "jpeg", "png"]
    )


    if uploaded_image:

        image = Image.open(uploaded_image)

        st.subheader("Original Image")

        st.image(
            image,
            use_container_width=True
        )


        img_array = np.array(image)


        results = model(img_array)


        output = results[0].plot()


        st.subheader("Detection Result")

        st.image(
            output,
            channels="BGR",
            use_container_width=True
        )


# ---------------- VIDEO DETECTION ----------------

else:

    uploaded_video = st.file_uploader(
        "Upload Video",
        type=["mp4", "avi", "mov"]
    )


    if uploaded_video:

        temp_file = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        )


        temp_file.write(
            uploaded_video.read()
        )


        cap = cv2.VideoCapture(
            temp_file.name
        )


        stframe = st.empty()


        while True:

            ret, frame = cap.read()

            if not ret:
                break


            results = model.track(
                frame,
                persist=True
            )


            output = results[0].plot()


            stframe.image(
                output,
                channels="BGR"
            )


        cap.release()