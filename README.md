# YOLOv8 Object Detection and Tracking System

## AI-Based Computer Vision Application using YOLOv8, OpenCV and Streamlit

---

## Project Overview

The **YOLOv8 Object Detection and Tracking System** is an Artificial Intelligence and Computer Vision project that detects and tracks objects from images and videos using the advanced **YOLOv8 deep learning model**.

The application uses a pre-trained YOLOv8 model to identify objects, generate bounding boxes, display object labels, and provide confidence scores through an interactive **Streamlit web application**.

This project demonstrates the implementation of real-time object detection techniques using Deep Learning, Image Processing, and AI model deployment.

---

# Project Workflow

![Project Workflow]("D:\internship\object_detection_tracking_YOLO\assest\project_workflow.jpeg")

---

# Features

## 1. Image Object Detection

- Upload images through the web interface
- Detect multiple objects automatically
- Generate accurate bounding boxes
- Display object names and confidence scores
- Visualize AI prediction results instantly


## 2. Video Object Detection and Tracking

- Upload video files
- Process video frames using YOLOv8
- Detect objects continuously
- Track objects across multiple frames
- Generate real-time detection visualization


## 3. AI-Powered Object Recognition

- Deep learning based object detection
- Multi-class object recognition
- High-speed inference using YOLOv8 Nano model
- Accurate object localization


## 4. Interactive Web Application

- User-friendly Streamlit interface
- Simple upload-based workflow
- Fast AI predictions
- Easy access without complex setup


---

# Technology Stack

| Category | Technology |
|----------|------------|
| Programming Language | Python |
| AI Framework | Ultralytics YOLOv8 |
| Deep Learning Model | YOLOv8 Nano |
| Computer Vision | OpenCV |
| Web Framework | Streamlit |
| Image Processing | Pillow |
| Numerical Computing | NumPy |

---

# Project Structure

```
CodeAlpha_Object_Detection_Tracking_YOLO

│
├── streamlit_app.py
│      Main Streamlit application
│
├── yolov8n.pt
│      Pre-trained YOLOv8 model
│
├── requirements.txt
│      Required Python dependencies
│
├── README.md
│      Project documentation
│
└── .gitignore
       Ignored files
```

---

# Installation and Setup

## Clone Repository

```bash
git clone https://github.com/kaviya050102/CodeAlpha_Object_Detection_Tracking_YOLO.git
```

## Navigate to Project Directory

```bash
cd CodeAlpha_Object_Detection_Tracking_YOLO
```

## Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# Run Application

Start the Streamlit application:

```bash
streamlit run streamlit_app.py
```

Application will open:

```
http://localhost:8501
```

---

# How The System Works

### Step 1: Input Collection

The user uploads an image or video through the Streamlit interface.

### Step 2: Image Processing

The input data is converted into a format suitable for AI processing.

### Step 3: YOLOv8 Detection

The YOLOv8 model analyzes the input and identifies objects.

### Step 4: Object Tracking

Detected objects are tracked across video frames.

### Step 5: Result Visualization

The application displays:

- Object boundaries
- Class labels
- Detection results

---

# YOLOv8 Model Information

YOLOv8 (You Only Look Once Version 8) is a state-of-the-art object detection algorithm developed for fast and accurate computer vision applications.

This project uses:

```
Model: YOLOv8 Nano
Dataset: COCO Dataset
Task: Object Detection and Tracking
```

Advantages:

- Real-time detection
- High accuracy
- Lightweight architecture
- Fast inference speed

---

# Detected Object Examples

The model can recognize objects including:

- Person
- Vehicle
- Bicycle
- Animal
- Electronics
- Furniture
- Daily life objects

and many more classes from the COCO dataset.

---

# Application Areas

## Smart Surveillance

Detect and monitor objects in security systems.

## Traffic Monitoring

Identify vehicles and analyze road conditions.

## Industrial Automation

Support automated inspection systems.

## Retail Analytics

Monitor customer activity and product interaction.

## Autonomous Systems

Assist AI-based decision-making systems.

---

# Deployment

The application can be deployed using:

## Streamlit Cloud

Live Application:

```
ADD_YOUR_STREAMLIT_LINK
```

---

# Demo

Project Demonstration Video:

```
ADD_YOUR_GOOGLE_DRIVE_VIDEO_LINK
```

The demo includes:

- Image detection
- Video detection
- AI prediction results

---

# Future Enhancements

Future improvements planned:

- Real-time webcam detection
- Advanced tracking using DeepSORT
- Custom dataset training
- Object counting system
- Real-time analytics dashboard
- Mobile application integration

---

# Learning Outcomes

Through this project, the following concepts were implemented:

- Artificial Intelligence
- Computer Vision
- Deep Learning
- YOLO Object Detection
- Object Tracking
- OpenCV Image Processing
- Streamlit Application Development
- AI Model Deployment

---

# Author

## Kaviya G

B.Tech Artificial Intelligence and Data Science

---

# Internship Project

Developed as part of:

**CodeAlpha Artificial Intelligence Internship**

Project Title:

**Object Detection and Tracking using YOLOv8**

---