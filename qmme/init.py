import qmme.handler as handler
import qmme.steps as steps
import qmme.rater as rater
import qmme.screen_controller as screen_controller

import ai
import config
from screen_controller_utils import sleep

task_expiration_in_seconds = 60 * 5


def run():
    print("running qmme...")

    timer = config.start_timer()

    assistant = rater.retrieve_assistant()
    query = screen_controller.read_query()
    thread = ai.create_thread()

    print("query: %s" % query)

    for step in steps.steps:
        ok = handler.handle_steps(
            assistant=assistant, query=query, step=step, thread=thread
        )

        if ok:
            sleep(5)

            continue

        raise Exception("%s_failed" % step)

    while True:
        if config.is_timer_near_to_expiration(
            expiration=task_expiration_in_seconds, timer=timer
        ):
            break

        sleep(1)

    ok = handler.submit()

    if not ok:
        raise Exception("submit_failed")

    return True
