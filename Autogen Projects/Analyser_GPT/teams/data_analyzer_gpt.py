from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from ..agents.Code_executor_agent import getCodeExecutorAgent
from ..agents.Data_analyser_agent import getDataAnalyzerAgent


def dataAnalyzerTeam(model_client, docker):

    code_executor_agent = getCodeExecutorAgent(docker)

    data_analyzer_agent = getDataAnalyzerAgent(model_client=model_client)

    text_mention_termination = TextMentionTermination('STOP')

    team = RoundRobinGroupChat(
        participants=[code_executor_agent, data_analyzer_agent],
        termination_condition=text_mention_termination,
        max_turns=10)

    return team
