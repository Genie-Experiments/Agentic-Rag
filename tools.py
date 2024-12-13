from dotenv import load_dotenv
from llama_index.llms.openai import OpenAI
from llama_index.core import (
    VectorStoreIndex,
    SimpleDirectoryReader,
)
from llama_index.core import Settings,SQLDatabase
from llama_index.core.tools import QueryEngineTool, ToolMetadata

from typing import List
# text-to-SQL
from sqlalchemy import (
    create_engine,
    MetaData,
    Table,
    Column,
    String,
    Integer,
    VARCHAR,
    Boolean,
    select,
    insert,
    text,

)
from sqlalchemy.exc import IntegrityError
from llama_index.core.indices.struct_store.sql_query import (
    SQLTableRetrieverQueryEngine,
)
from llama_index.core.objects import (
    SQLTableNodeMapping,
    ObjectIndex,
    SQLTableSchema,
)
from llama_index.core.indices.struct_store.sql_query import (
    SQLTableRetrieverQueryEngine,
)
from llama_index.core.objects import (
    SQLTableNodeMapping,
    ObjectIndex,
    SQLTableSchema,
)

load_dotenv()

llm = OpenAI(model="gpt-4", temperature=0.1)

# RAG for api documentation
documents = SimpleDirectoryReader(input_files=["./data/readme.pdf"]).load_data()
Settings.chunk_size = 1024
nodes = Settings.node_parser.get_nodes_from_documents(documents)
index = VectorStoreIndex(nodes)
query_engine_doc = index.as_query_engine(llm=llm)
# tool
api_documentation_tool = QueryEngineTool(
    query_engine=query_engine_doc,
    metadata=ToolMetadata(
        name="api_documentation",
        description="this gives documentation about code for an api.Use this for reading docs for the api"
    )
)

# ------------------------------------------------------------------------------------------------------------------------

# RAG for Perks and Benefits
documents = SimpleDirectoryReader(input_files=["./data/Perks and benefits.pdf"]).load_data()
Settings.chunk_size = 1024
nodes = Settings.node_parser.get_nodes_from_documents(documents)
index = VectorStoreIndex(nodes)
query_engine_perks_and_benefits = index.as_query_engine(llm=llm)
# tool
perks_and_benefits_tool = QueryEngineTool(
    query_engine=query_engine_perks_and_benefits,
    metadata=ToolMetadata(
        name="perks_and_benefits",
        description="""this gives information regarding the Perks and Benfits provided at the company Emumba. It contains the information regarding 
        family health insurance, provident fund, EOBI, retirement fund, home cooked lunch, hostel facility and snack station.
          Use it to asnwer questions regarding the Perks and Benfits, health insurance, provident fund, EOBI, retirement fund, 
          home cooked lunch, hostel facility and snack station"""
    )
)

# ------------------------------------------------------------------------------------------------------------------------

# RAG for Policies and Guidelines
documents = SimpleDirectoryReader(input_files=["./data/Policies and Guidelines.pdf"]).load_data()
Settings.chunk_size = 1024
nodes = Settings.node_parser.get_nodes_from_documents(documents)
index = VectorStoreIndex(nodes)
query_engine_policies_and_guidelines = index.as_query_engine(llm=llm)
# tool
policies_and_guidelines_tool = QueryEngineTool(
    query_engine=query_engine_policies_and_guidelines,
    metadata=ToolMetadata(
        name="policies_and_guidelines",
        description="""this gives information regarding the policies and guidelines of Emumba, work from, leave of absence, hardware and 
        accessories change/replace, reserving a meeting room, smoking area, reimbursements, maternity, paternity, loan application, 
        trips and activities. Use this to answer questions related to the before mentioned topics."""
    )
)

# ------------------------------------------------------------------------------------------------------------------------

# RAG for OPD Discount Centers
documents = SimpleDirectoryReader(input_files=["./data/OPD-Discount-Centers-Nationwide.pdf"]).load_data()
Settings.chunk_size = 1024
nodes = Settings.node_parser.get_nodes_from_documents(documents)
index = VectorStoreIndex(nodes)
query_engine_opd_discount_centres = index.as_query_engine(llm=llm)
# tool
opd_discount_centres_tool = QueryEngineTool(
    query_engine=query_engine_opd_discount_centres,
    metadata=ToolMetadata(
        name="opd_discount_centers",
        description="""this gives information regarding the opd discount centers that are available nationwide. 
        It gives the name, address, contact, discount, city and province of each discount center.The data is in 
        a tabular form with name, address, contract, discount, city and province as the column names. Use this
          to answer questions related to opd dscount centers available nationwide, their name, address, contact, discount, city, province."""
    )
)

# ------------------------------------------------------------------------------------------------------------------------

