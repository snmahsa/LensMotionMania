from .dependencies import *
class Noise:
    def __init__(self,image):
        self.image = image

    def white(self,tensity):

        if tensity < 0:
            tensity = 0
        elif tensity > 1:
            tensity = tensity / 100
        
        # noise = np.random.rand(*self.image.shape)
        image = self.image.astype(np.float32) / 255
        # Generate white noise with the same size as the image
        noise = np.random.randn(*self.image.shape) * tensity
        white_image = np.clip(image + noise, 0, 255)
        # Add the noise to the image with a certain intensity
        return white_image
    
    # def gaussian_normalize(self, mean= 0, var= 0.1):

    #     var = np.sqrt(var)
    #     # ایجاد نویز گوسی با توزیع نرمال
    #     noise = np.random.normal(loc= mean, scale= var, size=(self.image.shape))

    #     # افزودن نویز به تصویر
    #     gauss_image = self.image + self.image*noise
    #     gauss_image = cv2.normalize(gauss_image, None, 0, 255, cv2.NORM_MINMAX)

    #     return gauss_image 


    def gaussian(self, mean=0, var=0.1):
        var = np.sqrt(var)
        image = self.image.astype(np.float32) / 255
        if self.image.ndim == 2 :
            rows, cols = self.image.shape
            # ایجاد نویز گوسی با توزیع نرمال
            noise = np.random.normal(loc= mean, scale= var, size=(self.image.shape))
            # noise=np.random.normal(loc= 0, scale= 0.5**0.5, size=(y.shape)).astype('uint8')

            # add noise to the image
            gauss_image = self.image + self.image*noise
            # normal
            gauss_image_final = np.clip(gauss_image, 0, 255)
        else:
            rows, cols, channels = self.image.shape
            b, g, r = cv2.split(image)

             # Generate noise with normal distribution for each color channel
            noise_b = np.random.normal(mean, var, (rows, cols))
            noise_g = np.random.normal(mean, var, (rows, cols))
            noise_r = np.random.normal(mean, var, (rows, cols))

            # add noise to the image
            noisy_b = b + b*noise_b
            noisy_g = g + g*noise_g
            noisy_r = r + r*noise_r

            gauss_image = cv2.merge((noisy_b, noisy_g, noisy_r))
            # normal
            gauss_image_final = np.clip(gauss_image, 0, 255)

        
        return gauss_image_final
           