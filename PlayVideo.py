import cv2.cv as cv

# create a window
winname = "myWindow"
win = cv.NamedWindow(winname, cv.CV_WINDOW_AUTOSIZE)

# load video file
invideo = cv.CaptureFromFile("1.avi")

# interval between frame in ms.
#fps = cv.GetCaptureProperty(invideo, cv.CV_CAP_PROP_FPS)
#interval = int(1000.0 / fps)   

# play video
while (True):
    im = cv.QueryFrame(invideo)
    cv.ShowImage(winname, im)
    if cv.WaitKey(33) == 27: # ASCII 27 is the ESC key
        break

del invideo
cv.DestroyWindow(winname)