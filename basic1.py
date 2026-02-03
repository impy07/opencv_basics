import cv2

img = cv2.imread("assets/Logo.png", cv2.IMREAD_GRAYSCALE)
assert img is not None, "Image not found"

img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

cv2.imshow("Logo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
