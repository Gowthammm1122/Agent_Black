from langgraph.graph import StateGraph, END
from pipeline_nodes import (
    context_node,
    purpose_node,
    flow_node,
    diagram_node,
    feedback_node,
    market_feedback_node
)
from pydantic import BaseModel

# Define schema using Pydantic
class AgenticState(BaseModel):
    title: str
    goals: str
    feedback: str
    context: str | None = None
    purpose: str | None = None
    flow: str | None = None
    diagram: str | None = None
    feedback_out: str | None = None
    market_insights: str | None = None  # NEW

def build_graph():
    builder = StateGraph(state_schema=AgenticState)

    builder.add_node("Context", context_node)
    builder.add_node("Purpose", purpose_node)
    builder.add_node("Flow", flow_node)
    builder.add_node("Diagram", diagram_node)
    builder.add_node("Feedback", feedback_node)
    builder.add_node("MarketFeedback", market_feedback_node)  # NEW

    builder.set_entry_point("Context")
    builder.add_edge("Context", "Purpose")
    builder.add_edge("Purpose", "Flow")
    builder.add_edge("Flow", "Diagram")
    builder.add_edge("Diagram", "Feedback")
    builder.add_edge("Feedback", "MarketFeedback")  # NEW
    builder.add_edge("MarketFeedback", END)

    return builder.compile()
