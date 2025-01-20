# Multi-Agent Marketing System 🚀

## Overview
This repository contains a **multi-agent system for automated marketing**, built using **LangGraph**. The system leverages **React agents** that collaboratively plan, execute, and evaluate marketing campaigns. The agents utilize real-time **Tavily web search** to ensure access to the latest information and provide cutting-edge strategies for campaign design. The system also supports API integration for enhanced functionality, and API keys are stored securely in environment variables.

---

## Features
- **React Agents**: Dynamically reason and take actions based on given inputs.
- **Multi-Agent Collaboration**: Agents work in tandem to handle different aspects of marketing campaigns such as planning, content creation, and market analysis.
- **Tavily Web Search Integration**: Provides real-time information retrieval capabilities to keep the campaigns up-to-date.
- **Custom Templates and Prompts**: Tailored campaign creation with adjustable inputs.
- **Structured Output**: Campaign plans are generated as markdown files (one file per campaign) for better readability and documentation.
- **API Integration**: Works seamlessly with third-party services using secure environment-based API keys.

---

## Technical Details

### System Design
- **Framework**: Built with **LangGraph**, a tool for designing stateful multi-agent systems.
- **Output**: Campaigns are generated as structured markdown files.
- **Model**: Uses **LLaMA 3.3 70B** via **Groq** for faster inference and high throughput.

### Agent Types
| **Agent Type**         | **Description**                                                                 |
|-------------------------|---------------------------------------------------------------------------------|
| **Campaign Planner**    | Designs strategic marketing campaigns, including targeting and messaging.       |
| **Content Creation**    | Generates creative assets like social media posts, blogs, or ad copy.          |
| **Research Agent**      | Collects real-time information and analyzes market trends using Tavily.         |
| **Campaign Evaluator**  | Reviews and refines campaigns to improve performance and outcomes.              |

---

## Workflow
1. **Initial Input**: Takes user inputs such as company details and project description.
2. **Agent Collaboration**: Each agent performs a specialized task as part of the campaign.
3. **Tavily Web Search**: Ensures campaigns are created with the latest and most relevant data.
4. **Output**: Campaign plans are saved as markdown files for better documentation.

---

## Setup Instructions

### Prerequisites
1. Python >= 3.8
2. API keys for:
   - [OpenAI](https://openai.com/api)
   - [Tavily](https://www.tavily.io)

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/multi-agent-marketing-system.git
   cd multi-agent-marketing-system
