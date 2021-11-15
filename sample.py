import cv2 as cv

from xcaptcha.defaults import CHARSET_ALPHANUMERIC, FONTS
from xcaptcha.generator import generate_captchas, CAPTCHAGenerator
from xcaptcha.types import CAPTCHA


def main():
    generator: CAPTCHAGenerator = generate_captchas(
        CHARSET_ALPHANUMERIC, (150, 300), (200, 400), 5, 7, FONTS, [], [], [], [])

    captcha: CAPTCHA = next(generator)
    cv.imshow("CAPTCHA", captcha.image)
    cv.waitKey(0)

    merged_masks = generator.merge_masks(list(captcha.masks.values()))
    cv.imshow("Character Masks", merged_masks)
    cv.waitKey(0)


if __name__ == "__main__":
    main()
