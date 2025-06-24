from agents.context_reader import context_reader
from agents.purpose_generator import generate_purpose_statement
from agents.flow_planner import generate_project_flow
from agents.diagram_generator import generate_mermaid_diagram
from agents.feedback_agent import generate_feedback
from agents.market_feedback_agent import market_feedback_agent  # NEW

def context_node(state):
    return {"context": context_reader(state.title, state.goals, state.feedback)}

def purpose_node(state):
    return {"purpose": generate_purpose_statement(state.context)}

def flow_node(state):
    return {"flow": generate_project_flow(state.purpose)}

def diagram_node(state):
    return {"diagram": generate_mermaid_diagram(state.flow)}

def feedback_node(state):
    return {"feedback_out": generate_feedback(state.context, state.purpose, state.flow)}

def market_feedback_node(state):  # NEW
    return {"market_insights": market_feedback_agent(state.context, state.purpose)}
