
'''
#RAG imports
import bs4
from uuid import uuid4
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain_community.document_loaders import DirectoryLoader


from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_pinecone import PineconeVectorStore
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

'''





import warnings
warnings.filterwarnings("ignore")

from typing import List, Optional
from pydantic import BaseModel,Field


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





#all the models
model_openai=ChatOpenAI(model="gpt-4o-mini", temperature=1)
model_llama=ChatGroq(model="llama-3.3-70b-versatile")
model_llama2=ChatGroq(model="llama-3.3-70b-specdec")
model_llama=model_openai
model_llama_vision=ChatGroq(model="llama-3.2-11b-vision-preview")



