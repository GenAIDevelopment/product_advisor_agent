from langgraph.graph import (
    START, 
    END,
    StateGraph
)
from langgraph.prebuilt import tools_condition
from state import AdvisorState
from nodes import (
    assistant, 
    get_tool_node, 
    capture_customer_info,
    all_tools
)


def create_graph() -> StateGraph:
    """
    This method create a graph
    """
    state_graph = StateGraph(AdvisorState)
    state_graph.add_node("assistant", assistant)
    state_graph.add_node("tools", get_tool_node)
    state_graph.add_node("capture", capture_customer_info)

    #todo: need to define right edges
    state_graph.add_edge(START, "assistant")
    state_graph.add_conditional_edges(
        "assistant",
        tools_condition
    )
    state_graph.add_edge("assistant", "capture")
    state_graph.add_edge("capture", END)
    return state_graph




