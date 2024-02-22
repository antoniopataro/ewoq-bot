from config import openai_client as client
from screen_controller_utils import sleep

from openai.types.beta.thread import Thread
from openai.types.beta.threads.run import Run


def create_assistant(
    name: str,
    instructions: str,
):
    assistant = client.beta.assistants.create(
        instructions=instructions,
        name=name,
        model="gpt-3.5-turbo-1106",
    )

    return assistant


def create_thread():
    thread = client.beta.threads.create()

    return thread


def retrieve_assistant(assistant_id: str):
    assistant = client.beta.assistants.retrieve(assistant_id=assistant_id)

    return assistant


def wait_on_run(run: Run, thread: Thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )

    sleep(1)

    return run
