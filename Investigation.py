import json
import os
import typing

import typing_extensions
from dotenv import load_dotenv

import Instructions
from Wrapper import Gemini

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")


class DetectiveResponseSchema(typing_extensions.TypedDict):
    response_type: typing.Literal["QUESTION", "RESULT"]
    targeted_suspect: typing.Literal["Evelyn Harper", "Jonathan Blackwood", "Dr. Leonard Whitmore"] | None
    content: str


def detective_chat(user_message):
    return json.loads(detective.chat(user_message))


detective = Gemini(api_key=GOOGLE_API_KEY, system_instruction=Instructions.detective_instruction, response_schema=DetectiveResponseSchema)
evelyn = Gemini(api_key=GOOGLE_API_KEY, system_instruction=Instructions.criminal_suspect_instruction)
jonathan = Gemini(api_key=GOOGLE_API_KEY, system_instruction=Instructions.innocent_suspect_instruction)
leonard = Gemini(api_key=GOOGLE_API_KEY, system_instruction=Instructions.innocent_suspect_instruction)

suspects = {
    "Evelyn Harper": evelyn,
    "Jonathan Blackwood": jonathan,
    "Dr. Leonard Whitmore": leonard
}

detective_response = detective_chat("Start your investigation by asking the suspects your questions one by one.")
while detective_response["response_type"] == "QUESTION":
    question = detective_response["content"]
    user_input = input(f"Detective: {question} ")
    if user_input.strip().lower() == "stop":
        break
    suspect_name = detective_response["targeted_suspect"]
    targeted_suspect = suspects[suspect_name]
    suspect_answer = targeted_suspect.chat(question)
    user_input = input(f"{suspect_name}: {suspect_answer} ")
    if user_input.strip().lower() == "stop":
        break
    detective_response = detective_chat(suspect_answer)
else:
    print(f"Result: {detective_response['content']}")
