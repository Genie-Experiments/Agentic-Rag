from openai import OpenAI
import base64
from dotenv import load_dotenv
from llama_index.core.tools import FunctionTool

load_dotenv()

IMAGE_PATH = "data\organizational structure.png"

# Open the image file and encode it as a base64 string
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

base64_image = encode_image(IMAGE_PATH)

client = OpenAI()

def emumba_organizational_structure(question):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that answers questions from images."},
            {"role": "user", "content": [
                {"type": "text", "text": question},
                {"type": "image_url", "image_url": {
                    "url": f"data:image/png;base64,{base64_image}"}
                }
            ]}
        ],
        temperature=0.0,
    )

    return response.choices[0].message.content

emumba_organizational_structure_tool = FunctionTool.from_defaults(
    fn=emumba_organizational_structure,
    name="emumba_organizational_structure",
    description="""this tool is used to answer the question related to the organizational structure of Emumba. It contains information regarding 
    leadership, engineering managers, project managers and team leads. Use this to answer questions regarding the organizational structure or 
    the position of an employee of emumba."""
)