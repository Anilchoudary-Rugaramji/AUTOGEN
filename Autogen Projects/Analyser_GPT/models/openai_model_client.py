from autogen_ext.models.openai import OpenAIChatCompletionClient
from ..utils.enumeration import MODEL_TYPE

import os
from dotenv import load_dotenv

load_dotenv()


def get_model_client():
    openai_model_client = OpenAIChatCompletionClient(
        model=str(MODEL_TYPE.GPT_4),
        api_key=os.getenv('OPENAI_API_KEY')
    )
    return openai_model_client
