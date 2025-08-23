import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("It's not Open🤷🏻‍♂️")

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Webcam is available", frame)
    
    if cv2.waitKey(10) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()