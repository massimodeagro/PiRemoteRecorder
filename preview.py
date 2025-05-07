from picamera2 import Picamera2
import time

                      
# adding here static variables for ease of use
res = (2304, 1296)

# main
picam2 = Picamera2()
picam2.preview_configuration.size = res

picam2.start(show_preview=True)
time.sleep(60)
picam2.close()
