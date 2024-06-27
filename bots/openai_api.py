import openai

class OpenAI:
    def __init__(
        self, api_key, model_type, max_new_tokens=2048, temperature=1, top_p=1, **kwargs
    ):
        self.api_key = api_key
        self.model_type = model_type
        openai.api_key = self.api_key
        self.max_new_tokens = max_new_tokens
        self.temperature = temperature
        self.top_p = top_p

    def make_completion(self, messages):
        """
        Sends a request to the ChatGPT API to retrieve a response based on a list of previous messages.
        """
        keep_loop = True
        while keep_loop:
            try:
                return openai.ChatCompletion.create(
                    model=self.model_type,
                    messages=messages,
                    temperature=self.temperature,
                    top_p=self.top_p,
                    max_tokens=self.max_new_tokens,
                    stream=False,
                )["choices"][0]["message"]["content"]
            except Exception as err:
                raise err

        return None
