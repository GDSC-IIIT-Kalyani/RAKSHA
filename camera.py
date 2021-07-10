import cv2
from pose import decorate

class Camera(object):
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        # Define the codec and create VideoWriter object
        self.fourcc = cv2.VideoWriter_fourcc(*'mp4v')
        self.out = cv2.VideoWriter('output.mp4', self.fourcc, 20.0, (640, 480))

    def __del__(self):
        self.cap.release()

    def get_frame(self):
        ret, img = self.cap.read()
        ret, jpg = cv2.imencode(".JPG",decorate(img))
        self.out.write(img)
        return jpg.tobytes()
     
        
 
