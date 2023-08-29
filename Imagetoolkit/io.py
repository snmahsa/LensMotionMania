from .dependencies import *


def read_image(path, mode = -1):
    """
    0 : gray scale
    1 : colorfull
    -1 : same
    """
    return cv2.imread(path, mode)

def upload_image_of_local():

    
    #Hide tk window
    root = tk.Tk()
    root.withdraw()
    #Get image path of local 
    file_path = filedialog.askopenfilename()
    #Select new path for saving
    dest_directory = filedialog.askdirectory()
    #Check
    if file_path and len(dest_directory) != 0 :
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

def read_image_from_folder():
    #get directory path
    project_dir = os.getcwd()
    #creat Image folder path
    DEFAULT_FOLDER_PATH  = os.path.join(project_dir, 'Images/')
    is_exist = os.path.exists(DEFAULT_FOLDER_PATH)
    if not is_exist:
        os.mkdir(DEFAULT_FOLDER_PATH)  

    default_folder_path = DEFAULT_FOLDER_PATH
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

def upload_image_of_url(url):
    """
    return imagr name
    """
    url = url
    response = requests.get(url)
    image = PIL.Image.open(BytesIO(response.content))
    image = np.array(image)
    image = image.astype(float)

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