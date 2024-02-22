import pyautogui
import time


def close_tab():
    print("closing tab...")

    pyautogui.hotkey("command", "w")


def is_guideline_disclaimer_visible():
    print("checking if guideline disclaimer is visible...")

    try:
        pyautogui.locateCenterOnScreen(
            "./images/guideline_disclaimer_title.png", grayscale=True, confidence=0.9
        )

        return True
    except pyautogui.ImageNotFoundException:
        return False


def locate_image_center(name: str, path: str) -> None | tuple[int, int]:
    try:
        return pyautogui.locateCenterOnScreen(path, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        print("%s_not_found" % name)

        return None


def locate_image_center_and_click(name: str, path: str):
    image_center = locate_image_center(
        name=name,
        path=path,
    )

    if image_center == None:
        return False

    pyautogui.moveTo(
        image_center,
        duration=1,
        tween=pyautogui.easeInOutQuad,
    )
    pyautogui.click()

    return True


def reload_page():
    pyautogui.press("f5")

    sleep(12)


def sleep(seconds: int):
    print("sleeping %ss" % seconds)

    time.sleep(seconds)


def skip_guideline_disclaimer():
    print("skipping guideline disclaimer...")

    locate_image_center_and_click(
        name="guideline_disclaimer_skip_button",
        path="./images/guideline_disclaimer_skip_button.png",
    )


def start_new_task():
    print("starting new task...")

    pyautogui.screenshot("./screenshots/logs/start_new_task.png")

    return locate_image_center_and_click(
        name="start_new_task_button",
        path="./images/start_new_task_button.png",
    )
