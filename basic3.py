import cv2
import numpy as np


def picker2opencv_hsv(hue, sat, val):
    """
    Conversione dei valori standard picker (geometrici) a
    valori in byte per opencv
    HUE: 0-360 -> 0-180
    SAT: 0-100 -> 0-255
    VAL: 0-100 -> 0-255
    """

    h = int(hue / 2)
    s = int((sat / 100) * 255)
    v = int((val / 100) * 255)

    return np.array([h, s, v], dtype=np.uint8)


cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
heigth = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

while True:
    ret, frame = cap.read()

    if not ret:
        exit("No Camera Available")

    # Conversione per risultati robusti (NOTA: i valori sono in byte, quindi il range è dimezzato da 360 a 180)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Range basso HSV per il rosso
    lowerb_1 = picker2opencv_hsv(0, 70, 40)
    upperb_1 = picker2opencv_hsv(20, 100, 100)

    # Range alto HSV per il rosso (il rosso apre e chiude il cerchio HUE)
    lowerb_2 = picker2opencv_hsv(340, 70, 40)
    upperb_2 = picker2opencv_hsv(360, 100, 100)

    mask_1 = cv2.inRange(frame, lowerb_1, upperb_1)
    final_1 = cv2.bitwise_and(frame, frame, mask=mask_1)

    mask_2 = cv2.inRange(frame, lowerb_2, upperb_2)
    final_2 = cv2.bitwise_and(frame, frame, mask=mask_2)

    final = cv2.bitwise_or(final_1, final_2)

    # Conversione a BGR per imshow
    bgr = cv2.cvtColor(final, cv2.COLOR_HSV2BGR)
    cv2.imshow("Camera", final)

    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
