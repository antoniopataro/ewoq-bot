import qmme.init as qmme
import seau.init as seau

import screen_controller_utils
from screen_controller_utils import sleep

import pyautogui


def run():
    print("running...")

    ok = screen_controller_utils.start_new_task()

    if ok:
        sleep(5)

    if screen_controller_utils.is_guideline_disclaimer_visible():
        screen_controller_utils.skip_guideline_disclaimer()
        sleep(5)

    if (
        screen_controller_utils.locate_image_center(
            name="seau",
            path="./images/tasks/seau.png",
        )
        != None
    ):
        ok = seau.run()

        if ok:
            sleep(5)

            run()

        raise Exception("seau_failed")

    if (
        screen_controller_utils.locate_image_center(
            name="qmme",
            path="./images/tasks/qmme.png",
        )
        != None
    ):
        ok = qmme.run()

        if ok:
            sleep(5)

            run()

        raise Exception("qmme_failed")


if __name__ == "__main__":
    try:
        run()
    except Exception as e:
        print(e)

        pyautogui.screenshot("./screenshots/restart.png")

        print("restarting...")

        screen_controller_utils.reload_page()

        run()
