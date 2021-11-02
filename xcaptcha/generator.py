from typing import Callable, List, Tuple
import cv2 as cv
import numpy as np

from xcaptcha.types import CAPTCHA


class CAPTCHAGenerator():
    def __init__(self, charset: str, min_size: Tuple[int, int], max_size: Tuple[int, int], fonts: List[str],
                 transformations_under: List[Callable[[np.ndarray], np.ndarray]],
                 transformations_text: List[Callable[[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]],
                 transformations_over: List[Callable[[np.ndarray], np.ndarray]]):
        self.charset = charset
        self.min_size = min_size
        self.max_size = max_size
        self.fonts = fonts
        self.transformations_under = transformations_under
        self.transformations_text = transformations_text
        self.transformations_over = transformations_over

    def __iter__(self) -> CAPTCHA:
        pass


def generate_captcha(charset: str, min_size: Tuple[int, int], max_size: Tuple[int, int], fonts: List[str],
                     transformations_under: List[Callable[[np.ndarray], np.ndarray]],
                     transformations_text: List[Callable[[np.ndarray, np.ndarray], Tuple[np.ndarray, np.ndarray]]],
                     transformations_over: List[Callable[[np.ndarray], np.ndarray]]) -> CAPTCHAGenerator:
    """
    Creates an infinite iterable of CAPTCHA objects.

    The min/max size parameters describe the range of CAPTCHA sizes
    to be generated, while the transformations describe the obfuscation
    to apply to the image. `transformations_under` functions will be
    create data under the text, and `transformations_over` functions
    will create data over the text. `transformations_text` functions
    will modify the text layer itself. These functions take the image
    layer as their first parameter, and the character mask as their
    second, and should be returned in the same order. Character fonts
    are chosen per character from the `fonts` parameter, which should
    contain a list of font names. 
    """

    # Validation
    assert(len(charset) > 0)
    assert(len(fonts) > 0)
    assert(min_size[0] > 0)
    assert(min_size[1] > 0)
    assert(max_size[0] > 0)
    assert(max_size[1] > 0)

    return CAPTCHAGenerator(charset, min_size, max_size, fonts, transformations_under, transformations_text, transformations_over)
