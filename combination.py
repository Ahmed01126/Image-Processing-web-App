from Image import *
from ImageProcessing import *


class ImageCombination:
    def __init__(self, image1, image2):
        self.image1 = image1
        self.image2 = image2

    def get_real(self):
        return np.real(np.fft.ifft2(np.fft.ifftshift(np.multiply(self.image1, self.image2))))
        # Source: https://stackoverflow.com/questions/59179262/undo-np-fft-fft2-to-get-the-original-image

    def Mixing(ch, edges1, edges2, uniPhase, uni_Magn):
        img_1 = Image("static/images/input/Image1.png")
        img_2 = Image("static/images/input/Image2.png")
        processing_for_image1 = Processing(
            edges1, (ch == "option1"), uni_Magn, uniPhase).getting_phase_and_magnitude(img_1.getfourier(width=600, height=427))

        processing_for_image2 = Processing(
            edges2, (ch != "option1"), uni_Magn, uniPhase).getting_phase_and_magnitude(img_2.getfourier(width=600, height=427))

        img_combined = ImageCombination(
            processing_for_image1, processing_for_image2)

        Image_dir = f"static/images/output/rad.png"
        Processing.save_image(Image_dir, img_combined.get_real())
        return Image_dir
