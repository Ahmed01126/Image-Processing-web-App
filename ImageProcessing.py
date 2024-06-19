import cv2
import numpy as np
from Image import *


class Processing:
    def __init__(self, val, uniamp, uniPh, rim):
        self.rim = rim
        self.val = val
        self.uniamp = uniamp
        self.uniPh = uniPh

    def getting_phase_and_magnitude(self, fftShift):
        if self.val == 1:
            val = self.cropping(np.abs(fftShift))
            if self.uniamp != "false":
                val = np.ones(val.shape)

        elif self.val == 0:
            val = np.exp(1j*self.cropping(np.angle(fftShift)))
            if self.uniPh != 'false':
                val = np.ones(val.shape)
        return val

    def cropping(self, arr):
        for i in range(arr.shape[0]):
            for j in range(arr.shape[1]):
                if (i < self.rim[0][0] or i >= self.rim[0][1]) or (j <= self.rim[1][0] or j >= self.rim[1][1]):
                    arr[i][j] = self.val

        return arr

    @staticmethod
    def save_image(path, img):
        with open(path, 'wb'):
            cv2.imwrite(path, img)
