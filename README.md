# YOLO Webcam Object Detection

Real-time object detection through webcam using YOLOv5 (You Only Look Once). This implementation is optimized to run on MacBook Air M3 using CPU-only inference, while still achieving real-time performance.

![YOLO Webcam Detection](screenshot.jpg)

## Features

- Real-time object detection using your webcam
- CPU-optimized for Apple Silicon (M3 chip)
- Detection of 80 different object classes with confidence scores
- Automatic webcam access management with macOS permission handling
- Average inference time of ~40-50ms on MacBook Air M3 (20+ FPS)

## Technical Implementation

This project uses YOLOv5, a state-of-the-art real-time object detection system. Key implementation details:

- **Model**: YOLOv5s (small variant) with 7.2M parameters
- **Inference**: CPU-only inference optimized for Apple Silicon
- **Resolution**: Input frames are processed at 640x640 resolution
- **Performance**: ~40-50ms inference time (~20-25 FPS) on MacBook Air M3
- **Framework**: PyTorch backend with OpenCV for camera handling
- **Camera Access**: Multi-index camera detection with macOS permission handling
- **Detection Threshold**: 0.25 confidence threshold for object detection

## Requirements

- Python 3.6+
- macOS (tested on macOS Sonoma with M3 chip)
- External webcam or built-in camera
- Required Python packages:
  - torch
  - torchvision
  - opencv-python
  - numpy
  - Pillow

## Installation

1. Clone this repository:
```bash
git clone https://github.com/nudro/yolo-webcam.git
cd yolo-webcam
```

2. Run the installation script which will automatically install all dependencies:
```bash
./run_yolo_webcam.sh
```

## Usage

Run the script with:

```bash
./run_yolo_webcam.sh
```

This will:
1. Check if Python 3 is installed
2. Guide you through camera permission setup (if needed)
3. Download the YOLOv5s model if needed
4. Start the webcam detection

While the detection window is open:
- Press 'q' to quit the application

## Camera Permission on macOS

On first run, you may need to grant camera access permission:

1. Open System Preferences → Security & Privacy → Privacy → Camera
2. Ensure Terminal (or your Python application) is checked in the list
3. You may need to click the lock icon in the bottom left to make changes
4. Restart the application after granting permission

## Technical Details

### Detection Pipeline

1. **Camera Initialization**: The system attempts to connect to available cameras (index 0-2)
2. **Frame Processing**: Captured frames are resized to 640x640 and normalized
3. **Inference**: The YOLOv5s model processes frames with PyTorch on CPU
4. **Non-Maximum Suppression**: Overlapping detections are filtered
5. **Visualization**: Detected objects are annotated with bounding boxes and labels

### Performance Optimization

The implementation includes several optimizations for MacBook Air M3:
- Efficient tensor operations optimized for Apple Silicon
- Minimal preprocessing to reduce CPU overhead
- Direct use of YOLOv5's detect.py script which is highly optimized

## Customization

You can modify the detection parameters by editing the arguments in `webcam_detection.py`:

- Change `--conf` value to adjust detection threshold
- Change `--img-size` to adjust processing resolution
- Filter specific classes by adding the `--classes` parameter

## Credits

This project uses [YOLOv5](https://github.com/ultralytics/yolov5) by Ultralytics. 