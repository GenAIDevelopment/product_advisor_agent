from typing import TypedDict, Optional, Annotated
from langchain_core.messages import (
    AIMessage, 
    SystemMessage, 
    HumanMessage, 
    ToolMessage,
    BaseMessage
)
from langgraph.graph import add_messages, MessagesState

# class MyState(MessagesState):
#     product_id: Optional[str]
#     mobile_number: Optional[str]
#     email: Optional[str]
#     customer_name: Optional[str]
#     lead_status: Optional[str]

class AdvisorState(TypedDict, total=False):
    messages: Annotated[ list[BaseMessage], add_messages] 
    product_id: Optional[str]
    mobile_number: Optional[str]
    email: Optional[str]
    customer_name: Optional[str]
    lead_status: Optional[str]