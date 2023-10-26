import cv2 as cv

#img=cv.imread('')
#cv.imshow('',img)
#Please refer to function as the in action mode is their

def rescale(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimension = (width,height)
    return cv.resize(frame, dimension, interpolation=cv.INTER_AREA)

cap=cv.VideoCapture(0)
while True:
    isTrue, frame = cap.read()

    frame_resized=rescale(frame)
    #imshow('frame',frame)
    cv.imshow('resize',frame_resized)

    if cv.waitKey(0) & 0xFF('q'):
        break

cap.release()
cv.destroyAllWindows()
