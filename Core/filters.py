from .dependencies import *
from scipy.ndimage import convolve


def mean_filter_color_image(image, window_size):
    b, g, r = cv2.split(image)

    # اعمال فیلتر میانگین بر روی هر کانال رنگی
    b_filtered = cv2.blur(b, (window_size, window_size))
    g_filtered = cv2.blur(g, (window_size, window_size))
    r_filtered = cv2.blur(r, (window_size, window_size))

    # ترکیب کانال‌های رنگی فیلتر شده
    filtered_image = cv2.merge((b_filtered, g_filtered, r_filtered))

    return filtered_image


def mean_filter(image, window_size=3,padding=0):
    # اندازه پنجره فیلتر
    window_half = window_size // 2
    # تصویر جدید

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
        # اعمال فیلتر میانگین بر روی هر پیکسل
    for y in range(height):
        for x in range(width):
            # محاسبه محدوده همسایگی برای هر پیکسل
            y_min = max(0, y - window_half)
            y_max = min(height, y + window_half + 1)
            x_min = max(0, x - window_half)
            x_max = min(width, x + window_half + 1)

            # محاسبه میانگین مقادیر پیکسل‌های همسایه
            window = part_image[y_min:y_max, x_min:x_max]
            mean_value = np.mean(window)

            # اختصاص مقدار میانگین به پیکسل مرکزی
            filtered_image[y, x] = mean_value

    return filtered_image            