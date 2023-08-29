from .dependencies import *
"""
class to display image :
    with cv2
    with matplotlib.pyplot
    resizable window
    send size for resizable window

"""

def show_image_cv2(image):
    """
    q for exist 
    """
    cv2.imshow('img_window',image)
    while True:
        k = cv2.waitKey(0)
        if k == ord('q'):
            break
        
    cv2.destroywindow('img_window')    
    cv2.destroyAllWindows()

def show_image_plot(image, cmp = None):
    if cmp is None:
        cmap = 'viridis'
    else:
        cmap = cmp
    
    plt.imshow(image, aspect='equal', cmap= cmp)

def show_in_resizable_window(image):
    #creat window
    cv2.namedWindow('resizable', cv2.WINDOW_NORMAL)
    #show
    cv2.imshow('resizable', image)
    cv2.waitKey(0)
    cv2.destroyWindow('v')

def show_in_selected_resize_Window(image, x, y):
    #creat window
    cv2.namedWindow('resizable', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('resizable', x, y)
    #show
    cv2.imshow('resizable', image)
    cv2.waitKey(0)
    cv2.destroyWindow('resizable')

def show_multi_images_plt(image, rows, columns,img_titles, vmin=0, vmax=255):
    images = image
    fig = plt.figure(figsize=(15, 17), dpi=100)
    for i in range(len(images)):
        fig.add_subplot(rows, columns, i+1)
        plt.imshow(images[i], cmap='gray', vmin=vmin, vmax=vmax)
        plt.axis('off')
        plt.title(img_titles[i])        
    

def show_multi_images_cv2(image,rows, cols):
    images = image
    # ساخت یک تصویر خالی برای نمایش عکس‌ها
    display_image = np.zeros((rows * images[0].shape[0], cols * images[0].shape[1], 3), dtype=np.uint8)
    
    # قرار دادن عکس‌ها در تصویر نمایش
    for i in range(rows):
        for j in range(cols):
            if i * cols + j < len(images):
                image = cv2.cvtColor(images[i * cols + j], cv2.COLOR_BGR2RGB)
                display_image[i * images[0].shape[0]:(i + 1) * images[0].shape[0], j * images[0].shape[1]:(j + 1) * images[0].shape[1]] = image
    
    # نمایش تصویر نمایش
    cv2.imshow("Images", display_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()    

    