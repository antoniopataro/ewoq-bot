import ai

from openai.types.beta.assistant import Assistant
from openai import OpenAI
from openai.types.beta.thread import Thread


def guarantee_answer_is_in_provided_options(
    answer: str,
    assistant: Assistant,
    client: OpenAI,
    options: list[str],
    thread: Thread,
) -> str:
    retries = 1

    def is_answer_in_provided_options(answer: str) -> bool:
        print(answer)
        print(options)

        for option in options:
            print("answer: %s, option: %s" % answer.upper(), option.upper())
            if answer.upper() in option.upper():
                return True

            return False

    while not is_answer_in_provided_options(answer=answer):
        print("answer: %s" % answer)
        print("guaranteeing answer is in provided options... #%d" % retries)

        if retries > 3:
            raise Exception("answer_not_in_provided_options")

        client.beta.threads.messages.create(
            content="Please answer strictly only with the provided possible options in quotes.",
            role="user",
            thread_id=thread.id,
        )

        run = client.beta.threads.runs.create(
            assistant_id=assistant.id,
            thread_id=thread.id,
        )

        ai.wait_on_run(run=run, thread=thread)

        messages = client.beta.threads.messages.list(thread_id=thread.id)

        answer = messages.data[0].content[0].text.value.upper().replace('"', "").strip()

        retries += 1

    return answer
