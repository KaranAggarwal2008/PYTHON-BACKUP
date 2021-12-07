import cv2
import dropbox
import time
import random

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    result = True
    while(result):
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        img_name = "img"+str(number)+".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken")
    # releases the camera
    videoCaptureObject.release()
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

#We need to get the current time and also a random digit for that There are other modules like time and
# random. time.time() module returns time in seconds and the random module
# helps us generate random numbers. To use these modules we need to
# import them first. < run the following code in python shell> 
# Code:-
# import time
# import random
# print(time.time())
# print(random.randint(0,9)
# randint will give a random digit between 0 and 9


# the upload_file function which takes the path from the take_snapshot function and uplaods the images to dropbox>
def upload_file(img_name):
    access_token = "FUMzG2wlw5AAAAAAAAAAAaP45XP7gagFj2aXPSBklBe-JbcbaIkRGz0oBdYY4cD0"
    file =img_name
    file_from = file
    file_to="/image/"+(img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        #Note: in the files_upload method add a parameter mode=dropbox.files.WriteMode.overwrite to resolve the path errors
        dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded")

#define a main function which after every 5 mins calls the take_snapshot and upload_file functions
def main():
    while(True):
        if ((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

#call a main function which after every 5 mins calls the take_snapshot and upload_file function
main()
 