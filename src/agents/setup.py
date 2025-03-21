import os
# import sys
# import autogen
# sys.path.append(os.path.abspath(".."))  

def llm_configuration():
    config_dict = {
        "model" : os.getenv("QA_DEPLOYMENT_NAME"),
        "api_key" : os.getenv("AZURE_OPENAI_API_KEY_QA_LIST"),
        "base_url" : os.getenv("AZURE_OPENAI_ENDPOINT_QA_LIST"),
        "api_type" : "azure",
        "api_version" : os.getenv("OPENAI_API_VERSION_QA"),
    }
    config_list = [config_dict]

    llm_config = {
        "config_list" : config_list,
        "temperature" : 0.0,
        "cache_seed" : None
    }

    return llm_config