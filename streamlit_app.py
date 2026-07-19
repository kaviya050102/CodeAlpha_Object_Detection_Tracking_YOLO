import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import tempfile
from streamlit_webrtc import webrtc_streamer, VideoProcessorBase
import av


# ---------------- PAGE CONFIG ----------------

st.set_page_config(
    page_title="YOLOv8 Object Detection & Tracking",
    page_icon="🤖",
    layout="wide"
)


st.title("🤖 YOLOv8 Real-Time Object Detection & Tracking")

st.write(
    "Computer Vision project using YOLOv8, OpenCV and Streamlit"
)


# ---------------- SIDEBAR ----------------

st.sidebar.title("Project Features")

st.sidebar.write(
"""
✅ Live Webcam Detection

✅ Image Detection

✅ Video Detection

✅ Object Tracking

✅ Confidence Score

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

    model = YOLO("yolov8n.pt")

    return model


model = load_model()



# =====================================================
# WEBCAM DETECTION
# =====================================================

class YOLOProcessor(VideoProcessorBase):

    def recv(self, frame):

        img = frame.to_ndarray(
            format="bgr24"
        )


        results = model.track(
            img,
            persist=True
        )


        output = results[0].plot()


        return av.VideoFrame.from_ndarray(
            output,
            format="bgr24"
        )



# =====================================================
# MENU
# =====================================================

option = st.selectbox(
    "Choose Detection Mode",
    [
        "Live Webcam",
        "Image Upload",
        "Video Upload"
    ]
)



# =====================================================
# LIVE WEBCAM
# =====================================================

if option == "Live Webcam":

    st.subheader("📷 Live Camera Detection")


    webrtc_streamer(
        key="yolo-webcam",
        video_processor_factory=YOLOProcessor,
        media_stream_constraints={
            "video": True,
            "audio": False
        }
    )



# =====================================================
# IMAGE DETECTION
# =====================================================

elif option == "Image Upload":


    uploaded_image = st.file_uploader(
        "Upload Image",
        type=[
            "jpg",
            "jpeg",
            "png"
        ]
    )


    if uploaded_image:


        image = Image.open(
            uploaded_image
        )


        st.subheader(
            "Original Image"
        )


        st.image(
            image,
            use_container_width=True
        )


        img_array = np.array(
            image
        )


        results = model(
            img_array
        )


        output = results[0].plot()


        st.subheader(
            "Detection Result"
        )


        st.image(
            output,
            channels="BGR",
            use_container_width=True
        )



# =====================================================
# VIDEO DETECTION
# =====================================================

else:


    uploaded_video = st.file_uploader(
        "Upload Video",
        type=[
            "mp4",
            "avi",
            "mov"
        ]
    )


    if uploaded_video:


        temp_file = tempfile.NamedTemporaryFile(
            delete=False
        )


        temp_file.write(
            uploaded_video.read()
        )


        cap = cv2.VideoCapture(
            temp_file.name
        )


        stframe = st.empty()


        while cap.isOpened():


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
                channels="BGR",
                use_container_width=True
            )


        cap.release()