from .dependencies import *
class Color:
    """
    Class to convert color space . 
    just need send image when initialize class
    """
    def __init__(self, image) :
        self.image = image

    def bgr_to_hsv(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2HSV)
    
    def hsv_to_bgr(self):
        return cv2.cvtColor(self.image, cv2.COLOR_HSV2BGR)

    def rgb_to_hsv(self):
        return cv2.cvtColor(self.image, cv2.COLOR_RGB2HSV)

    def hsv_to_bgr(self):
        return cv2.cvtColor(self.image, cv2.COLOR_HSV2BGR)
    
    def rgb_to_gray(self):
        return cv2.cvtColor(self.image, cv2.COLOR_RGB2GRAY)

    def bgr_to_gray(self):
        return cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
    
    def gray_to_bgr(self):
        return cv2.cvtColor(self.image, cv2.COLOR_GRAY2BGR)

    def gray_to_rgb(self):
        return cv2.cvtColor(self.image, cv2.COLOR_GRAY2RGB)