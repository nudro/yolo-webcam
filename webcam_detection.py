import os
import sys
import platform
import subprocess
import cv2

def request_camera_permission_macos():
    """
    Display instructions for enabling camera permissions on macOS
    """
    print("\n*** CAMERA PERMISSION REQUIRED ***")
    print("On macOS, you need to grant camera permission to this application.")
    print("Please follow these steps:")
    print("1. Open System Preferences")
    print("2. Go to Security & Privacy -> Privacy -> Camera")
    print("3. Ensure that Terminal or your Python application is checked")
    print("4. Restart this application after granting permission")
    print("\nAlternatively, you can try running the script from a Python IDE like PyCharm or VS Code\n")
    
    # Ask if user wants to open System Preferences
    choice = input("Would you like to open System Preferences now? (y/n): ")
    if choice.lower() == 'y':
        subprocess.call(['open', 'x-apple.systempreferences:com.apple.preference.security?Privacy_Camera'])
    
    print("Please restart the application after granting permission.")
    sys.exit(1)

def test_camera_access():
    """Test if we can access the camera"""
    print("Testing camera access...")
    
    # Try multiple camera indices
    camera_indices = [0, 1, 2]  # Try camera indices 0, 1, and 2
    
    for idx in camera_indices:
        cap = cv2.VideoCapture(idx)
        if cap.isOpened():
            # Successfully opened camera
            ret, frame = cap.read()
            if ret:
                print(f"Successfully connected to camera at index {idx}")
                print(f"Camera resolution: {frame.shape[1]}x{frame.shape[0]}")
                cap.release()
                return True
            else:
                print(f"Connected to camera at index {idx} but could not read frame")
                cap.release()
        else:
            print(f"Could not connect to camera at index {idx}")
    
    # If we're here, we couldn't access any camera
    print("Error: Could not access any webcam.")
    if platform.system() == 'Darwin':  # macOS
        request_camera_permission_macos()
    else:
        print("Please check that your webcam is properly connected and not in use by another application.")
    return False

def main():
    # First check if we can access the camera
    if not test_camera_access():
        return
    
    print("Starting YOLOv5 webcam detection using built-in detect.py script...")
    
    # Build the command to run detect.py with webcam input
    cmd = [
        "python3", "detect.py",
        "--weights", "yolov5s.pt",
        "--source", "0",           # Use webcam (index 0)
        "--conf", "0.25",          # Confidence threshold
        "--img-size", "640",       # Input image size
        "--device", "cpu"          # Use CPU
    ]
    
    # Execute the command
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running YOLOv5 detection: {e}")
    except KeyboardInterrupt:
        print("Detection interrupted by user.")

if __name__ == "__main__":
    main() 