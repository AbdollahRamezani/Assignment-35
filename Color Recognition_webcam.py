import cv2
import numpy as np

cap = cv2.VideoCapture(0)

_, frame = cap.read()
rows = frame.shape[0]
cols = frame.shape[1]

writer = cv2.VideoWriter("output/color_detector_webcam.mp4", cv2.VideoWriter_fourcc(*'MJPG'), 8, (cols, rows))

while  True:
    _, frame = cap.read()
    rectangle = cv2.rectangle(frame, (290, 200), (370, 275), 0, 1)

    for i in range(240, 260):
        for j in range(315, 345) :
            B,G,R=frame[i, j]

            if R>200 and G<100 and B<100:       
                cv2.putText(frame, "RED", (0, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, 0)
            elif R<100 and G>200 and B<100:       
                cv2.putText(frame, "GREEN", (0, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, 0)  
            elif R<150 and G<150 and B>200:       
                cv2.putText(frame, "BLUE", (0, 50), cv2.FONT_HERSHEY_PLAIN, 1.5, 0)        
               
  
    writer.write(frame)
    cv2.imshow("result", frame)
    if cv2.waitKey(25) & 0xFF==ord("q"):
        break

writer.release() 
cap.release()

       


