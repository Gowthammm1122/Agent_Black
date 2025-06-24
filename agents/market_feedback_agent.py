from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import Document
from langchain.chains import RetrievalQA

# ✅ Sample feedback corpus (replace with real data if needed)
sample_feedback = [
    "Students find it hard to generate empathetic purpose statements.",
    "Tools often ignore real-world feature gaps.",
    "Milestone-based planners lack adaptive feedback systems.",
    "Most tools are overly technical for non-CS students.",
    "Competitors don’t visualize process flow effectively."
]

# ✅ Step 1: Initialize vector database with feedback documents
def init_chroma():
    persist_dir = "./chroma_db"
    embedding = OpenAIEmbeddings()
    docs = [Document(page_content=feedback) for feedback in sample_feedback]
    vectordb = Chroma.from_documents(docs, embedding, persist_directory=persist_dir)
    return vectordb

# ✅ Step 2: RAG-enabled Market Feedback Analyzer Agent
def market_feedback_agent(context: str, purpose: str) -> str:
    vectordb = init_chroma()
    retriever = vectordb.as_retriever()
    llm = ChatOpenAI(model="gpt-3.5-turbo")

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )

    query = (
        f"Given the purpose '{purpose}' in the context of '{context}', "
        f"what are potential areas of improvement based on user pain points? "
        f"Use insights from similar tools and user complaints."
    )

    result = qa_chain.run(query)
    return result
