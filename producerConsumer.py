#!/usr/bin/env python3
import threading
import cv2
import os
import time
import numpy as np
import base64
import queue
import logging, threading, time

def __init__(self):
	# filename of clip to load
      self.message = ""
      self.producer_lock = threading.Lock()
      self.consumer_lock = threading.Lock()
      self.consumer_lock.acquire()
	
def displayFrames(self, inputBuffer):
    # initialize frame count
    count = 0
    # aquire lock
    self.consumer_lock.acquire()
    # go through each frame in the buffer until the buffer is empty
    while not inputBuffer.empty():
        # get the next frame
        frame = inputBuffer.get()

        print(f'Displaying frame {count}')        

        # display the image in a window called "video" and wait 42ms
        # before displaying the next frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(42) and 0xFF == ord("q"):
            break

        count += 1

    print('Finished displaying all frames')
    # cleanup the windows
    cv2.destroyAllWindows()
    self.producer_lock.release()

def extractFrames(self, fileName, outputBuffer, maxFramesToLoad=9999):
    # Initialize frame count 

    #acquire lock
    self.producer_lock.acquire()
    count = 0

    # open video file
    vidcap = cv2.VideoCapture(fileName)

    # read first image
    success,image = vidcap.read()
    
    print(f'Reading frame {count} {success}')
    while success and count < maxFramesToLoad:
        # get a jpg encoded frame
        success, jpgImage = cv2.imencode('.jpg', image)

        #encode the frame as base 64 to make debugging easier
        jpgAsText = base64.b64encode(jpgImage)

        # add the frame to the buffer
        outputBuffer.put(image)
       
        success,image = vidcap.read()
        print(f'Reading frame {count} {success}')
        count += 1
    
    print('Frame extraction complete')
    self.consumer_lock.release()

def toGrayScale(self):
	# globals
      outputDir = 'frames'

	# initialize frame count
      count = 0

	# get the next frame file name
      inFileName = f'{outputDir}/frame_{count:04d}.bmp'


	# load the next file
      inputFrame = cv2.imread(inFileName, cv2.IMREAD_COLOR)

      while inputFrame is not None and count < 72:
            print(f'Converting frame {count}')

    		# convert the image to grayscale
            grayscaleFrame = cv2.cvtColor(inputFrame, cv2.COLOR_BGR2GRAY)
    
    		# generate output file name
            outFileName = f'{outputDir}/grayscale_{count:04d}.bmp'

    		# write output file
            cv2.imwrite(outFileName, grayscaleFrame)

            count += 1

    		# generate input file name for the next frame
            inFileName = f'{outputDir}/frame_{count:04d}.bmp'
    
    		# load the next frame
            inputFrame = cv2.imread(inFileName, cv2.IMREAD_COLOR)





# shared queue  
extractionQueue = queue.Queue()

filename = input("Enter File Name: ")

# extract the frames
extractFrames(filename,extractionQueue, 72)
toGrayScale()
# display the frames
displayFrames(extractionQueue)
#first queue into grayscale
#second queue
#third queue takes grayscale displays
