from os import access
import cv2
from cv2 import VideoCapture
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    videoCaptureObject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time()
        result = False
    print("snapshot taken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return img_name

def upload_file(img_name):
    access_token = "sl.BMq3CCcZ8dvfM3zmyz_kkKRHPp9o1lpp6Eai7pcYmAc0qzYxG-oZdFrfYPf1mXt-JAHfEjWbZwvT2fhjaVukgiVqLD9sWv3acTIoMg5_xBgEqVzNFNs3zHk5vY0Rsm5iv0IxUkw"
    file = img_name
    file_from = file
    file_to = "/Snapshotkobe/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()