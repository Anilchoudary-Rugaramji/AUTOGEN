from autogen_agentchat.agents import CodeExecutorAgent


def getCodeExecutorAgent(code_executor):
    executor = CodeExecutorAgent(
        name="code_executor",
        code_executor=code_executor
    )

    return executor
