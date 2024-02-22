from qmme.positions import positions

import ocr_utils

import pyautogui

pyautogui.useImageNotFoundException()


def read_query():
    print("reading query...")

    x, y, w, h = positions.get("read_query")

    pyautogui.screenshot(
        "./screenshots/query.png",
        region=(x, y, w, h),
    )

    query = ocr_utils.read_text_from_image("./screenshots/query.png").strip()

    return query
