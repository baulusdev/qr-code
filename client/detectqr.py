from qreader import QReader
import cv2
import os
import time
#import rclpy

print(os.getcwd())

# Create a QReader instance
qreader = QReader()

# Get the image that contains the QR code (QReader expects an uint8 numpy array)

num = 0



def getimage(num):
    #get image through webcam
    print('reading image from fs')
    return cv2.imread(f'image{num}.png') 
    print('success')
  


def decode(image):
   # Use the detect_and_decode function to get the decoded QR data
    decoded_text = qreader.detect_and_decode(image)
    print(decoded_text)
    if decoded_text != None:
        with open('data.txt', 'a') as f:
            f.write(f'Image Nr. {num}:{decoded_text}; ')
    

#getwebcam(cam)



if __name__ == '__main__':
    while True:
        num = num + 1
        decode(getimage(num))


