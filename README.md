# Marketing using AI Agents 🚀

## Overview
This project is designed to revolutionize marketing strategy using AI Agents . Built using LangGraph, this system leverages multiple specialized agents to perform key tasks like company research, project planning, content creation, and campaign generation. By integrating Tavily for real-time web search and utilizing powerful LLMs like LLaMA 3.3 70B through Groq for faster inference, this system ensures cutting-edge performance and up-to-date insights. Whether it's developing marketing strategies or generating comprehensive campaign content, the system empowers businesses with automation, scalability, and unparalleled intelligence.

<br> <br>
## Features
- **React Agents**: Dynamically reason and take actions based on the situation.
- **Multi-Agent Collaboration**: Agents work in tandem to handle different aspects of marketing campaigns such as planning, content creation, and market analysis.
- **Tavily Web Search Integration**: Provides real-time information retrieval capabilities to keep the campaigns up-to-date.
- **Fast Inference**: Uses the LLaMA 3.3 70B model via Groq cloud for faster and accurate reasoning and response generation.
- **Structured Output**: Campaign plans are generated as markdown files (one file per campaign) for better readability and documentation.
  You can check out the sample output in the ```sample_output``` folder.

<br>


### Agent Types
| **Agent**         | **Description**                                                                 |
|-------------------------|---------------------------------------------------------------------------------|
| **Research Agent**      | Collects real-time information and analyzes market trends using Tavily.         |
| **Company Researcher**      | gathers and analyzes company-specific data to provide insights for informed decision-making in marketing strategies.|
| **Strategy Planner**    |  Plans the overall marketing strategy based on which the campaigns are designed        |
| **Campaign Planner**    | Designs strategic marketing campaigns, including targeting and messaging.       |
| **Content Creation**    | Generates creative assets like social media posts, blogs, or ad copy for each campaign        |

---

---
<br><br>   
## Installation Guide

Follow the steps below to set up and use the Marketing Multi-Agent system locally:

#### 1. Clone the Repository
Use Git to clone the repository to your local machine:
```bash
git clone https://github.com/mihiraryaa/Marketing-Multi_Agent.git
cd Marketing-Multi_Agent
```

### 2. Set Up Virtual Environment
Create and activate a Python virtual environment:
```bash
# Create a virtual environment
python -m venv env
```
Activate the environment (use the command corresponding to your OS) 

On Windows:
```bash
env\Scripts\activate
```
On macOS/Linux:
```bash
source env/bin/activate
```
### 3. Install Dependencies
Install all required libraries specified in requirements.txt:
```bash
pip install -r requirements.txt
```
### 4. Configure the Environment Variables
The project uses environment variables for secure API key management.
Copy ```.env.example```to ```.env``` and update the placeholder values with your API keys:
```bash
cp .env.example .env
```

### 5. Set Up Input Configuration
Navigate to the ```src/config``` directory.
Open input.yaml and modify it to match your marketing project details. Example

```yaml
company_name:
   <input_company_name>
project_description: 
   <input_project_details>
```
### 6. Run the System
Start the marketing multi-agent system by running:
```bash
cd src
python main.py
```

### 7. View the Outputs
The overall marketing strategy and the generated campaigns will be saved as markdown files in the ```src/outputs/``` directory.

### Notes
1. Using .env vs System Environment Variables: If you prefer storing your API keys in the system environment variables, make sure they are properly configured before running the system. The .env setup is optional and is for convenience.

2. Tavily API Setup: The system uses Tavily for web search.Ensure the TAVILY_API_KEY is valid and has sufficient permissions for advanced searches.

3. Groq rate limits: This system uses Llama 3.3 (70B), hosted via Groq cloud, which has token limits. Refer https://console.groq.com/settings/limits for more information.
