from ..dependencies import * 
class Transform:
    def __init__(self,image):
        self.image = image

    def resize_image(self, x, y):
        """
        Syntax : cv2.resize(source, dsize, dest, fx, fy, interpolation)
        dest, fx, fy, interpolation are [optional]
        """
        return cv2.resize(self.image, (x,y))

    def ratio_resize_image(self, fx, fy):
        """
        Syntax : cv2.resize(source, dsize, dest, fx, fy, interpolation)
        dest, fx, fy, interpolation are [optional]

        Here, the second parameter of the function,
          i.e. None, means to set the image size manually.

        fx and fy are the coefficients that change the size of
          the image in the horizontal and vertical directions, respectively.  
        """
        return cv2.resize(self.image, None, fx=fx, fy=fy)
