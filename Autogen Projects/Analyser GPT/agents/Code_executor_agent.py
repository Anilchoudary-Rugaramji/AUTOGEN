from autogen_agentchat.agents import CodeExecutorAgent


def getCodeExecutor(code_executor):
    executor = CodeExecutorAgent(
        name="code_executor",
        code_executor=code_executor
    )

    return executor
