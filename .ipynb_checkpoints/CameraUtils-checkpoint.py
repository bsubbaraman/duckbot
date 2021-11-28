#!/usr/bin/env python
# coding: utf-8

import cv2
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt
import numpy as np


def getCameraIndices():
    """Returns valid camera indices for use with OpenCV"""
    index = 0
    arr = []
    i = 4
    while i > 0:
        try:
            cap = cv2.VideoCapture(index)
            if cap.read()[0]:
                arr.append(index)
                cap.release()
        except:
            print('exception')
        index += 1
        i -= 1
    return arr


def getFrame(idx=0):
    """Return a frame from the specified camera"""
    videoCaptureObject = cv2.VideoCapture(idx)
    for f in range(5): # on mac we have to read several frames
                       # don't have to on the pi
        ret,frame = videoCaptureObject.read()
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
    if ret:
        return frame
    else:
        return "couldn't get frame!"

def saveFrame(idx=0, path="./test.png"):
    """Return a frame from the specified camera and save it to file"""
    videoCaptureObject = cv2.VideoCapture(idx)
    for f in range(5): # on mac we have to read several frames
                       # don't have to on the pi
        ret,frame = videoCaptureObject.read()
        cv2.imwrite(path,frame)
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    
    if ret:
        return frame
    else:
        return "couldn't get frame!"
def showFrame(frame):
    plt.imshow(frame)
    plt.title('frame capture')
    plt.show()
    
def selectPoint(frame):
    plt.imshow(frame)
    plt.title('frame capture')
    pts = plt.ginput(1)[0] #number of clicks
    print(pts)
    plt.close()
    
    return pts

