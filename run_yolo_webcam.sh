#!/bin/bash

# Define paths
SCRIPT_DIR="$(dirname "$0")"
YOLOV5_DIR="$SCRIPT_DIR/yolov5"
MODEL_PATH="$YOLOV5_DIR/yolov5s.pt"

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Error: Python 3 is required but not installed. Please install Python 3 and try again."
    exit 1
fi

# macOS camera permission warning
if [[ "$OSTYPE" == "darwin"* ]]; then
    echo "======================================================"
    echo "IMPORTANT: macOS Camera Permission Information"
    echo "======================================================"
    echo "If this is your first time running this app, you may need"
    echo "to grant camera access permission in System Preferences."
    echo ""
    echo "If you see a camera access error, please:"
    echo "1. Go to System Preferences -> Security & Privacy -> Camera"
    echo "2. Ensure Terminal (or your Python application) is checked"
    echo "3. Run this script again"
    echo "======================================================"
    echo ""
    read -p "Press Enter to continue..."
fi

# Check if the YOLOv5s model exists, download if needed
if [ ! -f "$MODEL_PATH" ]; then
    echo "Downloading YOLOv5s model..."
    python3 -c "import torch; torch.hub.download_url_to_file('https://github.com/ultralytics/yolov5/releases/download/v6.1/yolov5s.pt', '$MODEL_PATH')"
fi

# Detect whether we're running on Apple Silicon
if [[ "$(uname -m)" == "arm64" ]]; then
    echo "Apple Silicon (M-series) detected. Using optimized settings."
    DEVICE="cpu"  # CPU is often faster on M-series Macs for small models
else
    echo "Intel architecture detected."
    DEVICE="cpu"
fi

echo "Starting YOLOv5 webcam detection..."
echo "Press 'q' to exit the detection window"

# Choose detection method based on user preference
if [ -z "$1" ] || [ "$1" == "detect" ]; then
    # Use built-in detect.py script with webcam input
    echo "Using YOLOv5's built-in detect.py script"
    cd "$YOLOV5_DIR" && python3 detect.py --weights yolov5s.pt --source 0 --conf 0.25 --img-size 640 --device $DEVICE
elif [ "$1" == "custom" ]; then
    # Use our custom detection script
    echo "Using custom webcam_detection.py script"
    cd "$YOLOV5_DIR" && python3 webcam_detection.py
else
    echo "Unknown option: $1"
    echo "Usage: ./run_yolo_webcam.sh [detect|custom]"
    echo "  detect: Use YOLOv5's built-in detect.py script (default)"
    echo "  custom: Use our custom webcam detection script"
    exit 1
fi

echo "YOLOv5 webcam detection stopped." 