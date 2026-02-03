import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        exit("No Camera Available")

    image = np.zeros(frame.shape, dtype=np.uint8)
    h, w, _ = frame.shape
    smaller_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

    image[: h // 2, : w // 2, :] = smaller_frame
    image[h // 2 :, : w // 2, :] = smaller_frame
    image[: h // 2, w // 2 :, :] = smaller_frame
    image[h // 2 :, w // 2 :, :] = smaller_frame
    cv2.imshow("Camera", image)

    if cv2.waitKey(1) == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
