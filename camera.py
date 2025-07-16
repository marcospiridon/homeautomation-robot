from picamzero import Camera
import os

home_dir = os.environ['HOME'] #set the location of your home directory
cam = Camera()

cam.take_photo(f"{home_dir}/dev/robot/new_image.jpg") #save the image to your desktop