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
    targeted_suspect: typing.Literal["Elena Rivers", "Professor Gregory Shaw", "Henry Lang"] | None
    content: str


detective = Gemini(api_key=GOOGLE_API_KEY, system_instruction=Instructions.detective_instruction, response_schema=DetectiveResponseSchema)
elena = Gemini(api_key=GOOGLE_API_KEY, system_instruction=Instructions.innocent_suspect_instruction)
gregory = Gemini(api_key=GOOGLE_API_KEY, system_instruction=Instructions.criminal_suspect_instruction)
henry = Gemini(api_key=GOOGLE_API_KEY, system_instruction=Instructions.innocent_suspect_instruction)

suspects = {
    "Elena Rivers": elena,
    "Professor Gregory Shaw": gregory,
    "Henry Lang": henry
}

detective_response = detective.chat("Start your investigation by asking the suspects your questions one by one.")
while detective_response["response_type"] == "QUESTION":
    question = detective_response["content"]
    print(f"Detective: {question}")
    suspect_name = detective_response["targeted_suspect"]
    targeted_suspect = suspects[suspect_name]
    suspect_answer = targeted_suspect.chat(question)
    print(f"{suspect_name}: {suspect_answer}\n")
    detective_response = detective.chat(suspect_answer)
else:
    print(f"Result: {detective_response['content']}")
