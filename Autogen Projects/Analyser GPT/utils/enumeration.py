from enum import Enum


class MODEL_TYPE(Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo-0125"
    GPT_3_5_TURBO_1106 = "gpt-3.5-turbo-1106"
    GPT_4 = "gpt-4"
    GPT_4_1106 = "gpt-4-1106-preview"
    GPT_4V = "gpt-4-1106-vision-preview"

    def __str__(self) -> str:
        return self.value
