import cv2

cap = cv2.VideoCapture(0)

i = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret==True:
        # function(frame) q
        cv2.imshow('frame', frame)

        key = cv2.waitKey(1)
        if key & 0xFF == ord('s'):
            cv2.imwrite('Inhyun'+'%d'%(i)+'.jpg', frame)
            i = i+1
            print('Numbering:','%d'%(i))
        elif key & 0xFF == ord('q'):
            break

cap.release()