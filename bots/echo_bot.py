# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from botbuilder.core import ActivityHandler, MessageFactory, TurnContext
from botbuilder.schema import ChannelAccount
from bots.openai_api import OpenAI
from bots.utils import get_pdf_docs


class EchoBot(ActivityHandler):
    async def on_members_added_activity(
        self, members_added: [ChannelAccount], turn_context: TurnContext
    ):
        for member in members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity("요약하실 논문의 url을 입력하세요!")

    async def on_message_activity(self, turn_context: TurnContext):
        self.api_key = ""
        self.model_name = "gpt-4-1106-preview"
        self.max_new_tokens=4095
        self.temperature=1
        self.top_p=1
        self.url = turn_context.activity.text

        self.openai_bot = OpenAI(self.api_key, self.model_name, self.max_new_tokens, self.temperature, self.top_p)
        prompt = "This GPT is tailored to structure the summaries of English academic papers in Korean using a specified format and telegraphic style. It organizes the summary under specific headers: Title, Date, Affiliation, Purpose, Main Results, and Detailed Results. Each section starts with a header followed by listed items. The purpose and main results are listed directly under their respective headers. Detailed results are further structured with sub-headers for each point. The summaries end each point with the telegraphic style ending in '-임', '-함', etc. This GPT will ensure the summaries are clear, well-organized, and adhere to the specified structure, providing users with a coherent and comprehensive overview of the papers."

        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": get_pdf_docs(self.url, False)},
        ]

        return await turn_context.send_activity(
            MessageFactory.text(self.openai_bot.make_completion(messages))
        )