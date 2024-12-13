import os
from llama_index.core.tools import FunctionTool

def code_reader_func(file_name):
    file_path = os.path.join(file_name)

    try:
        with open(file_path, "r") as file:
            content = file.read()
            return {"file_content":content}
        
    except Exception as E:
        return {"error": str(E)}    
    

code_reader_tool = FunctionTool.from_defaults(
    fn=code_reader_func,
    name="code_reader",
    description="""this tool can read the contents of code files and return their results.
    Use this when you need to read the contents of a file"""
)    