# RAG for Careers and Growth
documents = SimpleDirectoryReader(input_files=["./data/Careers and Growth.pdf"]).load_data()
Settings.chunk_size = 1024
nodes = Settings.node_parser.get_nodes_from_documents(documents)
index = VectorStoreIndex(nodes)
query_engine_careers_and_growth = index.as_query_engine(llm=llm)
# tool
careers_and_growth_tool = QueryEngineTool(
    query_engine=query_engine_careers_and_growth,
    metadata=ToolMetadata(
        name="careers_and_growth",
        description="""this gives information regarding the careers and growth, 1-to-1 mentoring, SIGs(specialized interest groups),
        , responsibilites of a vertical head, information regarding who is the head of each vertical, responsibilities of an account manager,
          responsibilities of a manager, responsibilities of a proect manager, responsibilities of a technical mentor. Use this
          to answer questions related to the before mentioned topics."""
    )
)

# ------------------------------------------------------------------------------------------------------------------------

# RAG for Clubs and activities
documents = SimpleDirectoryReader(input_files=["./data/Clubs and activities.pdf"]).load_data()
Settings.chunk_size = 1024
nodes = Settings.node_parser.get_nodes_from_documents(documents)
index = VectorStoreIndex(nodes)
query_engine_clubs_and_activities = index.as_query_engine(llm=llm)
# tool
tool_clubs_and_activities = QueryEngineTool(
    query_engine=query_engine_clubs_and_activities,
    metadata=ToolMetadata(
        name="Clubs_and_activities",
        description="""this gives information regarding the emumba's sports clubs, toastmasters club, football club, 
        fitness, table tennis, team activities. Use this to answer questions related to the before mentioned topics."""
    )
)

# ------------------------------------------------------------------------------------------------------------------------

# RAG for Hiring and Onboarding
documents = SimpleDirectoryReader(input_files=["./data/Hiring and Onboarding.pdf"]).load_data()
Settings.chunk_size = 1024
nodes = Settings.node_parser.get_nodes_from_documents(documents)
index = VectorStoreIndex(nodes)
query_engine_hiring_and_onboarding = index.as_query_engine(llm=llm)
# tool
tool_hiring_and_onboarding = QueryEngineTool(
    query_engine=query_engine_hiring_and_onboarding,
    metadata=ToolMetadata(
        name="Hiring_and_Onboarding",
        description="""this gives information regarding emumba's hiring process, onboarding process, referral incentive, 
        conducting interviews(purpose of interview, during interview, the art of turning rejected candidates into allies). Use
          this to answer questions related to the before mentioned topics."""
    )
)

# ------------------------------------------------------------------------------------------------------------------------

# RAG for Performance Appraisals
documents = SimpleDirectoryReader(input_files=["./data/Performance Appraisals.pdf"]).load_data()
Settings.chunk_size = 1024
nodes = Settings.node_parser.get_nodes_from_documents(documents)
index = VectorStoreIndex(nodes)
query_engine_performance_appraisals = index.as_query_engine(llm=llm)
# tool
tool_performance_appraisals = QueryEngineTool(
    query_engine=query_engine_performance_appraisals,
    metadata=ToolMetadata(
        name="Performance_appraisal",
        description="""this gives information regarding emumba's biannual performance reviews and performance evaluation. Use
          this to answer questions related to the before mentioned topics."""
    )
)

# ------------------------------------------------------------------------------------------------------------------------

# RAG for Referral Incentive
documents = SimpleDirectoryReader(input_files=["./data/referral.pdf"]).load_data()
Settings.chunk_size = 1024
nodes = Settings.node_parser.get_nodes_from_documents(documents)
index = VectorStoreIndex(nodes)
query_engine_referral_incentive = index.as_query_engine(llm=llm)
# tool
tool_referral_incentive = QueryEngineTool(
    query_engine=query_engine_referral_incentive,
    metadata=ToolMetadata(
        name="referral_incentive",
        description="""this gives information regarding emumba's biannual performance reviews and performance evaluation. Use
          this to answer questions related to the before mentioned topics."""
    )
)


#
##
### Tool for Text-to-SQL
##
#

### ------------ CREATE DATABASE SCHEMA -----------------
engine = create_engine("sqlite:///dummy.db")

metadata_obj = MetaData()

# create city SQL table
table_name = "city_stats"
city_stats_table = Table(
    table_name,
    metadata_obj,
    Column("city_name", String(16), primary_key=True),
    Column("population", Integer),
    Column("country", String(16), nullable=False),
)

# create employees table
employees_table = Table(
    "employees_info",
    metadata_obj,
    Column("user_id", Integer, primary_key=True, nullable=False, autoincrement=True),
    Column("username", VARCHAR(255)),
    Column("first_name", VARCHAR(50)),
    Column("last_name", VARCHAR(50)),
    Column("gender", VARCHAR(10)),
    Column("password", VARCHAR(50)),
    Column("status", Boolean)
)
metadata_obj.create_all(engine)


