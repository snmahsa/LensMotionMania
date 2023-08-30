from ..dependencies import *

def bgr_to_hsv(image):
    """
    convert color space . 
    just need send image when initialize class
    """
    return cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

def hsv_to_bgr(image):
    return cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

def rgb_to_hsv(image):
    """
    convert color space . 
    just need send image when initialize class
    """    
    return cv2.cvtColor(image, cv2.COLOR_RGB2HSV)

def hsv_to_bgr(image):
    """
    convert color space . 
    just need send image when initialize class
    """    
    return cv2.cvtColor(image, cv2.COLOR_HSV2BGR)

def rgb_to_gray(image):
    """
    convert color space . 
    just need send image when initialize class
    """    
    return cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

def bgr_to_gray(image):
    """
    convert color space . 
    just need send image when initialize class
    """    
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

def gray_to_bgr(image):
    """
    convert color space . 
    just need send image when initialize class
    """    
    return cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)

def gray_to_rgb(image):
    """
    convert color space . 
    just need send image when initialize class
    """    
    return cv2.cvtColor(image, cv2.COLOR_GRAY2RGB)