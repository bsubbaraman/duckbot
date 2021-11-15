from camera_calib import calibrate_chessboard, load_coefficients, save_coefficients

# Parameters
IMAGES_DIR = '/home/pi/duckweed/calibration/images/z_50mm/'
IMAGES_FORMAT = 'jpg'
SQUARE_SIZE = 0.1 #cm
WIDTH = 3
HEIGHT = 3

# Calibrate 
ret, mtx, dist, rvecs, tvecs = calibrate_chessboard(
    IMAGES_DIR, 
    IMAGES_FORMAT, 
    SQUARE_SIZE, 
    WIDTH, 
    HEIGHT
)
# Save coefficients into a file
save_coefficients(mtx, dist, "calibration_chessboard.yml")
