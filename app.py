import cv2
import numpy as np
from tqdm import tqdm

cap = cv2.VideoCapture("Kiriko48.mp4")

height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))

fps = cap.get(cv2.CAP_PROP_FPS)
print(f"initial fps: {fps}")

total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
print(f"total frames: {total_frames}")

out_fps = 2 * fps

fourcc = cv2.VideoWriter_fourcc(*"mp4v")
out = cv2.VideoWriter("output.mp4", fourcc, out_fps, (width,height))

ret, prev_frame = cap.read()

if cap.isOpened():
    for i in tqdm(range(total_frames)):
        ret, curr_frame = cap.read()
        if not ret:
            break
        
        out.write(prev_frame)
        intermediate_frame = cv2.addWeighted(prev_frame, 0.5, curr_frame, 0.5, 0)
        out.write(intermediate_frame)
        
        prev_frame = curr_frame

print(f"new fps: {out_fps}")

cap.release()
out.release()
