from picamera2 import Picamera2

# adding here static variables for ease of use
fps = 60
res = (1280, 1024)

# here you have user specified data
file_name = input('please insert the video name: ')

print('please insert the video duration')
recording_duration_h = input('hours: ')
recording_duration_m = input('minutes: ')
recording_duration_s = input('seconds: ')

recording_duration = (int(recording_duration_h)*60 + int(recording_duration_m)) * 60 + int(recording_duration_s) # recording duration total needs to be expressed in seconds

# main
picam2 = Picamera2()
picam2.video_configuration.controls.FrameRate = fps
picam2.preview_configuration.size = res

picam2.start_and_record_video(file_name+'.mp4', duration=recording_duration)
picam2.close()

                             
