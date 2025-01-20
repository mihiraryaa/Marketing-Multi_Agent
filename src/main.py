from agent_templates import *
from schemas import *
from prompts import * 
import time
from langgraph.checkpoint.memory import MemorySaver
memory=MemorySaver()
from langchain_community.tools.tavily_search import TavilySearchResults
tavily_tool = TavilySearchResults(
    max_results=3,          
    search_depth="advanced",
    api_key=TAVILY_API_KEY
)

def call_model(prompt, model=model_llama):
    res=model.invoke(prompt)
    return res

class AgentState(TypedDict):
    inputs:dict
    research: dict
    strategy: str
    ideas: list[str]
    campaigns: list[str]
    contents: list[str]
    output: str
    


def company_research(state:AgentState):
    inputs=state["inputs"]
    research=state["research"]
    system=SystemMessage(content=company_prompt)
    user=HumanMessage(content=f"#Company name:\n{inputs["company_name"]}\n\n#Project description:\n{inputs["project_description"]}")

    res=research_agent([system,user])
    research["company_report"]=res
    return {"research": research}



def project_research(state:AgentState):
    inputs=state["inputs"]
    research=state["research"]
    system=SystemMessage(content=project_prompt)
    user=HumanMessage(content=f"##Company report:\n{research['company_report']}\n\n\n##Project description:\n{inputs["project_description"]} ")
    prompt=[system,user]
    res=research_agent(prompt)
    research["project_understanding"]=res
    return {"research": research}

def strategy_agent(state:AgentState):
    research=state["research"]
    system=SystemMessage(content=strategy_prompt)
    user=HumanMessage(content=f"#COMPANY REPORT:\n {research['company_report']}\n\n\n#PROJECT UNDERSTANDING:\n{research['project_understanding']}")
    strategy=research_agent([system,user])

    return {"strategy": strategy}

def campaign_ideas_agent(state:AgentState):
    research=state["research"]
    strategy=state["strategy"]
    system=SystemMessage(content=campaign_ideas_prompt)
    user=HumanMessage(content=f"#COMPANY REPORT:\n {research['company_report']}\n\n\n#PROJECT UNDERSTANDING:\n{research['project_understanding']}\n\n\n#MARKETING STRATEGY:\n{strategy}")
    model=model_llama.with_structured_output(campaign_ideas)
    ideas=model.invoke([system,user])
    print(ideas)
    return {"ideas": ideas.ideas}

def campaign_planner_agent(state:AgentState):
    ideas=state["ideas"]
    research=state["research"]
    strategy=state["strategy"]
    campaigns=[]
    system=SystemMessage(content=campaign_planner_prompt)
    for idea in ideas:
        user=HumanMessage(content=f"#MARKETING STRATEGY:\n{strategy}\n\n\n#CAMPAIGN IDEA:\n{idea}")
        model=model_llama.with_structured_output(campaign)
        res=research_agent([system,user])
        campaigns.append(res)
    return {"campaigns": campaigns}

def content_creation_agent(state:AgentState):
    campaigns=state["campaigns"]
    report=state["research"]["company_report"]
    system=SystemMessage(content=content_creation_prompt)
    contents=[]
    for camp in campaigns:
        user=HumanMessage(content=f"#CAMPAIGN PLAN:\n{camp}")
        content=model_llama.invoke([system,user])
        contents.append(content.content)
        print(content.content)
    
    return {"contents": contents}

def write(strategy:str, campaigns:list[str], contents:list[str]):
    file_path="outputs/Marketing_strategy.md"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(strategy)
    nos=1
    for nos in range(len(contents)):
        file_path=f"outputs/campaigns/campaign_{nos+1}.md"
        with open(file_path, "w",encoding="utf-8") as f:
            content=campaigns[nos]+'\n\n\n\n'+ contents[nos]
            f.write(content)


def output(state: AgentState):
    research=state["research"]
    comp_report=research["company_report"]
    project_understanding=research["project_understanding"]
    strategy=state["strategy"]
    campaigns=state["campaigns"]
    contents=state["contents"]
    write(strategy,campaigns, contents)
    print(f"company report:\n{comp_report}\n\n\n\nProject Understanding:\n{project_understanding}")
    print(f'\n\n\nMarketing Strategy: \n{strategy}')
    print("\n\n\n\nCampaigns:\n\n")

    for event in campaigns:
        print(event)
        print('#'*150)
    return {"output": ""}




workflow=StateGraph(AgentState)
workflow.add_node("company_research_agent", company_research)
workflow.add_node("project_research_agent", project_research)
workflow.add_node("strategy_agent", strategy_agent)
workflow.add_node("campaign_ideas_agent", campaign_ideas_agent)
workflow.add_node("campaign_planner_agent", campaign_planner_agent)
workflow.add_node("content_creator_agent", content_creation_agent)
workflow.add_node("output_agent", output)
workflow.set_entry_point("company_research_agent")


workflow.add_edge("company_research_agent", "project_research_agent")
workflow.add_edge( "project_research_agent", "strategy_agent")
workflow.add_edge( "strategy_agent", "campaign_ideas_agent")
workflow.add_edge( "campaign_ideas_agent", "campaign_planner_agent")
workflow.add_edge( "campaign_planner_agent", "content_creator_agent")
workflow.add_edge( "content_creator_agent", "output_agent")
workflow.add_edge("output_agent", END)
workflow=workflow.compile()


input={"inputs": user_query, "research": {}}

for event in workflow.stream(input):
    print(event)
    print('-'*165)


