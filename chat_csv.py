import os
import pandas as pd
from pandasai import Agent
from llama_index.core.tools import FunctionTool

# OPD discount centers
df_opd = pd.read_csv("data\opd_data.csv")
os.environ["PANDASAI_API_KEY"] = "$2a$10$jKZQacg7NVAseQbzS9.aqeQJCc3hus9yyLqJnbYEJNqskYCuaKBuu"
agent_opd = Agent(df_opd)

def chat_opd_discount_centers(question):
    global agent_opd

    return agent_opd.chat(question)

chat_opd_discount_centers_tool = FunctionTool.from_defaults(
    fn=chat_opd_discount_centers,
    name="chat_opd_discount_centers",
    description="""this tool is used to answer questions related to opd discount centers of emumba. The columns of the csv file containing the 
    information are name, address, contact, discount, city and province. Use this when you need to chat about, or retrieve information 
    related to the opd discount discount centers of emumba. The function that is called has one argument named 'question'. An important note: Do 
    not be case sensitive in your search. For example if the user asks you to search for something related to 'mirpur', then also search for 
    'Mirpur' because the user doesnt always enter the right case sensitivity."""
)


