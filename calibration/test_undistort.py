from camera_calib import load_coefficients
import cv2

# Load coefficients
mtx, dist = load_coefficients('calibration_chessboard.yml')
original = cv2.imread('/home/pi/duckweed/calibration/images/z_50mm/calib_1.jpg')
dst = cv2.undistort(original, mtx, dist, None, None)
cv2.imwrite('undist.jpg', dst)
