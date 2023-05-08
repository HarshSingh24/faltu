import cv2
import os

# Open the video capture
cap = cv2.VideoCapture(0)  # Change the parameter to the video file path if you want to process a video file

# Create a directory to store the captured frames
output_directory = './captured_frames'
if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Frame counter
frame_count = 0

while True:
    # Read a frame from the video capture
    ret, frame = cap.read()

    # Display the frame
    cv2.imshow("Frame", frame)

    # Store the frame in the output directory
    output_path = os.path.join(output_directory, f"frame{frame_count}.jpg")
    cv2.imwrite(output_path, frame)

    # Increment the frame counter
    frame_count += 1

    # Check for 'q' key press to stop the program
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close all windows
cap.release()
cv2.destroyAllWindows()