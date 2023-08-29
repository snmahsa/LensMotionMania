from .dependencies import *
from scipy.ndimage import convolve


def mean_fast_filter(image, window_size=3, padding=0):
    # b, g, r = cv2.split(image)
    # padded_b = cv2.copyMakeBorder(b, padding, padding, padding, padding, cv2.BORDER_CONSTANT)
    # padded_g = cv2.copyMakeBorder(g, padding, padding, padding, padding, cv2.BORDER_CONSTANT)
    # padded_r = cv2.copyMakeBorder(r, padding, padding, padding, padding, cv2.BORDER_CONSTANT)
    # # Apply an average filter to each color channel
    # b_filtered = cv2.blur(padded_b, (window_size, window_size))
    # g_filtered = cv2.blur(padded_g, (window_size, window_size))
    # r_filtered = cv2.blur(padded_r, (window_size, window_size))

    # # Combination of filtered color channels
    # filtered_image = cv2.merge((b_filtered, g_filtered, r_filtered))

    # return filtered_image


    if len(image.shape) == 2:  
        padded_image = cv2.copyMakeBorder(image, padding, padding, padding, padding, cv2.BORDER_CONSTANT)
        output_image =  cv2.blur(padded_image, (window_size, window_size))

    elif len(image.shape) == 3 and image.shape[2] == 3:  
        filtered_channels = []
        for chanl in cv2.split(image):
            filtered_channel= _private_fast_mean(chanl, window_size ,padding )
            filtered_channels.append(filtered_channel)

        output_image = cv2.merge(filtered_channels)

    else:
        raise ValueError("Unsupported image shape. Only grayscale and color images are supported.")

    return output_image


def mean_filter(image, window_size=3,padding=0):
    # Filter window size
    window_half = window_size // 2
    # New image

    if len(image.shape) == 2:  
        height, width = image.shape    
        filtered_image= _private_mean(height, width, image, window_half)
        output_image = filtered_image

    elif len(image.shape) == 3 and image.shape[2] == 3:  
        height, width, ـ = image.shape
        filtered_channels = []
        for chan in cv2.split(image):
            filtered_channel= _private_mean(height, width, chan, window_half)
            filtered_channels.append(filtered_channel)

        output_image = cv2.merge(filtered_channels)

    else:
        raise ValueError("Unsupported image shape. Only grayscale and color images are supported.")


    return output_image

def _private_mean(height,width,part_image, window_half):
    filtered_image = np.zeros_like(part_image)
        # Apply an average filter to each pixel
    for y in range(height):
        for x in range(width):
            # Calculate the neighborhood range for each pixel
            y_min = max(0, y - window_half)
            y_max = min(height, y + window_half + 1)
            x_min = max(0, x - window_half)
            x_max = min(width, x + window_half + 1)

            # Calculate the average values ​​of neighboring pixels
            window = part_image[y_min:y_max, x_min:x_max]
            mean_value = np.mean(window)

            # Assign the mean value to the center pixel
            filtered_image[y, x] = mean_value

    return filtered_image      

def _private_fast_mean(chanl, window_size ,padding):
    # Calculation of padding for each channel
    padded_chanl = cv2.copyMakeBorder(chanl, padding, padding, padding, padding, cv2.BORDER_CONSTANT)
    # Calculate the average for each channel
    chanl_filtered = cv2.blur(padded_chanl, (window_size, window_size))

    return chanl_filtered 

def median(image, window_size, padding=0):
    padded_image = cv2.copyMakeBorder(image, padding, padding, padding, padding, cv2.BORDER_CONSTANT)
    return cv2.medianBlur(padded_image, window_size)