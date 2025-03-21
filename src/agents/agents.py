import autogen
import os
import sys
from autogen import UserProxyAgent, register_function, ConversableAgent
sys.path.append(os.path.abspath(".."))
from src.tools import time, weather, country_info

def agents(llm_config):

    with open("agents/prompts/time_agent_prompt.txt", "r", encoding="utf-8") as file:
        times_agent_prompt = file.read()

    with open("agents/prompts/weather_agent_prompt.txt", "r", encoding="utf-8") as file:
        weather_agent_prompt = file.read()

    with open("agents/prompts/countries_info_prompt.txt", "r", encoding="utf-8") as file:
        countries_info_prompt = file.read()

    with open("agents/prompts/orchestrator_prompt.txt", "r", encoding="utf-8") as file:
        orchestrator_prompt = file.read()
    
    with open("agents/prompts/chat_manager_message.txt", "r", encoding="utf-8") as file:
        chat_manager_message = file.read()

    user_proxy = UserProxyAgent(
        name="User_proxy",
        system_message="A human admin.",
        code_execution_config=False,
        human_input_mode="NEVER",
        is_termination_msg=lambda x: x.get("content", "").rstrip().endswith("TERMINATE"),
    )

    times_agent = ConversableAgent(
        name = 'times_agent',
        llm_config = llm_config,
        system_message = times_agent_prompt
    )

    register_function(
        time.get_time_info,
        caller=times_agent,
        executor=user_proxy,
        description="Find exact time of a specific city",
    )

    weather_agent = ConversableAgent(
        name = 'weather_agent',
        llm_config = llm_config,
        system_message =weather_agent_prompt
    )

    register_function(
        weather.get_weather,
        caller=weather_agent,
        executor=user_proxy,
        description="Requesting weather information for a city",
    )

    countries_info_agent = ConversableAgent(
        name = 'countries_info_agent',
        llm_config = llm_config,
        system_message =countries_info_prompt
    )

    register_function(
        country_info.get_country_info,
        caller=countries_info_agent,
        executor=user_proxy,
        description="Requesting information for a specific country",
    )

    orchestrator_agent = ConversableAgent(
        name="Orchestrator_Agent",
        llm_config=llm_config,
        system_message=orchestrator_prompt
    )

    groupchat = autogen.GroupChat(agents=[user_proxy, orchestrator_agent, times_agent, weather_agent, countries_info_agent], messages=[], max_round=15)
    manager = autogen.GroupChatManager(groupchat=groupchat, llm_config=llm_config, system_message=chat_manager_message)

    return user_proxy, orchestrator_agent, times_agent, weather_agent, countries_info_agent, manager