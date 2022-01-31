import cv2
import numpy as np


def empty(_):
    pass

cv2.namedWindow("TrackBars")
cv2.resizeWindow("TrackBars", 640, 240)
cv2.createTrackbar("Green", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Red", "TrackBars", 0, 255, empty)
cv2.createTrackbar("Blue", "TrackBars", 0, 255, empty)

selectedRedCol = 0
selectedBlueCol = 0
selectedGreenCol = 0

while True:
    image = cv2.imread("test.png")
    redColor = cv2.getTrackbarPos("Red", "TrackBars")
    greenColor = cv2.getTrackbarPos("Green", "TrackBars")
    blueColor = cv2.getTrackbarPos("Blue", "TrackBars")
    image[np.where((image != [255, 255, 255]).all(axis=2))] = (blueColor, greenColor, redColor)
    cv2.imshow("Result", image)

    # save
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("result.png", image)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()