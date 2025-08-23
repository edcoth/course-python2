import cv2

# print(cv2.__version__)

img = cv2.imread("week01/small-breeds-hero.jpg")

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow("Result", gray)

cv2.waitKey(0)
cv2.destroyAllWindows()