import cv2

cap = cv2.VideoCapture("week02/cat-f1.mp4")

while True:
    # section1
    ret, frame = cap.read()
    if not ret:
        break
    # section2
    cv2.imshow("cat driving F1", frame)
    # section3
    if cv2.waitKey(30) & 0xFF == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows() 