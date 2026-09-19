from state import AdvisorState
from utils import get_model_from_gcp
from langgraph.prebuilt import ToolNode, tools_condition
from tools import (
    get_all_prodcuts,
    get_product
)

all_tools = [get_product, get_all_prodcuts]

def get_model_with_tools(tools):
    llm = get_model_from_gcp()
    return llm.bind_tools(tools=tools)

def assistant(state: AdvisorState):
    llm_with_tools = get_model_with_tools(
        tools = all_tools
    )
    # todo: need to add right logic over here
    return state



def get_tool_node() -> ToolNode:
    """This method returns the tool node

    Returns:
        _type_: _description_
    """
    return ToolNode(tools=all_tools)

def capture_customer_info(state: AdvisorState):
    # todo: need to add right logic over here
    return state






    
