from .dependencies import *
class Display:
    """
    class to display image :
        with cv2
        with matplotlib.pyplot
        resizable window
        send size for resizable window

    """
    def __init__(self,image):
        self.image = image

    def show_image_cv2(self):
        """
        q for exist 
        """
        cv2.imshow('img_window',self.image)
        while True:
            k = cv2.waitKey(0)
            if k == ord('q'):
                break
            
        cv2.destroywindow('img_window')    
        cv2.destroyAllWindows()

    def show_image_plot(self, cmp = None):
        if cmp is None:
            cmap = 'viridis'
        else:
            cmap = cmp
        
        plt.imshow(self.image, aspect='equal', cmap= cmp)

    def show_in_resizable_window(self):
        #creat window
        cv2.namedWindow('resizable', cv2.WINDOW_NORMAL)
        #show
        cv2.imshow('resizable', self.image)
        cv2.waitKey(0)
        cv2.destroyWindow('v')

    def show_in_selected_resize_Window(self, x, y):
        #creat window
        cv2.namedWindow('resizable', cv2.WINDOW_NORMAL)
        cv2.resizeWindow('resizable', x, y)
        #show
        cv2.imshow('resizable', self.image)
        cv2.waitKey(0)
        cv2.destroyWindow('resizable')
        

        