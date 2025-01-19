from imports import *
from langchain_community.tools.tavily_search import TavilySearchResults
tavily_tool = TavilySearchResults(
    max_results=3,          # Maximum number of results to return
    search_depth="advanced", # Level of search depth
)

'''
research-agent(agent+web search) -> based on topic make web-searches and give the final response
input: [system_message, human_message]
output: final ai message (can change this)

'''
class AgentState(TypedDict):
    messages: Annotated[list[AnyMessage], operator.add]

def research_agent(state:AgentState):
    messages=state["messages"]
    model=model_llama.bind_tools([tavily_tool])
    res=model.invoke(messages)
    
    return {"messages": [res]}

def tool_condition(state:AgentState):
    messages=state["messages"]
    return len(messages[-1].tool_calls)>0

def web_search(state:AgentState):
    message=state["messages"][-1]
    results=[]
    for call in message.tool_calls:
        res=tavily_tool.invoke(call["args"])
        results.append(ToolMessage(tool_call_id=call['id'], content=str(res)))

    return {"messages": results}

workflow=StateGraph(AgentState)
workflow.add_node("research_agent", research_agent)
workflow.add_node("web_search_agent", web_search)
workflow.set_entry_point("research_agent")

workflow.add_conditional_edges(
    "research_agent",
    tool_condition,
    {True: "web_search_agent", False: END}
)
workflow.add_edge("web_search_agent", "research_agent")
workflow=workflow.compile()

def research_agent(messages: list[AnyMessage])-> str:
    input={"messages":messages}
    result=workflow.invoke(input)
    return result["messages"][-1].content

