info = """
________________________________________________________________________________________________________________________________________
----------------------------------------------------------------------------------------------------------------------------------------
|   Author: Rounak Paul    
|   Scope: Personal Project
|   Dated: 11-12-2022
|   contact: rounakpaul@hotmail.com
|
|   This script performs linear frame interpolation on a MP4 video. 
|   The number of frames in the output video is 2x than that of the input video.
|
|    ⠀⠀⠀⠀⠀⠀⠀⠀⡰⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀
|    ⠀⠀⠀⠀⠀⠀⠀⠀⡇⡘⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠚⢼⢆⠀⠀⠀
|    ⠀⠀⠀⠀⠀⠀⠀⢠⡧⠑⠂⠓⠄⣀⣀⣀⠀⠀⠀⢀⣤⠞⡠⢠⣸⢸⠀⠀⠀
|    ⠀⠀⠀⠀⠀⠀⣠⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣵⡏⠔⣿⣿⠟⣼⠀⠀⠀
|    ⠀⠀⠀⢀⡠⠊⠔⠀⠀⠀⡠⠃⠀⠀⠀⠀⠀⠀⠀⠀⠋⠼⡿⠛⣤⣏⠀⠀⠀
|    ⠀⠀⢠⠋⢀⣤⣤⡄⠀⠄⠠⠂⠀⠀⠀⠐⢄⡀⠀⠀⠀⠀⠑⢶⣾⣟⡆⠀⠀
|    ⠀⠀⠆⡄⢸⣿⠟⠀⠀⠀⠀⢀⣤⡶⣳⣧⣢⠏⠀⠀⠀⠀⠀⠀⠸⠗⢢⠀⠀
|    ⠀⡈⠀⠃⠀⠀⠀⠀⠀⠀⠀⠙⠻⠾⠿⠟⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀
|    ⠀⠁⣠⡶⢫⢵⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⠀⠇⠀
|    ⢰⠀⡏⡄⣆⠠⣿⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⠀
|    ⠘⠀⢿⣇⣵⢢⣷⡒⠂⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇
|    ⠀⠆⠈⠿⣿⣮⣿⣷⣤⣴⢶⠿⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁
|    ⠀⠈⡆⠀⠐⠚⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
|    ⠀⠀⠃⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
|    ⠀⠘⠠⠤⠤⠤⠭⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠤⠬⠭⠥⠤⠤⠤⠄
|
|   © Cheemsland Pvt Ltd
|   Made by all that is Sigma
|_______________________________________________________________________________________________________________________________________
----------------------------------------------------------------------------------------------------------------------------------------
"""
print(info)

import cv2
# import numpy as np
from tqdm import tqdm
import random

path = input('path(relative path also works, must include extention "*.mp4"): ')
cap = cv2.VideoCapture(path)

image_interpolate_list = [cv2.INTER_NEAREST,cv2.INTER_LINEAR,cv2.INTER_LINEAR_EXACT,cv2.INTER_AREA,cv2.INTER_CUBIC,cv2.INTER_LANCZOS4,cv2.INTER_NEAREST_EXACT,cv2.INTER_MAX,cv2.WARP_FILL_OUTLIERS,cv2.WARP_INVERSE_MAP]

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
color = random.choice(['RED','GREEN','BLUE','CYAN','PINK','YELLOW'])

if cap.isOpened():
    for i in tqdm(range(total_frames), colour = color):
        ret, curr_frame = cap.read()
        if not ret:
            break
        
        out.write(prev_frame)
        intermediate_frame = cv2.addWeighted(prev_frame, 0.5, curr_frame, 0.5, 0)
        # intermediate_frame = cv2.resize(prev_frame, dsize=(width, height), interpolation=cv2.INTER_CUBIC)
        out.write(intermediate_frame)
        
        prev_frame = curr_frame

print(f"new fps: {out_fps}")

cap.release()
out.release()

