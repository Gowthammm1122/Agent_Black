from dotenv import load_dotenv
from pipeline_graph import build_graph

# Load environment variables
load_dotenv()

# Build the agent pipeline
graph = build_graph()

# Sample inputs
inputs = {
    "title": "AI-based Project Assistant",
    "goals": "Help students clearly define and plan their academic projects using AI agents",
    "feedback": "Many students struggle with scoping their project and lack milestone clarity"
}

# Run the pipeline
result = graph.invoke(inputs)

# Print outputs
print("\n--- 🧠 Agentic AI Pipeline Output ---")
print(f"\n📘 CONTEXT:\n{result.get('context', 'No output')}")
print(f"\n🎯 PURPOSE:\n{result.get('purpose', 'No output')}")
print(f"\n🛠️ PROCESS FLOW:\n{result.get('flow', 'No output')}")
print(f"\n📊 MERMAID DIAGRAM:\n{result.get('diagram', 'No output')}")
print(f"\n🧪 FEEDBACK:\n{result.get('feedback_out', 'No output')}")
print(f"\n🔍 MARKET INSIGHTS (RAG):\n{result.get('market_insights', 'No output')}")
