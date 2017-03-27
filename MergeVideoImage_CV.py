import cv2.cv as cv
resim = cv.LoadImage('2.jpg')
capture = cv.CaptureFromFile('1.avi')
fourcc = cv.CV_FOURCC(*'DIVX')
out = cv.CreateVideoWriter('output.avi', fourcc, 25, (768,1024))
if not out:
    print "Error in creating video writer"
    sys.exit(1)
while(1):
    frame = cv.QueryFrame(capture)
    cv.SetImageROI(frame,(100,100,resim.width,resim.height))
    cv.Add(frame,resim,frame)
    cv.ResetImageROI(frame)
    cv.ShowImage('frame',frame)
    cv.WriteFrame(out, frame)
    if cv.WaitKey(33)==27:
        break

capture.release() 
#out.release()
cv.ReleaseVideoWriter(out)
cv.destroyAllWindows()