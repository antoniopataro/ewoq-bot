from qmme.positions import positions
import qmme.steps as steps
import qmme.rater as rater

import image_recognition_utils
import screen_controller_utils
from screen_controller_utils import sleep

from openai.types.beta.assistant import Assistant
from openai.types.beta.thread import Thread

import pyautogui


def handle_steps(assistant: Assistant, query: str, step: steps.Steps, thread: Thread):
    if step == "is_query_relatable":
        query_relatableness = rater.rate_query_relatableness(
            assistant=assistant, query=query, thread=thread
        )

        if query_relatableness == "RELATABLE":
            return True

        if query_relatableness == "UNRELATABLE":
            screen_controller_utils.locate_image_center_and_click(
                name="unrelatable_query",
                path="./images/0/unrelatable_query.png",
            )

            return True

        return False

    if step == "research_app_and_rate":
        screen_controller_utils.locate_image_center_and_click(
            name="research_mobile_app",
            path="./images/reseach_mobile_app.png",
        )

        sleep(5)

        pyautogui.screenshot("./screenshots/mobile_app_storefront.png")

        mobile_app_storefront_description = image_recognition_utils.describe_image(
            image_path="./screenshots/mobile_app_storefront.png",
        )

        screen_controller_utils.close_tab()

        pyautogui.scroll(-1000)

        satisfaction = rater.rate_mobile_app_storefront_satisfaction(
            assistant=assistant,
            mobile_app_storefront_description=mobile_app_storefront_description,
            thread=thread,
        )

        if satisfaction == "DISSATISFACTION_LIKELY":
            x, y = positions.get("dissatisfaction_likely")

            pyautogui.click(x, y)

            return True

        if satisfaction == "DISSATISFACTION_POSSIBLE":
            x, y = positions.get("dissatisfaction_possible")

            pyautogui.click(x, y)

            return True

        if satisfaction == "NEUTRAL":
            x, y = positions.get("neutral")

            pyautogui.click(x, y)

            return True

        if satisfaction == "SATISFACTION_POSSIBLE":
            x, y = positions.get("satisfaction_possible")

            pyautogui.click(x, y)

            return True

        if satisfaction == "SATISFACTION_LIKELY":
            x, y = positions.get("satisfaction_likely")

            pyautogui.click(x, y)

            return True

        return False

    return False


def submit():
    ok = screen_controller_utils.locate_image_center_and_click(
        name="submit_button",
        path="./images/submit_button.png",
    )

    if ok:
        return True

    return False
