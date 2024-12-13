# Agentic-RAG

Agentic-RAG is a multi-agent system designed to interact with various tools and APIs to provide comprehensive responses to user queries. This project leverages OpenAI's GPT-4 model and integrates multiple functionalities such as reading code files, querying databases, and interpreting images.


## Table of Contents
- [Installation](#installation)
- [Project Structure](#project-structure)
- [Usage](#usage)
- [Tools](#tools)
- [Environment Variables](#environment-variables)
- [Demo](#environment-variables)

## Project Structure
```bash
Agentic-RAG/
├── __pycache__/
├── cache/
├── data/
├── exports/
├── test scripts/
├── .env
├── chat_csv.py
├── chat_image.py
├── code_reader.py
├── pandasai.log
├── requirements.txt
├── send_email.py
├── streamlit_main.py
├── tools.py
```


## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Agentic-RAG.git
   cd Agentic-RAG
  

2. Create and activate a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate  # On Windows use `venv\Scripts\activate`
  ```

3. Install the required packages:
  ```bash
  pip install -r requirements.txt
```

4. Set up environment variables:
  Create a .env file in the root directory and add the following variables:
  ```bash
  OPENAI_API_KEY="your_openai_api_key"
  SENDER_EMAIL_ADDRESS="your_email@example.com"
  SENDER_EMAIL_APP_PASSWORD="your_email_app_password"
  ```
## Usage
To start the Streamlit application, run:
  ```bash
  streamlit run streamlit_main.py
  ```

## Key Files
  - chat_csv.py: Handles CSV-related queries.
  - chat_image.py: Encodes images and interacts with the OpenAI API to answer questions based on images.
  - code_reader.py: Reads and returns the contents of code files.
  - send_email.py: Sends emails using the provided SMTP credentials.
  - streamlit_main.py: Main entry point for the Streamlit application.
  - tools.py: Defines various tools and their integrations.

## Tools
The project integrates several tools to handle different types of queries:

  - API Documentation Tool: Queries API documentation.
  - Perks and Benefits Tool: Provides information about company perks and benefits.
  - Policies and Guidelines Tool: Answers questions related to company policies and guidelines.
  - OPD Discount Centers Tool: Provides information about OPD discount centers.
  - Database Tool: Queries SQL databases.
  - Code Reader Tool: Reads and returns the contents of code files.
  - Organizational Structure Tool: Answers questions related to the organizational structure of Emumba.
  - Email Send Tool: Sends emails.
  - Chat OPD Discount Centers Tool: Handles chat-based queries related to OPD discount centers.

## Environment Variables
The project requires the following environment variables:
```bash
OPENAI_API_KEY: Your OpenAI API key.
SENDER_EMAIL_ADDRESS: The email address used to send emails.
SENDER_EMAIL_APP_PASSWORD: The app password for the sender email.
```
## Demo Video
https://github.com/EmumbaOrg/genie-research-experiments/blob/dev/Agentic-RAG/assets/agentic_rag.mp4

