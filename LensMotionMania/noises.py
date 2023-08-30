from .dependencies import *

"""
Noise is disturbances in the images that cause a drop in the quality and resolution of the image are called noise.

You create an object from the class and send the image to it. Then you call the functions on that object.
    If the function needs a parameter,you also send it to the function.
    Parameters :
        image : ndarray
        
Class to add different types of noise to an image. The types of noise that can be added are:
- White
- Gaussian
- Speckle
- Salt and Pepper
- Cornerـofـlight
- Circle_periodic
- Diamond_periodic
- Poisson




"""


def white(image,tensity):

    if tensity < 0:
        tensity = 0
    elif tensity > 1:
        tensity = tensity / 100
    
    # noise = np.random.rand(*image.shape)
    image = image.astype(np.float32) / 255
    # Generate white noise with the same size as the image
    noise = np.random.randn(*image.shape) * tensity
    result = image + noise
    #Change to INT
    white_image = np.round(result * 255).clip(0, 255).astype(np.uint8)
    # white_image = np.clip(image + noise, 0, 255)

    # Add the noise to the image with a certain intensity
    return white_image

def gaussian(image, mean=0, var=0.1):
    var = np.sqrt(var)
    image = image.astype(np.float32) / 255
    if image.ndim == 2 :
        rows, cols = image.shape
        #Generating Gaussian noise with normal distribution
        noise = np.random.normal(loc= mean, scale= var, size=(image.shape))
        # noise=np.random.normal(loc= 0, scale= 0.5**0.5, size=(y.shape)).astype('uint8')

        # add noise to the image
        gauss_image = image + image*noise
        # normal
        gauss_image_final = np.clip(gauss_image, 0, 255)
    else:
        rows, cols, channels = image.shape
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

# def gussian_hurt_color(self, mean=0, var=0.1):
#     var = np.sqrt(var)
#     noise = np.random.normal(mean,var,size=image.shape)
#     g_img = image * noise
#     result = g_img.astype(np.uint8)
#     return np.clip(result, 0, 255)
    
def speckle(image, tensity):

    image = image.astype(np.float32) / 255
    # Generate speckle noise with the same size as the image
    noise = np.random.randn(*image.shape) * np.sqrt(tensity)
    result = image + image * noise
    speckle_image = np.round(result * 255).clip(0, 255).astype(np.uint8)
    return speckle_image

def salt_and_pepper(image, amount=0.3, ratio=0.6):
    """
    ratio: Ratio of salt to pepper 
    amount: Overall proportion of image pixels to replace with noise 
    """
    sp_image = np.copy(image)
    num_pixels = int(amount * image.size)
    
    # Generate salt noise
    num_salt = int(num_pixels * ratio)
    # salt_coords = [np.random.choice(dim - 1, num_salt) for dim in sp_image.shape]
    salt_coords = tuple(np.random.randint(0, dim, num_salt) for dim in image.shape)
    #Set
    sp_image[salt_coords] = 255

    # Generate pepper noise
    num_pepper = num_pixels - num_salt
    # pepper_coords = [np.random.choice(dim - 1, num_pepper) for dim in sp_image.shape]
    pepper_coords = tuple(np.random.randint(0, dim, num_pepper) for dim in image.shape)
    #Set
    sp_image[pepper_coords] = 0
    
    return sp_image

def cornerـofـlight(image, frequency_range, amplitude):
    image = image
    len_img = len(image.shape)

    if len(image.shape) == 2:  
        height, width = image.shape
        noise = np.zeros_like(image, dtype=np.float32)
    elif len(image.shape) == 3 and image.shape[2] == 3:  
        height, width, _ = image.shape
        noise = np.zeros_like(image, dtype=np.float32)
    else:
        raise ValueError("Unsupported image shape. Only grayscale and color images are supported.")

    x = np.arange(width)
    y = np.arange(height)
    X, Y = np.meshgrid(x, y)
    if len_img == 3:
        X = np.expand_dims(X, axis=2)
        Y = np.expand_dims(Y, axis=2)

    for f in frequency_range:
        noise += amplitude * np.sin(2 * np.pi * f * X / width + 2 * np.pi * f * Y / height)

    noisy_image = np.clip(image.astype(np.float32) + noise, 0, 255).astype(np.uint8)
    return noisy_image
        
def circle_periodic(image, frequency, amplitude):
    """
    frequency: Determine the frequency of alternating noise
    amplitude: Determination of noise intensity
    """

    if len(image.shape) == 2:  
        height, width = image.shape
        channels = 1
    elif len(image.shape) == 3 and image.shape[2] == 3:  
        height, width, channels = image.shape
    else:
        raise ValueError("Unsupported image shape. Only grayscale and color images are supported.")

    noise = np.zeros_like(image, dtype=np.float32)

    x = np.arange(width)
    y = np.arange(height)
    X, Y = np.meshgrid(x, y)
    center_x = width // 2
    center_y = height // 2

    distance = np.sqrt((X - center_x) ** 2 + (Y - center_y) ** 2)
    noise = amplitude * np.sin(2 * np.pi * frequency * distance)

    if channels == 1:
        noisy_image = np.clip(image.astype(np.float32) + noise, 0, 255).astype(np.uint8)
    else:
        noisy_image = np.clip(image.astype(np.float32) + np.expand_dims(noise, axis=-1), 0, 255).astype(np.uint8)

    return noisy_image

def diamond_periodic(image, frequency, amplitude):
    """
    frequency: Determine the frequency of alternating noise
    amplitude: Determination of noise intensity
    """

    if len(image.shape) == 2:  
        height, width = image.shape
        channels = 1
    elif len(image.shape) == 3 and image.shape[2] == 3:  
        height, width, channels = image.shape
    else:
        raise ValueError("Unsupported image shape. Only grayscale and color images are supported.")

    noise = np.zeros_like(image, dtype=np.float32)

    x = np.arange(width)
    y = np.arange(height)
    X, Y = np.meshgrid(x, y)
    center_x = width // 2
    center_y = height // 2

    distance_x = np.abs(X - center_x)
    distance_y = np.abs(Y - center_y)
    noise = amplitude * np.sin(2 * np.pi * frequency * (distance_x + distance_y))

    if channels == 1:
        noisy_image = np.clip(image.astype(np.float32) + noise, 0, 255).astype(np.uint8)
    else:
        noisy_image = np.clip(image.astype(np.float32) + np.expand_dims(noise, axis=-1), 0, 255).astype(np.uint8)

    return noisy_image

def poisson(image):
    # 0 -- 255
    image = image.astype(np.uint8)

    # Apply the Poisson noise
    noisy = np.random.poisson(image)

    # Normalize the noisy image
    noisy = (noisy - np.min(noisy)) / (np.max(noisy) - np.min(noisy))

    noisy *= 255.0
    noisy = np.around(noisy).astype(np.uint8)

    return noisy


