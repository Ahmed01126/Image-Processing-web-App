import cv2
from random import randint
import numpy as np
rad = {randint(1, 1*10**5)}


class Image:

    def __init__(self, img):
        self.img = img
        self.width = None
        self.height = None
        self.fourier = None

    def grayScaled_Image(self):
        self.img = cv2.imread(self.img, cv2.IMREAD_GRAYSCALE)

    def getfourier(self, width, height):
        self.grayScaled_Image()
        self.img = cv2.resize(self.img, (width, height))
        # fft2 for 2d fourier transform as the variation of the image happend in two dimension
        fourier = np.fft.fft2((self.img))
        # to avoid the repeation in the frequencies
        fft_shift = np.fft.fftshift(fourier)
        self.img = fft_shift
        # Source: https://stackoverflow.com/questions/59179262/undo-np-fft-fft2-to-get-the-original-image
        return self.img
