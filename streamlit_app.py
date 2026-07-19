import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import tempfile
import cv2


# Page Configuration
st.set_page_config(
    page_title="YOLOv8 Object Detection",
    page_icon="AI",
    layout="wide"
)


st.title("YOLOv8 Object Detection and Tracking System")

st.write(
    "AI-powered Computer Vision application using YOLOv8 and Streamlit"
)


# Load YOLO Model
@st.cache_resource
def load_model():
    return YOLO("yolov8n.pt")


model = load_model()


# Sidebar
st.sidebar.title("Project Features")

st.sidebar.write(
"""
Features:
- Image Detection
- Video Detection
- Object Tracking
- Confidence Score

Technologies:
- Python
- YOLOv8
- OpenCV
- Streamlit
"""
)


option = st.selectbox(
    "Choose Detection Type",
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

        temp = tempfile.NamedTemporaryFile(
            delete=False,
            suffix=".mp4"
        )

        temp.write(
            uploaded_video.read()
        )


        cap = cv2.VideoCapture(
            temp.name
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