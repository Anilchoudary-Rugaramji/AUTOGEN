import asyncio
from Analyser_GPT.teams.data_analyzer_gpt import dataAnalyzerTeam
from Analyser_GPT.models.openai_model_client import get_model_client
from Analyser_GPT.config.docker_utils import getDockerCommandLineExecutor, start_docker_container, stop_docker_container


async def main():
    openai_model_client = get_model_client()
    docker = getDockerCommandLineExecutor()
    team = dataAnalyzerTeam(openai_model_client, docker)

    try:
        task = 'Can you give me a graph of survives and died in my data titanic.csv'
        await start_docker_container(docker)
        async for message in team.run_stream(task=task):
            print(message)
    except Exception as e:
        print(e)
    finally:
        await stop_docker_container(docker)

if __name__ == '__main__':
    asyncio.run(main())
