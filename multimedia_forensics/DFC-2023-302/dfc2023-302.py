import cv2  # type: ignore
import numpy as np  # type: ignore
import os

def save_frame_on_subtitle_change(video_path, subtitle_area, output_folder):
    cap = cv2.VideoCapture(video_path)
    prev_frame = None
    frame_count = 0
    saved_frame_count = 0

    os.makedirs(output_folder, exist_ok=True)

    while cap.isOpened():
        ret, frame  = cap.read()
        if not ret:
            break

        subtitle_frame = frame[subtitle_area[1]:subtitle_area[3], subtitle_area[0]:subtitle_area[2]]
        subtitle_gray = cv2.cvtColor(subtitle_frame, cv2.COLOR_BGR2GRAY)

        if prev_frame is None:
            prev_frame = subtitle_gray
            continue

        difference = cv2.absdiff(prev_frame, subtitle_gray)
        mean_diff = np.mean(difference)

        if mean_diff > 5: 
            frame_filename = os.path.join(output_folder, f'frame_{frame_count:04d}.jpg')
            cv2.imwrite(frame_filename, frame)
            print(f'Saved {frame_filename}')
            saved_frame_count += 1

        prev_frame = subtitle_gray
        frame_count += 1

    cap.release()
    cv2.destroyAllWindows()
    print(f'Total frames saved: {saved_frame_count}')

video_path = 'c3.mp4'
subtitle_area = (262, 437, 686, 509)  
output_folder = 'jpg2' 

save_frame_on_subtitle_change(video_path, subtitle_area, output_folder)