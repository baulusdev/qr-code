import cv2
import os

print(os.getcwd())

#cam = cv2.VideoCapture(0)
num = 1


def getimg():
    print('getting image')
    cam = cv2.VideoCapture(0)
    result, image = cam.read()
    if result:
        print('success')
        return image
    else:
        return None

def saveimg(image, num):
    print('saving image')
    cv2.imwrite(f'image{num}.png', image)
    print('success')

if __name__ == '__main__':
    while True:
        input("Enter drücken für bild...")#
        saveimg(getimg(), num)
        num += 1


