import picamera, time
import random

#Initailise the camera
camera=picamera.PiCamera()

#Generate random prefix
filename = str(random.randint(0, 999)) + "-frame_" 

# The time interval between two pictures, in seconds
timeInterval = 2 

#We have left all the settings in case you need to make some adjustments to improve the picture quality
camera.hflip = True
camera.vflip = True
camera.resolution = (1920, 1080)
camera.led = False

#camera.sharpness = 0
#camera.contrast = 0
#camera.brightness = 50
#camera.saturation = 0
#camera.ISO = 0
#camera.video_stabilization = False
#camera.exposure_compensation = 0
#camera.exposure_mode = 'auto'
#camera.meter_mode = 'average'
#camera.awb_mode = 'auto'
#camera.image_effect = 'none'
#camera.color_effects = None
#camera.rotation = 0
#camera.crop = (0.0, 0.0, 1.0, 1.0)

i=1
try:
    while True: #Infinite Loop
        camera.capture(filename + str(i) + '.jpg')
        print(filename + str(i) + '.jpg')
        time.sleep(timeInterval)
        i+=1
except KeyboardInterrupt: #Press Ctrl+C to interrupt
    pass

print('All done...')