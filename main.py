import cv2
cap=cv2.VideoCapture(0)
bs=cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame=cap.read()
    if not ret:
        break

    gray=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    mask=bs.apply(gray)
    contours, _=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        if cv2.contourArea(contour)>1000:
            x,y,w,h=cv2.boundingRect(contour)
            cv2.rectangle(frame, (x,y) , (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow("Car Movement Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()