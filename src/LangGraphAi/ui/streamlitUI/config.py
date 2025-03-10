import os
from configparser import ConfigParser

class config:
    def __init__(self,config_file="./src/LangGraphAi/ui/streamlitUI/uiconfigfile.ini"):
        self.config= ConfigParser() # It will call ConfigParser
        self.config.read(config_file)

    def get_page_title(self):
        return self.config["DEFAULT"].get("PAGE_TITLE") # TAKES PAGE_TITLE= LangGraph : Develop Agentic AI Applications FROM CONFIG.INI file
    
    def get_llm_options(self):
        return self.config["DEFAULT"].get("LLM_OPTION").split(",")  # use split to take multiple input 
    
    def get_usecase_options(self):
        return self.config["DEFAULT"].get("Usecase_options").split(",")
    
    def get_groq_model_options(self):
        return self.config["DEFAULT"].get("GROQ_MODEL_OPOTIONS").split(",")



        