from typing import Callable, List, Tuple
import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import size
from numpy.random import randint

from xcaptcha.types import CAPTCHA


class CAPTCHAGenerator():
    def __init__(self, charset: str, min_size: Tuple[int, int], max_size: Tuple[int, int],
                 min_length: int, max_length: int, fonts: List[str],
                 transformations_under: List[Callable[[np.ndarray], np.ndarray]],
                 transformations_char: List[Callable[[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]],
                 transformations_text: List[Callable[[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]],
                 transformations_over: List[Callable[[np.ndarray], np.ndarray]]):
        self.charset = charset
        self.charset_length = len(self.charset)
        self.min_size = min_size
        self.max_size = max_size
        self.min_length = min_length
        self.max_length = max_length
        self.fonts = fonts
        self.transformations_under = transformations_under
        self.transformations_char = transformations_char
        self.transformations_text = transformations_text
        self.transformations_over = transformations_over

    def __iter__(self) -> CAPTCHA:
        return self.generate()

    def generate(self) -> CAPTCHA:
        n_chars = randint(self.min_length, high=self.max_length)
        chars = randint(0, high=self.charset_length, size=(1, n_chars))
        pass


def generate_captcha(charset: str, min_size: Tuple[int, int], max_size: Tuple[int, int],
                     min_length: int, max_length: int, fonts: List[str],
                     transformations_under: List[Callable[[np.ndarray], np.ndarray]],
                     transformations_char: List[Callable[[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]],
                     transformations_text: List[Callable[[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]],
                     transformations_over: List[Callable[[np.ndarray], np.ndarray]]) -> CAPTCHAGenerator:
    """
    Creates an infinite iterable of CAPTCHA objects.

    The min/max size parameters describe the range of CAPTCHA sizes
    to be generated, while the transformations describe the obfuscation
    to apply to the image. The min/max length parameters describe the
    number of characters that should be included in the CAPTCHA sequence.

    `transformations_under` functions will be create data under the
    text, and `transformations_over` functions will create data over
    the text.

    `transformations_text` and `transformations_char` functions will
    modify the text layer itself. These functions take the image layer
    as their first parameter, and the character mask as their second,
    and should be returned in the same order. Character fonts are chosen
    per character from the `fonts` parameter, which should contain a list
    of font names. 
    """

    # Validation
    assert(min_length >= 0)
    assert(min_length < max_length)

    assert(len(charset) > 0)
    assert(len(fonts) > 0)

    assert(min_size[0] > 0)
    assert(min_size[1] > 0)
    assert(max_size[0] > 0)
    assert(max_size[1] > 0)

    return CAPTCHAGenerator(charset, min_size, max_size, min_length, max_length, fonts,
                            transformations_under, transformations_char, transformations_text, transformations_over)
