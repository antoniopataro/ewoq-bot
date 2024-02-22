import seau.handler as handler
import seau.rater as rater
import seau.screen_controller as screen_controller

import ai
import config
from screen_controller_utils import sleep

task_expiration_in_seconds = 60 * 5


def run():
    print("running seau...")

    timer = config.start_timer()

    assistant = rater.retrieve_assistant()
    query = screen_controller.read_query()
    thread = ai.create_thread()

    print("query: %s" % query)

    prompt_index = 0

    while True:
        if config.is_timer_near_to_expiration(
            expiration=task_expiration_in_seconds, timer=timer
        ):
            raise Exception("is_timer_near_to_expiration")

        right_prompt = screen_controller.read_right_prompt(index=prompt_index)

        if right_prompt == None:
            raise Exception("none_right_prompt")

        ok = handler.handle_right_prompt(
            assistant=assistant, query=query, right_prompt=right_prompt, thread=thread
        )

        if ok:
            prompt_index += 1

            sleep(5)

            continue

        break
