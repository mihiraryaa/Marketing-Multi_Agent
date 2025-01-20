

import warnings
warnings.filterwarnings("ignore")

from typing import List, Optional
from pydantic import BaseModel,Field
import yaml

#langchain setup
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate            
from langchain.schema.output_parser import StrOutputParser  
from langchain.schema.runnable import RunnableMap, RunnableLambda, RunnablePassthrough, RunnableParallel
from langchain_core.utils.function_calling import convert_to_openai_function



#langGraph setup
from langgraph.graph import StateGraph, END
from typing import TypedDict, Annotated, Union, Literal
import operator
from langchain_core.messages import AnyMessage, SystemMessage, HumanMessage, ToolMessage, AIMessage
from langchain_community.tools.tavily_search import TavilySearchResults








#loading environment variables
from dotenv import load_dotenv
import os
load_dotenv()

TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
GROQ_API_KEY=os.getenv("GROQ_API_KEY")

model_llama=ChatGroq(model="llama-3.3-70b-versatile", api_key=GROQ_API_KEY)
