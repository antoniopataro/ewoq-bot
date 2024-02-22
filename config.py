from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI
import os
import time


openai_api_key = os.getenv("OPENAI_API_KEY")

openai_client = OpenAI(api_key=openai_api_key)


def is_timer_near_to_expiration(expiration, timer):
    current_time = time.time()

    elapsed_time = current_time - timer

    print("elapsed_time: %s" % elapsed_time)

    if elapsed_time > expiration - 10:
        return True

    return False


def start_timer():
    return time.time()
