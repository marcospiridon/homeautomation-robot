# Example using picamera2 (newer library)
from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)})
picam2.configure(camera_config)
picam2.start_preview(Preview.QTGL)
time.sleep(2)
picam2.capture_file("dev/robot/image2.jpg")
picam2.close()