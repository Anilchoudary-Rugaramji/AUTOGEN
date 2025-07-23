from autogen_agentchat.agents import AssistantAgent
from ..prompt.data_analyzer_message import DATA_ANALYZER_SYSTEM_MESSAGE


def getDataAnayzerAgent(model_client):
    data_analyzer_agent = AssistantAgent(
        name="Data_Analyzer_Agent",
        model_client=model_client,
        description="An agent that solves the data analysis problem and gives the code",
        system_message=DATA_ANALYZER_SYSTEM_MESSAGE,
    )
    return data_analyzer_agent
