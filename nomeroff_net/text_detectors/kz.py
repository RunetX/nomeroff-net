"""
python3 -m nomeroff_net.text_detectors.kz -f nomeroff_net/text_detectors/kz.py
"""
import torch
from .base.ocr import OCR


class Kz(OCR):
    def __init__(self) -> None:
        OCR.__init__(self)
        self.letters = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F", "G", "H",
                        "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        self.max_text_len = 6
        self.max_plate_length = 6
        self.letters_max = len(self.letters)+1
        self.label_length = 32 - 2
        self.init_label_converter()


kz = Kz

if __name__ == "__main__":
    ocr = Kz()
    ocr.load()
    y = ocr.predict(torch.rand((1, 256, 4, 19)))
    print(y)
