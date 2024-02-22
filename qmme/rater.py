from dotenv import load_dotenv

load_dotenv()

import qmme.prompts as prompts

import ai
from config import openai_client as client
from rater_utils import guarantee_answer_is_in_provided_options

from openai.types.beta.assistant import Assistant
from openai.types.beta.thread import Thread
import os
from typing import Literal

bot_assistant_id = os.getenv("QMME_OPENAI_ASSISTANT_ID")


def create_assistant() -> Assistant:
    print("creating assistant...")

    assistant = ai.create_assistant(
        instructions=prompts.rater.get("create_assistant"),
        name="qmme-rater",
    )

    return assistant


type Satisfaction = Literal[
    "DISSATISFACTION_LIKELY",
    "DISSATISFACTION_POSSIBLE",
    "NEUTRAL",
    "SATISFACTION_POSSIBLE",
    "SATISFACTION_LIKELY",
]

satisfactions: list[Satisfaction] = [
    "DISSATISFACTION_LIKELY",
    "DISSATISFACTION_POSSIBLE",
    "NEUTRAL",
    "SATISFACTION_POSSIBLE",
    "SATISFACTION_LIKELY",
]


def rate_mobile_app_storefront_satisfaction(
    assistant: Assistant, mobile_app_storefront_description: str, thread: Thread
):
    print("rating mobile app storefront satisfaction...")

    client.beta.threads.messages.create(
        content=prompts.rater.get("rate_mobile_app_storefront_satisfaction")
        % mobile_app_storefront_description,
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

    satisfaction: Satisfaction = guarantee_answer_is_in_provided_options(
        answer=last_message,
        assistant=assistant,
        client=client,
        options=satisfactions,
        thread=thread,
    )

    return satisfaction


type Relatableness = Literal["RELATABLE", "UNRELATABLE"]

relatablenesses: list[Relatableness] = ["RELATABLE", "UNRELATABLE"]


def rate_query_relatableness(assistant: Assistant, query: str, thread: Thread):
    print("rating query relatableness...")

    client.beta.threads.messages.create(
        content=prompts.rater.get("rate_query_relatableness") % query,
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

    relatableness: Relatableness = guarantee_answer_is_in_provided_options(
        answer=last_message,
        assistant=assistant,
        client=client,
        options=relatablenesses,
        thread=thread,
    )

    print("relatableness: %s" % relatableness)

    return relatableness


def retrieve_assistant():
    print("retrieving assistant...")

    try:
        assistant = ai.retrieve_assistant(assistant_id=bot_assistant_id)
    except:
        assistant = create_assistant()

    return assistant
