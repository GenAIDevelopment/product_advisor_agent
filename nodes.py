from state import AdvisorState
from utils import get_model_from_gcp
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_core.messages import SystemMessage, BaseMessage, HumanMessage, RemoveMessage
from tools import (
    get_all_products,
    get_product
)
from prompts import SYSTEM_PROMPT

SUMMARY_TRIGGER = 12
KEEP_RECENT = 6

all_tools = [get_product, get_all_products]

def get_model_with_tools(tools):
    llm = get_model_from_gcp()
    return llm.bind_tools(tools=tools)

def assistant(state: AdvisorState):
    llm_with_tools = get_model_with_tools(
        tools = all_tools
    )
    reply = llm_with_tools.invoke([SystemMessage(SYSTEM_PROMPT)] +  state['messages'])
    #state['messages'] = [ reply ]
    return {'messages', [reply]}

def safe_cut(messages: list[BaseMessage], keep_recent:int) -> int:
    cut = len(messages) - keep_recent
    while cut > 0 and not isinstance(messages[cut], HumanMessage):
        cut -= 1
    return cut


def summarize_converstation(state: AdvisorState):
    messages = state['messages']
    cut = safe_cut(messages, KEEP_RECENT)
    old = messages[:cut]
    instruction = (
        "Summarise this part of a product-advice conversations in under 120 words. "
        "Keep the customers state concerns and which products were discussed. "
        "Do not invent anything"
    )
    previous = state.get('summary')
    if previous:
        instruction = f"Summary so far {previous}\n\n{instruction} Extend it"

    summary = get_model_from_gcp().invoke([SystemMessage(instruction)]).content
    return {
        "summary": summary,
        "messages": [RemoveMessage(id=m.id ) for m in old]

    }
    

def get_tool_node() -> ToolNode:
    """This method returns the tool node

    Returns:
        _type_: _description_
    """
    return ToolNode(tools=all_tools)

def capture_customer_info(state: AdvisorState):
    # todo: need to add right logic over here
    return state






    
