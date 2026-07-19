import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import tempfile


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
    [
        "Image Detection",
        "Video Detection"
    ]
)


# Image

if option == "Image Detection":

    file = st.file_uploader(
        "Upload Image",
        type=["jpg","jpeg","png"]
    )


    if file:

        image = Image.open(file)

        st.image(
            image,
            caption="Original Image"
        )


        img = np.array(image)


        result = model(img)


        output = result[0].plot()


        st.image(
            output,
            channels="BGR",
            caption="Detection Result"
        )


# Video

else:

    file = st.file_uploader(
        "Upload Video",
        type=["mp4","avi","mov"]
    )


    if file:

        temp = tempfile.NamedTemporaryFile(
            delete=False
        )

        temp.write(
            file.read()
        )


        cap = cv2.VideoCapture(
            temp.name
        )


        display = st.empty()


        while cap.isOpened():

            ret, frame = cap.read()

            if not ret:
                break


            results = model.track(
                frame,
                persist=True
            )


            output = results[0].plot()


            display.image(
                output,
                channels="BGR"
            )


        cap.release()