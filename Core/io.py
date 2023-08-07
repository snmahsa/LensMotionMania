from .dependencies import *
class Io:
    """
    Class for upload , read 
    """
    def __init__(self) -> None:
        pass

    def read_image(self, path, mode = -1):
        """
        0 : gray scale
        1 : colorfull
        -1 : same
        """
        return cv2.imread(path, mode)

    def upload_image_of_local(self):

        
        #Hide tk window
        root = tk.Tk()
        root.withdraw()
        #Get image path of local 
        file_path = filedialog.askopenfilename()
        #Select new path for saving
        dest_directory = filedialog.askdirectory()
        #Check
        if file_path and dest_directory != 0 :
            #Read image
            image = cv2.imread(file_path)
            #Save
            file_name = os.path.basename(file_path)
            cv2.imwrite(os.path.join(dest_directory, file_name), image)
            # shutil.copy(file_path,dest_directory)
            # image = cv2.imread(file_path)
            # return file_name
        else:
            print("No file selected")

    def read_image_from_folder(self):
        default_folder_path = 'Image/'
        #Hide tk window
        root = tk.Tk()
        root.withdraw()
        #Get image path
        file_path = filedialog.askopenfilename(initialdir=default_folder_path)
        #read image
        image = cv2.imread(file_path)
        #check successfully
        if image is None:
            print("Unable to read image")
            return None
        else:
            return image

    def upload_image_of_url(self, url):
        """
        return imagr name
        """
        url = url
        response = requests.get(url)
        image = PIL.Image.open(BytesIO(response.content))
        image = np.array(image)
        image = self.image.astype(float)

        #Select new path for saving
        dest_directory = filedialog.askdirectory()
        #Check
        if image.size > 0 and dest_directory != 0 :
            #Save
            file_name = os.path.basename(url)
            cv2.imwrite(os.path.join(dest_directory, file_name), image)

            # return file_name
        else:
            print("No file selected")