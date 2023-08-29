from .dependencies import *


def display_hist_plt(image, bins=256, range=(0, 256), figsize=(8, 6), dpi=100):
    """
    Display the histogram of an image using Matplotlib.

    Parameters:
    -----------
    img : numpy.ndarray
        The image to show the histogram for.
    bins : int, optional
        The number of bins used in the histogram. Default is 256.
    range : tuple, optional
        The lower and upper range of the bins. Default is (0, 256).
    figsize : tuple, optional
        The size of the figure. Default is (8, 6).
    dpi : int, optional
        The resolution of the figure. Default is 100.

    Returns:
    --------
    None : NoneType
        This function does not return anything, it only displays the histogram.
    """

    # Check if the input image is a valid numpy array.
    if not isinstance(image, np.ndarray):
        raise TypeError("Input image must be a numpy array.")

    # Create a new figure with the specified size and resolution.
    fig, ax = plt.subplots(figsize=figsize, dpi=dpi)

    # Calculate the histogram of the input image.
    hist, bins = np.histogram(image.ravel(), bins=bins, range=range)

    # Plot the histogram.
    ax.hist(image.ravel(), bins=bins, range=range)

    # Set the axis labels and title.
    ax.set_xlabel('Intensity')
    ax.set_ylabel('Count')
    ax.set_title('Histogram of Image')

    # Show the plot.
    plt.show()