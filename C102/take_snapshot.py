import cv2

def take_snapshot():
    #initializing cv2
    videoCaptureObject = cv2.VideoCapture(0,cv2.CAP_DSHOW)
    
    #now we want to run a loop that is infinite so that we can capture every frame
    #a result variable has been declared and its value has been initially set to True for the loop to 
    # continue running and when the result becomes false the loop will stop.
    result = True
    
    # a while loop has been initiated.
    while(result):
  
    #[In the while loop, to read the frames, read() method is used ret, frame = videoCaptureObject.read() 
    #Here ret is a dummy variable which returns a boolean value, basically to tell us if something is being 
    #returned or not. And the frame has the frame of the video]
 
        
        #read the frames while the camera is on
        ret,frame = videoCaptureObject.read()
        #cv2.imwrite() method is used to save an image to any storage device
        cv2.imwrite("NewPicture1.jpg",frame)
        result = False

    # releases the camera
    videoCaptureObject.release()
    
    #To close the webcam the release() method is used. And to close any opened windows 
    # by the camera destroyAllWindows() method is used. As the name suggests it destroys 
    # all the created windows.
    
    #closes all the window that might be opened while this process
    cv2.destroyAllWindows()

#After that the take_snapshot function has been called
take_snapshot()
