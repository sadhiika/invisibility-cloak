import cv2
import time
import numpy as np

def create_background(cap, num_frames = 30):
    print("Press any key when ready to capture background (make sure you're out of the frame)")
    cv2.imshow('Invisibility cloak', cap.read()[1])  # Show current frame
    cv2.waitKey(0)  # Wait indefinitely until a key is pressed
    
    print("Capturing background...")
    background = []
    for i in range(num_frames):
        ret, frame = cap.read()
        if ret:
            background.append(frame)
            cv2.imshow('Invisibility cloak', frame)  # Show frames being captured
            cv2.waitKey(1)  # Update display
        else:
            print(f"could not read frame")
        time.sleep(0.1)
    if background:
        return np.median(background, axis=0).astype(np.uint8)
    else:
        raise ValueError("No frames captured for background.")

    
def create_mask(frame, lower_color, upper_color):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_color, upper_color)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=2)
    mask = cv2.morphologyEx(mask, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8), iterations=1)
    return mask

def apply_cloak_effect(frame, mask, background):
    mask_inv = cv2.bitwise_not(mask)
    fg = cv2.bitwise_and(frame, frame, mask=mask_inv)
    bg = cv2.bitwise_and(background, background, mask=mask)
    return cv2.add(fg, bg)

def main():
    cap = cv2.VideoCapture(0) 
    if not cap.isOpened():
        print("Error: Could not open video.")
        return
    try:
        background = create_background(cap)
    except ValueError as e:
        print(e)
        cap.release()
        return
    
    # Define deep pink color range in HSV
    

    lower_pink = np.array([150, 100, 100])  # Lower bound for bright pink/coral
    upper_pink = np.array([180, 255, 255])  # Upper bound for bright pink/coral

    print("Starting main loop. Press 'q' to quit.")
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame.")
            time.sleep(1)
            continue

        mask = create_mask(frame, lower_pink, upper_pink)
        result = apply_cloak_effect(frame, mask, background)

        cv2.imshow('Invisiblity cloak', result)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()

    
