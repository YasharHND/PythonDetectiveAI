from google import generativeai


class Gemini:
    def __init__(self, api_key, system_instruction, response_schema=None):
        generativeai.configure(api_key=api_key)
        if response_schema:
            generative_model = generativeai.GenerativeModel(model_name="gemini-1.5-pro",
                                                            safety_settings=4,
                                                            system_instruction=system_instruction,
                                                            generation_config={
                                                                "response_mime_type": "application/json",
                                                                "response_schema": response_schema
                                                            })
        else:
            generative_model = generativeai.GenerativeModel(model_name="gemini-1.5-flash",
                                                            safety_settings=4,
                                                            system_instruction=system_instruction)

        self.session = generative_model.start_chat(history=[])

    def chat(self, user_message):
        response = self.session.send_message(user_message)
        return response.text.strip()
