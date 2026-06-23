import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
import os
from dotenv import load_dotenv

load_dotenv()

# LangSmith tracking
if os.getenv("LANGCHAIN_API_KEY"):
    os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
    os.environ["LANGCHAIN_TRACING_V2"] = "true"
    os.environ["LANGCHAIN_PROJECT"] = "Q&A CHATBOT"

st.set_page_config(
    page_title="Groq AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #f8fafc 0%, #eef2ff 100%);
}

.hero-card {
    background: linear-gradient(135deg, #4f46e5 0%, #7c3aed 100%);
    padding: 35px;
    border-radius: 22px;
    color: white;
    margin-bottom: 25px;
    box-shadow: 0 12px 30px rgba(79, 70, 229, 0.25);
}

.hero-title {
    font-size: 44px;
    font-weight: 800;
    margin-bottom: 8px;
}

.hero-subtitle {
    font-size: 18px;
    opacity: 0.9;
}

.metric-card {
    background: white;
    padding: 18px;
    border-radius: 16px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.08);
    text-align: center;
    border: 1px solid #e5e7eb;
}

.response-box {
    background: white;
    padding: 24px;
    border-radius: 18px;
    border-left: 6px solid #4f46e5;
    box-shadow: 0 8px 22px rgba(0,0,0,0.08);
    line-height: 1.7;
    font-size: 16px;
}

.footer {
    text-align: center;
    color: #6b7280;
    margin-top: 35px;
    font-size: 14px;
}
</style>
""", unsafe_allow_html=True)

prompt = ChatPromptTemplate.from_messages([
    ("system", """You are an advanced AI assistant designed to provide professional, accurate, and insightful responses.

        Instructions:
        - Answer directly and accurately.
        - Structure responses with clear headings.
        - Use bullet points and numbered steps when appropriate.
        - Provide practical examples whenever useful.
        - For technical topics, explain both the concept and its real-world application.
        - For comparisons, provide pros, cons, and key differences.
        - Keep responses informative, professional, and easy to read.
        - Adapt the level of detail based on the complexity of the question."""),
    ("user", "Question: {question}")
])

def generate_response(question, api_key, selected_model, temperature, max_tokens):
    llm = ChatGroq(
        groq_api_key=api_key,
        model=selected_model,
        temperature=temperature,
        max_tokens=max_tokens
    )

    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser

    return chain.invoke({"question": question})

with st.sidebar:
    st.title("⚙️ Settings")

    api_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="Enter your Groq API key"
    )

    selected_model = st.selectbox(
        "Select Model",
        [
            "llama-3.1-8b-instant",
            "llama-3.3-70b-versatile",
            "qwen/qwen3-32b"
        ]
    )

    temperature = st.slider(
        "Creativity",
        min_value=0.0,
        max_value=1.0,
        value=0.7
    )

    max_tokens = st.slider(
        "Max Response Length",
        min_value=50,
        max_value=500,
        value=200
    )

    st.divider()
    st.caption("Built with Streamlit, LangChain, and Groq.")

st.markdown("""
<div class="hero-card">
    <div class="hero-title">🤖 Groq AI Assistant</div>
    <div class="hero-subtitle">
        A clean, fast, and professional AI chatbot powered by LangChain and Groq.
    </div>
</div>
""", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="metric-card">
        <h3>⚡ Fast</h3>
        <p>Low-latency Groq inference</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <h3>🧠 Smart</h3>
        <p>Multiple model choices</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <h3>🛠️ Tracked</h3>
        <p>LangSmith monitoring enabled</p>
    </div>
    """, unsafe_allow_html=True)

st.divider()

user_input = st.text_area(
    "Ask your question",
    placeholder="Example: Explain LangChain agents in simple terms...",
    height=130
)

submit = st.button("Generate Response", type="primary")

if submit:
    if not api_key:
        st.warning("Please enter your Groq API key in the sidebar.")
    elif not user_input.strip():
        st.warning("Please enter a question.")
    else:
        with st.spinner("Generating response..."):
            try:
                response = generate_response(
                    user_input,
                    api_key,
                    selected_model,
                    temperature,
                    max_tokens
                )

                st.subheader("Response")
                st.markdown(
                    f'<div class="response-box">{response}</div>',
                    unsafe_allow_html=True
                )

            except Exception as e:
                st.error(f"Error: {e}")
else:
    st.info("Enter a question and click Generate Response.")

st.markdown("""
<div class="footer">
    Built with Streamlit · LangChain · Groq
</div>
""", unsafe_allow_html=True)