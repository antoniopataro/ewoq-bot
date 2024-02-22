import seau.screen_controller as screen_controller
import seau.prompts as prompts
import seau.rater as rater

import screen_controller_utils

from openai.types.beta.assistant import Assistant
from openai.types.beta.thread import Thread
import pyautogui


def click_next_question_button():
    ok = screen_controller_utils.locate_image_center_and_click(
        name="next_question_button",
        path="./images/next_question_button.png",
    )

    if not ok:
        raise Exception("next_question_button_not_found")


def handle_right_prompt(
    assistant: Assistant, query: str, right_prompt: prompts.RightPrompt, thread: Thread
):
    if right_prompt == prompts.right_prompts[0]:
        query_interpretation = rater.interpret_query(
            assistant=assistant,
            query=query,
            thread=thread,
        )

        print("query_interpretation: %s" % query_interpretation)

        if query_interpretation == "MISSING":
            raise Exception("query_interpretation_missing")

        if query_interpretation == "NO":
            screen_controller_utils.locate_image_center_and_click(
                name="could_never",
                path="./images/0/no.png",
            )

        if query_interpretation == "NON_ENGLISH":
            raise Exception("query_interpretation_non_english")

        if query_interpretation == "UNEXPECTED_PORN":
            raise Exception("query_interpretation_unexpected_porn")

        if query_interpretation == "YES":
            screen_controller_utils.locate_image_center_and_click(
                name="could_never",
                path="./images/0/yes.png",
            )

        pyautogui.scroll(-50)

        click_next_question_button()

        return True

    if right_prompt == prompts.right_prompts[1]:
        ad_creative_text = screen_controller.read_ad_creative_text()

        usefulness = rater.rate_ad_creative_usefulness(
            ad_creative_text=ad_creative_text,
            assistant=assistant,
            thread=thread,
        )

        print("usefulness: %s" % usefulness)

        if usefulness == "COULD_NEVER_BE_USEFUL":
            screen_controller_utils.locate_image_center_and_click(
                name="could_never",
                path="./images/1/could_never.png",
            )

        if usefulness == "ERROR/DID_NOT_LOAD":
            raise Exception("ad_creative_usefulness_error_did_not_load")

        if usefulness == "UNEXPECTED_PORN":
            raise Exception("ad_creative_usefulness_unexpected_porn")

        if usefulness == "WRONG_LANGUAGE":
            raise Exception("ad_creative_usefulness_wrong_language")

        if usefulness == "COULD_BE_USEFUL":
            screen_controller_utils.locate_image_center_and_click(
                name="could_never",
                path="./images/1/could.png",
            )

        pyautogui.scroll(-50)

        click_next_question_button()

        return True

    return False


# handle_right_prompt(
#     assistant=rater.retrieve_assistant(),
#     query="washing machines at home depot",
#     right_prompt=prompts.right_prompts[1],
#     thread=ai.create_thread(),
# )
