import cv2
import numpy as np
import pyautogui
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


def find_text_coordinates(text, lang="en"):
    screenshot = pyautogui.screenshot()

    img = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2GRAY)

    data = pytesseract.image_to_data(img, lang=lang, output_type="data.frame")

    try:
        x, y = (
            data[data["text"] == text]["left"].iloc[0],
            data[data["text"] == text]["top"].iloc[0],
        )

    except IndexError:
        return None

    return (int(x), int(y))


def read_text_from_image(image_path) -> str:
    img = cv2.imread(image_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    text = pytesseract.image_to_string(gray)

    return text
