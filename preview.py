from picamera2 import Picamera2, Preview
from libcamera import controls
import time

lens_position = float(input('specify lens position from 0 to 1'))
                      
# adding here static variables for ease of use
res = (1280, 1024)

# main
picam2 = Picamera2()
picam2.preview_configuration.size = res
picam2.set_controls({"AfMode": controls.AfModeEnum.Manual, "LensPosition": lens_position})

picam2.start(show_preview=True)
time.sleep(10)
picam2.close()
