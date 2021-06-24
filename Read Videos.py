#Reading,Writing and Showing videos from webcam

# Importing module
import cv2

# specify video camera device using
cap = cv2.VideoCapture(0)
# capturing the video
fourcc = cv2.VideoWriter_fourcc(*'XVID')
# returning the video to it
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

print(cap.isOpened()) # checking if camera is open

# While True Loop 
while(cap.isOpened()):
    # cap.read() returns two things  1.error  2.frame
    ret, frame = cap.read()

    # Checking The error and procceding
    if ret == True:
      # cap.get(propId)
      print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # for width
      print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # for height

      # Writing the freme to out to create video
      out.write(frame)

      # converting the bgr frame to gray using cvtColor
      gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      # Show the Frame
      cv2.imshow('frame', gray)

      # on click of "q" exit or break the code 
      if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    else:
      break

# Releasing the camera as well as the video we are creating
cap.release()
out.release()
# Destroy the window on action
cv2.destroyAllWindows()


# METHODOLOGY
'''
At first Importing the modules then 
-> the video camera using VideoCapture()
-> if want to record then using VideoWriter_fourcc() and VideoWrite() we can create a file to get recorded
-> using loop we are capturing the frames cap.read() which return 2 values 
-> we are adding the frame in the videowrite we creaded so that at last can create a video 
-> then we can get the frame and using imshow() we can see the video on the window 
-> now to quit the program we are adding a click button functionality linked to wait key
-> releasing the camera and video if recording 
-> destroying the window
'''