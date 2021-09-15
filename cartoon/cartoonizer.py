import cv2 as cv
import numpy as np
import argparse

def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", dest="img_path", help="path to image", default="./sergio.jpg",
                        type=str)
    parser.add_argument("--mode", dest="mode", help="colour/grayscale", default="color",
                        type=str)
    return parser.parse_args()

def cartoonize(img : np.ndarray) -> np.ndarray:
    """
    Turns an image into a cartoon.
    Parameters:
    ----------
        img: The input image to be cartoonized.
    Returns:
    --------
        A cartoonized image.
    """
    #q_img = quantize(img, 25)
    q_img = quantize2(img)
    edge_img = edge(img, 7)
    bf = cv.bilateralFilter(q_img, 9, 150, 150)
    #bf1 = cv.bilateralFilter(img,5, 150, 150)
    #n_edge = edge2(cv.bitwise_and(bf, bf1), 7)
    #cart = cv.bitwise_and(bf, bf1, mask=n_edge)
    #cart = cv.dilate(cart, np.ones((3,3), np.uint8), iterations=1)
    #return cv.bitwise_and(cart, cv.cvtColor(edge_img, cv.COLOR_GRAY2BGR))
    return cv.bitwise_and(bf, cv.cvtColor(edge_img, cv.COLOR_GRAY2BGR))


def gray_cartoon(img : np.ndarray) -> np.ndarray:
    """
    Returns a grayscale vesrsion of the cartoonized image.
    """
    return cv.cvtColor(cartoonize(img), cv.COLOR_BGR2GRAY)

def edge(img : np.ndarray, size : int) -> np.ndarray:
    """
    Detects edges in an image.
    Parameters:
    -----------
        img: The input image.
        size: The size of the kernel matrix.
    Returns:
    --------
        An image with the edges in black.
    """
    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    img_gray = cv.medianBlur(img_gray, size)
    edges = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,
                                size, 15)
    kernel = np.ones((1,1), np.uint8)
    edges = cv.erode(edges, kernel)
    edges = cv.dilate(edges, kernel, iterations=10)
    return edges

def edge2(img : np.ndarray, sz : np.ndarray) -> np.ndarray:

    img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    edges = cv.adaptiveThreshold(img_gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY,
                                sz, 10)
    return edges


def quantize(img : np.ndarray, k : int) -> np.ndarray:
    """
    Reduces the numbers of colors in an image using the kmeans algorithm.
    Parameters:
    ----------
        img: The input image.
        k: The cluster size
    Returns:
    --------
        An image with reduced colors.
    """
    n_img = np.float32(img.reshape((-1,3)))
    criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 5, 1.0)
    ret, label, center = cv.kmeans(n_img, k, None, criteria, 5, cv.KMEANS_RANDOM_CENTERS)
    center = np.uint8(center)
    result = center[label.flatten()]
    return result.reshape(img.shape)

def quantize2(img : np.ndarray) -> np.ndarray:
    """
    Performs similar thing as the quantize 1 function, but its way faster than
    the previous function. But the efficieny is lesser than the previous.
    """

    #n_img = img // div * div + div // 2
    return (img&224) #'11110000'-3bits for each channel


if __name__ == "__main__":
    """args = arg_parser()
    path = args.img_path
    mode = args.mode
    
    img = cv.imread(path)
    if mode in ("color", "colour"):
        cv.imshow("cartoon", cartoonize(img))
    else:
        cv.imshow("gray_cart", gray_cartoon(img))
    cv.waitKey(0)
    """
    videoWriter = None
    fourcc = cv.VideoWriter_fourcc(*"mp4v")
    cap = cv.VideoCapture("./test.mp4")
    while cap.isOpened():
        ret, frame = cap.read()
        if ret:
            cartoonized = cartoonize(frame)
            if not videoWriter:
                videoWriter = cv.VideoWriter("./out.mp4", fourcc, 16, (frame.shape[1], frame.shape[0]))
            videoWriter.write(cartoonized)
        else:
            VideoWriter.release()
            break
    cap.release()
