from llama_index.llms.openai import OpenAI
from dotenv import load_dotenv
import os
from llama_index.core import Settings
from llama_index.core.agent import ReActAgent
from code_reader import code_reader_tool
from tools import (
    api_documentation_tool,perks_and_benefits_tool, policies_and_guidelines_tool,opd_discount_centres_tool,
    database_tool, careers_and_growth_tool, tool_clubs_and_activities, tool_hiring_and_onboarding, 
    tool_performance_appraisals, tool_referral_incentive
)    
from code_reader import code_reader_tool
from chat_image import emumba_organizational_structure_tool
from send_email import email_send_tool
from chat_csv import chat_opd_discount_centers_tool
import streamlit as st


load_dotenv()

groq_api_key = os.getenv("GROQ_API_KEY")
# llm = Groq(model=llm_model_name, api_key=groq_api_key)
llm = OpenAI(model="gpt-4", temperature=0.1)

tools = [
    api_documentation_tool, perks_and_benefits_tool, policies_and_guidelines_tool, 
    opd_discount_centres_tool, database_tool, code_reader_tool, careers_and_growth_tool, tool_clubs_and_activities,
    tool_hiring_and_onboarding, tool_performance_appraisals, tool_referral_incentive, email_send_tool,chat_opd_discount_centers_tool,emumba_organizational_structure_tool
         ]
# tools=[]

llm_code = OpenAI(model="gpt-4", temperature=0.1)

# create agent
agent = ReActAgent.from_tools(tools=tools, llm=llm, verbose=True, context="""Purpose: The role of this agent is to route the
                              questions to the appropriate tools it has. Do not answer questions that are not related to the information that the tools provide.
                               Dont use your own general knowledge to answer unrelated questions.""", max_iterations=100)

#                   #
##                 ##
### streamlit app ###
##                 ##
#                   #

st.title('How can I help you ?')

# prompt = st.text_input('task')
prompt = st.text_area("task", height=200)
if prompt:
    # print(prompt, '\n\n')
    print("User:  ",prompt)
    result = agent.query(prompt)
    st.write(result.response)
    print("Agent: ",result.response)
    print("----------------------------------------------------------------------------------------------------------------")

