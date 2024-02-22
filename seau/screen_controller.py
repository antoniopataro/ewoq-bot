from seau.positions import positions
import seau.prompts as prompts

import ocr_utils

import pyautogui

pyautogui.useImageNotFoundException()


def read_ad_creative_text():
    print("reading ad creative text...")

    ad_creative_label = ocr_utils.find_text_coordinates("User")

    if ad_creative_label == None:
        print("ad_creative_label_not_found")

        return

    ad_creative_label_x, ad_creative_label_y = ad_creative_label

    pyautogui.screenshot(
        "./screenshots/ad_creative.png",
        region=(ad_creative_label_x, ad_creative_label_y + 220, 800, 400),
    )

    ad_creative = ocr_utils.read_text_from_image("./screenshots/ad_creative.png")

    return ad_creative


def read_query():
    print("reading query...")

    x, y, w, h = positions.get("read_query")

    pyautogui.screenshot(
        "./screenshots/query.png",
        region=(x, y, w, h),
    )

    query = ocr_utils.read_text_from_image("./screenshots/query.png").strip()

    return query


def read_right_prompt(index: int) -> prompts.RightPrompt | None:
    x, y, w, h = positions.get("read_right_prompt")

    pyautogui.screenshot(
        "./screenshots/read_right_prompt%d.png" % index,
        region=(x, y, w, h),
    )

    text = ocr_utils.read_text_from_image(
        "./screenshots/read_right_prompt%d.png" % index
    )

    for right_prompt in prompts.raw_right_prompts:
        if right_prompt in text:
            return right_prompt.replace("\n", " ").strip()

    return None
