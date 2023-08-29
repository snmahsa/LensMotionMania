from ..dependencies import * 
def resize_image(image, x, y):
    """
    Syntax : cv2.resize(source, dsize, dest, fx, fy, interpolation)
    dest, fx, fy, interpolation are [optional]
    """
    return cv2.resize(image, (x,y))

def ratio_resize_image(image, fx, fy):
    """
    Syntax : cv2.resize(source, dsize, dest, fx, fy, interpolation)
    dest, fx, fy, interpolation are [optional]

    Here, the second parameter of the function,
      i.e. None, means to set the image size manually.

    fx and fy are the coefficients that change the size of
      the image in the horizontal and vertical directions, respectively.  
    """
    return cv2.resize(image, None, fx=fx, fy=fy)
