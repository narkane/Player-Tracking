import numpy as np
np.set_printoptions(threshold=np.nan)
import numpy.linalg as la
import cv2
# import cv2.cv as cv
import math
import matplotlib.pyplot as plt
import time

# Count runtime

start_time = time.time()
vid_filepath = '..//vid//panorama.mov'
def on_mouse(event, x, y, flags, param):
    if event == cv2.CV_EVENT_LBUTTONUP:
        print ("col: %d, row: %d" % (x, y))

def main():
    # Read the .mp4 video using OpenCV Python API cv2.VideoCapture

    vid_cap = cv2.VideoCapture(vid_filepath)

    # Print the frame width, frame height, frames per second 
    # and frame count of the input video using cap.get

    fwidth = vid_cap.get(cv2.CV_CAP_PROP_FRAME_WIDTH)
    fheight = vid_cap.get(cv2.CV_CAP_PROP_FRAME_HEIGHT)
    fps = vid_cap.get(cv2.CV_CAP_PROP_FPS)
    fcount = vid_cap.get(cv2.CV_CAP_PROP_FRAME_COUNT)

    print ("Frame width: " + str(fwidth) + "\nFrame height: " + str(fheight) + "\nFrames per second: " + str(fps) + "\nFrame count: " + str(fcount))

    _,img = vid_cap.read()
    filename_topview = '..//img//top-view.jpg'
    
    top_image = cv2.imread(filename_topview)
    
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.namedWindow('frame1')
    cv2.SetMouseCallback('frame1', on_mouse, None)
    cv2.imshow('frame1', top_image)
    cv2.waitKey(0)
    
    
    
    vid_cap.release()

main()
print("Done! Took %s seconds" % (time.time() - start_time))
