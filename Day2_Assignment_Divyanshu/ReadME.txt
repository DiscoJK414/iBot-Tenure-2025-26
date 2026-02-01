This project implements a **robust circle detection system** using the **Hough Circle Transform**.  
It supports **automatic parameter tuning**, an **interactive Tkinter-based GUI**.

Features-
Image preprocessing (grayscale + Gaussian blur)
Circle detection using OpenCV’s Hough Circle Transform
Visualization of detected circles with IDs and radii

### 1. Preprocessing
- Convert image to grayscale
- Apply Gaussian blur to reduce noise

### 2. Automatic Parameter Tuning
- Uses Canny edge detection to estimate edge density
- Adjusts:
  - `param2` (accumulator threshold)
  - `minDist` (minimum distance between circle centers)
  - Radius range based on image size

### 3. Circle Detection
- Uses `cv2.HoughCircles` with tuned parameters
- Returns `(x, y, radius)` for each detected circle

### 4. GUI-Based Fine Tuning
- Tkinter GUI with sliders for:
  - `dp`
  - `minDist`
  - `param1`
  - `param2`
  - `minRadius`
  - `maxRadius`
