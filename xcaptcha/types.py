from dataclasses import dataclass

import numpy as np


@dataclass
class CAPTCHA():
    """Container class for generated CAPTCHA data."""
    image: np.ndarray
    mask: np.ndarray
    solution: str
