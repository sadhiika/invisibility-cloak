# Invisibility Cloak

## Overview
This project implements a virtual "invisibility cloak" inspired by Harry Potter using computer vision techniques with OpenCV and Python. By detecting a specific color (bright pink/coral in this implementation), the program replaces that color with the background, creating the illusion that objects covered by the cloth are invisible.

## How It Works
1. The program first captures a static background image when no one is in the frame.
2. It then identifies the designated color (pink/coral) in each video frame.
3. The program replaces the pixels of that color with the corresponding pixels from the background image.
4. This creates the illusion that anything covered by the colored cloth is invisible.

## Requirements
- Python 3.x
- OpenCV (`opencv-python`)
- NumPy

## Installation
```bash
pip install opencv-python numpy
```

## Usage
Run the script:
```bash
python cloak.py
```
1. When prompted, move out of the camera frame and press any key to capture the background.
2. Return to the frame with your colored cloth (bright pink/coral).
3. Objects covered by the cloth will appear "invisible".
4. Press 'q' to quit the application.

## Code Explanation
- `create_background()`: Captures and processes the background image.
- `create_mask()`: Creates a binary mask for the colored cloth.
- `apply_cloak_effect()`: Replaces the cloth with the background.
- `main()`: Orchestrates the entire process.

## Customization
We can modify the HSV color range in the code to use a different colored cloth:
```python
lower_color = np.array([h_min, s_min, v_min])
upper_color = np.array([h_max, s_max, v_max])
