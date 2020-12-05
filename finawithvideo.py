# -*- coding: utf-8 -*-
"""
Created on Thu May  7 17:54:59 2020

@author: RIYA
"""

import cv2
import numpy as np
font = cv2.FONT_HERSHEY_SIMPLEX
cap = cv2.VideoCapture('Crawling.mp4') 

while True:
	ret, frames = cap.read()
	if ret == False:
		break
	else :
		
		img = cv2.cvtColor(frames, cv2.COLOR_BGR2GRAY)
		thresh = 126

		img_binary = cv2.threshold(img, thresh, 255, cv2.THRESH_BINARY)[1]

		kernel = np.ones((17,17), np.uint8) 
		img_erosion = cv2.erode(img_binary, kernel, iterations=1) 

		kernel2 = np.ones((11,11), np.uint8) 
		img_dilation = cv2.dilate(img_erosion, kernel, iterations=1) 



		params = cv2.SimpleBlobDetector_Params()
		params.filterByArea = True
		params.minArea = 250
	
		params.filterByColor = True
		params.blobColor = 255

		params.filterByCircularity = True
		params.minCircularity = 0
		
		params.filterByConvexity = True
		params.minConvexity = 0
		
		ver = (cv2.__version__).split('.')
		if int(ver[0]) < 3 :
		  detector = cv2.SimpleBlobDetector(params)

		else :
			detector = cv2.SimpleBlobDetector_create(params)
		
		
	
		keypoints = detector.detect(img_dilation)

		im_with_keypoints = cv2.drawKeypoints(img_dilation, keypoints, np.array([]), (0,0,255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
		nblobs = len(keypoints)
		print(nblobs)
		nblob=str(nblobs)
		
		#img_final= cv2.putText(im_with_keypoints, nblob, (20,20), font,  
                 #  1, (0,0,255), 2, cv2.LINE_AA)
		#cv2.imshow('video2', im_with_keypoints)
		
		img_final= cv2.putText(frames, nblob, (30,30), font,  
                   1, (0,0,255), 2, cv2.LINE_AA)

		cv2.imshow('video2', frames)
	
		if cv2.waitKey(33)==27:
			break
	
cv2.destroyAllWindows()
  
