from picamera2 import Picamera2, Preview
import time

# adding here static variables for ease of use
res = (1280, 1024)

# main
picam2 = Picamera2()
picam2.preview_configuration.size = res

picam2.start(show_preview=True)
time.sleep(10)
picam2.close()
