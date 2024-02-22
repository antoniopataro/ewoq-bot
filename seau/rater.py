from dotenv import load_dotenv

load_dotenv()

import seau.prompts as prompts

import ai
from config import openai_client as client
from rater_utils import guarantee_answer_is_in_provided_options

from openai.types.beta.assistant import Assistant
from openai.types.beta.thread import Thread
import os
from typing import Literal

bot_assistant_id = os.getenv("SEAU_OPENAI_ASSISTANT_ID")


def create_assistant() -> Assistant:
    print("creating assistant...")

    assistant = ai.create_assistant(
        instructions=prompts.rater.get("create_assistant"),
        name="seau-rater",
    )

    return assistant


type Interpretation = Literal["MISSING", "NO", "NON_ENGLISH", "UNEXPECTED_PORN", "YES"]

interpratations: list[Interpretation] = [
    "MISSING",
    "NO",
    "NON_ENGLISH",
    "UNEXPECTED_PORN",
    "YES",
]


def interpret_query(assistant: Assistant, query: str, thread: Thread) -> Interpretation:
    print("interpreting query...")

    client.beta.threads.messages.create(
        content=prompts.rater.get("interpret_query") % query,
        role="user",
        thread_id=thread.id,
    )

    run = client.beta.threads.runs.create(
        assistant_id=assistant.id,
        thread_id=thread.id,
    )

    ai.wait_on_run(run=run, thread=thread)

    messages = client.beta.threads.messages.list(thread_id=thread.id)

    last_message = (
        messages.data[0].content[0].text.value.upper().replace('"', "").strip()
    )

    interpretation: Interpretation = guarantee_answer_is_in_provided_options(
        answer=last_message,
        assistant=assistant,
        client=client,
        options=interpratations,
        thread=thread,
    )

    print("interpretation: %s" % interpretation)

    return interpretation


type AdCreativeUsefulness = Literal[
    "COULD_BE_USEFUL",
    "COULD_NEVER_BE_USEFUL",
    "ERROR/DID_NOT_LOAD",
    "UNEXPECTED_PORN",
    "WRONG_LANGUAGE",
]

ad_creative_usefulness_interpratations: list[AdCreativeUsefulness] = [
    "COULD_BE_USEFUL",
    "COULD_NEVER_BE_USEFUL",
    "ERROR/DID_NOT_LOAD",
    "UNEXPECTED_PORN",
    "WRONG_LANGUAGE",
]


def rate_ad_creative_usefulness(
    assistant: Assistant, ad_creative_text: str, thread: Thread
) -> AdCreativeUsefulness:
    print("rating ad creative usefulness...")

    client.beta.threads.messages.create(
        content=prompts.rater.get("rate_ad_creative_usefulness") % ad_creative_text,
        role="user",
        thread_id=thread.id,
    )

    run = client.beta.threads.runs.create(
        assistant_id=assistant.id,
        thread_id=thread.id,
    )

    ai.wait_on_run(run=run, thread=thread)

    messages = client.beta.threads.messages.list(thread_id=thread.id)

    last_message = (
        messages.data[0].content[0].text.value.upper().replace('"', "").strip()
    )

    usefulness: AdCreativeUsefulness = guarantee_answer_is_in_provided_options(
        answer=last_message,
        assistant=assistant,
        client=client,
        options=ad_creative_usefulness_interpratations,
        thread=thread,
    )

    print("usefulness: %s" % usefulness)

    return usefulness


def retrieve_assistant():
    print("retrieving assistant...")

    try:
        assistant = ai.retrieve_assistant(assistant_id=bot_assistant_id)
    except:
        assistant = create_assistant()

    return assistant
