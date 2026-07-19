# Real-Time Object Detection and Tracking System Using YOLOv8

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![YOLOv8](https://img.shields.io/badge/Model-YOLOv8-green)
![OpenCV](https://img.shields.io/badge/Computer%20Vision-OpenCV-red)
![Streamlit](https://img.shields.io/badge/Web%20Application-Streamlit-orange)
![Artificial Intelligence](https://img.shields.io/badge/Domain-AI-purple)

---

## Project Overview

The **Real-Time Object Detection and Tracking System** is an AI-based computer vision application developed using **YOLOv8, OpenCV, and Streamlit**.

The system detects and tracks multiple objects from different input sources such as live webcam, images, and video files. It uses deep learning-based object detection techniques to identify objects, display bounding boxes, confidence scores, and tracking IDs in real time.

This project was developed as part of the **CodeAlpha Artificial Intelligence Internship Program**.

---

## Objectives

- Develop a real-time object detection system using YOLOv8
- Detect multiple objects from live and recorded inputs
- Implement object tracking with unique IDs
- Create an interactive AI-based web application
- Deploy the computer vision model using Streamlit Cloud

---

## Features

- Real-time webcam object detection
- Image-based object detection
- Video-based object detection
- Object tracking with unique IDs
- Bounding box visualization
- Object classification
- Confidence score display
- Interactive Streamlit web interface

---

## Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| Object Detection Model | YOLOv8 |
| Computer Vision | OpenCV |
| AI Framework | Ultralytics |
| Web Framework | Streamlit |
| Image Processing | NumPy, Pillow |

---

## System Workflow

```
Input Source
(Webcam / Image / Video)
          |
          ↓
OpenCV Processing
          |
          ↓
YOLOv8 Deep Learning Model
          |
          ↓
Object Detection & Tracking
          |
          ↓
Streamlit Web Interface
          |
          ↓
Detection Results
```

---

## Project Structure

```
Object_Detection_Tracking_YOLO/

│── streamlit_app.py        # Main Streamlit web application
│── app.py                  # OpenCV based detection application
│── yolov8n.pt              # YOLOv8 pretrained model
│── requirements.txt        # Required Python packages
│── README.md               # Project documentation
│── .gitignore              # Ignored files
```

---

# Installation and Setup

## Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

## Navigate to Project Folder

```bash
cd Object_Detection_Tracking_YOLO
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running the Application

Run the Streamlit application:

```bash
streamlit run streamlit_app.py
```

The application will open in your browser.

---

# Application Modules

## 1. Live Webcam Detection

The application captures live webcam input and performs real-time object detection and tracking using YOLOv8.

Detected objects are displayed with:

- Object names
- Bounding boxes
- Confidence scores
- Tracking IDs

---

## 2. Image Detection

Users can upload images and the AI model detects objects present in the image.

The output contains:

- Detected object labels
- Confidence percentage
- Annotated image output

---

## 3. Video Detection

Users can upload video files and the system processes each frame to detect and track objects.

---

# Model Information

## YOLOv8

YOLOv8 (You Only Look Once Version 8) is a state-of-the-art deep learning model used for fast and accurate real-time object detection.

The pretrained model can detect various common objects including:

- Person
- Vehicles
- Animals
- Electronics
- Everyday objects

---

# Deployment

The application is deployed using **Streamlit Community Cloud**.

## Live Web Application

Website Link:

```
ADD_YOUR_STREAMLIT_APP_LINK_HERE
```

---

# Demo Video

Project demonstration video:

Google Drive Link:

```
ADD_YOUR_GOOGLE_DRIVE_VIDEO_LINK_HERE
```

---

# Future Enhancements

- Custom object detection model training
- CCTV surveillance integration
- Advanced tracking using Deep SORT
- Cloud-based AI inference
- Mobile application deployment

---

# Author

**G. Kaviya**

B.Tech Artificial Intelligence and Data Science

---

# Internship Information

Developed as part of the **CodeAlpha Artificial Intelligence Internship Program**.

This project demonstrates practical implementation of:

- Computer Vision
- Deep Learning
- Object Detection
- AI Model Deployment
- Web Application Development