### ------------ INSERT DATA -----------------
# add some data to the database
sql_database = SQLDatabase(engine, include_tables=["city_stats","employees_info"])
from sqlalchemy import insert

# add data to city table
rows = [
    {"city_name": "Toronto", "population": 2930000, "country": "Canada"},
    {"city_name": "Tokyo", "population": 17960000, "country": "Japan"},
    {
        "city_name": "Chicago",
        "population": 2679000,
        "country": "United States",
    },
    {"city_name": "Seoul", "population": 9776000, "country": "South Korea"},
]
for row in rows:
    stmt = insert(city_stats_table).values(**row)
    with engine.begin() as connection:
        try:
            cursor = connection.execute(stmt)
        except IntegrityError:
            pass
# add data to employees table 
rows = [
    {"user_id": 1, "username": "rogers63", "first_name": "david", "last_name": "john", "gender": "Female", "password": "e6a33eee180b07e563d74fee8c2c66b8", "status": True},
    {"user_id": 2, "username": "mike28", "first_name": "rogers", "last_name": "paul", "gender": "Male", "password": "2e7dc6b8a1598f4f75c3eaa47958ee2f", "status": True},
    {"user_id": 3, "username": "rivera92", "first_name": "david", "last_name": "john", "gender": "Male", "password": "1c3a8e03f448d211904161a6f5849b68", "status": True},
    {"user_id": 4, "username": "ross95", "first_name": "maria", "last_name": "sanders", "gender": "Male", "password": "62f0a68a4179c5cdd997189760cbcf18", "status": True},
    {"user_id": 5, "username": "paul85", "first_name": "morris", "last_name": "miller", "gender": "Female", "password": "61bd060b07bddfecccea56a82b850ecf", "status": True},
    {"user_id": 6, "username": "smith34", "first_name": "daniel", "last_name": "michael", "gender": "Female", "password": "7055b3d9f5cb2829c26cd7e0e601cde5", "status": True},
    {"user_id": 7, "username": "james84", "first_name": "sanders", "last_name": "paul", "gender": "Female", "password": "b7f72d6eb92b45458020748c8d1a3573", "status": True},
    {"user_id": 8, "username": "daniel53", "first_name": "mark", "last_name": "mike", "gender": "Male", "password": "299cbf7171ad1b2967408ed200b4e26c", "status": True},
    {"user_id": 9, "username": "brooks80", "first_name": "morgan", "last_name": "maria", "gender": "Female", "password": "aa736a35dc15934d67c0a999dccff8f6", "status": True},
    {"user_id": 10, "username": "morgan65", "first_name": "paul", "last_name": "miller", "gender": "Female", "password": "a28dca31f5aa5792e1cefd1dfd098569", "status": True}
]
for row in rows:
    stmt = insert(employees_table).values(**row)
    with engine.begin() as connection:
        try:
            cursor = connection.execute(stmt)  
        except IntegrityError:
            pass


### ------------ CREATE RETRIEVER ENGINE -----------------
# set Logging to DEBUG for more detailed outputs
table_node_mapping = SQLTableNodeMapping(sql_database)

city_stats_text = (
    "This table gives information regarding the population and country of a"
    " given city.\nThe user will query with codewords, where 'foo' corresponds"
    " to population and 'bar'corresponds to city."
)

employees_info_text = (
    """This table gives information regarding employees. Its columns contain information regarding user id,
    first name, last name, user name, password, gender and status """
)

table_schema_objs = [
    (SQLTableSchema(table_name="city_stats",context=city_stats_table)),
    (SQLTableSchema(table_name="employees_info",context=employees_info_text))
] 

obj_index = ObjectIndex.from_objects(
    table_schema_objs,
    table_node_mapping,
    VectorStoreIndex
)
query_engine_database = SQLTableRetrieverQueryEngine(
    sql_database, obj_index.as_retriever(similarity_top_k=1)
)

database_tool = QueryEngineTool(
    query_engine=query_engine_database,
    metadata=ToolMetadata(
        name="database_info",
        description="""this database contains the following tables.
        - city_stats: This table gives information regarding the population and country of a given city. It contains the 
        columns city name, population and country.
        - employees_info: This table gives information regarding employees. Its columns contain information regarding user id,
        first name, last name, user name, password, gender and status.
        An important note: when you are generating sql queries to retrieve data, do not be case sensitive. For example if user wants to find 
        'male' employees, you should look for both 'male' and 'Male'. Hence keep this in mind that the user doesnt always asks the question 
        with the right case sensitivity."""
    )
    # verbose=True
)

