import cv2  
# video capture object where 0 is the camera number for a usb camera (orwebcam)
# if 0 doesn't work, you might need to change the camera number to get theright camera you want to access
video = cv2.VideoCapture(0)
i = 0
while(1):
#for i in range(5):
    _,frame = video.read()    # reading one frame from the camera object
    cv2.imshow('Test2',frame)
    cv2.imwrite('Image'+str(i)+'.png', frame)  #Save the image
    if cv2.waitKey(1) & 0xff == ord('q'):   # press q to quit the camera (getout of loop)
        break
video.release()  # Close the cameara
cv2.destroyAllWindows()  #Close all the active windows
