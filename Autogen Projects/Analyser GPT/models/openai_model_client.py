from autogen_ext.models.openai import OpenAIChatCompletionClient
from ..utils.enumeration import MODEL_TYPE

import os


def get_model_client():
    openai_model_client = OpenAIChatCompletionClient(
        model=MODEL_TYPE.GPT_4,
        api_key=os.getenv('OPENAI_API_KEY')
    )
