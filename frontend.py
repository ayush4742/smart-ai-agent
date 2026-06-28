import streamlit as st
import requests

# ------------------------------------
# Page Config
# ------------------------------------

st.set_page_config(
    page_title="LangGraph AI Agent",
    page_icon="🤖",
    layout="centered"
)

# ------------------------------------
# CSS
# ------------------------------------

st.markdown("""
<style>

html, body, [class*="css"]{
    background-color:#0f172a;
}

.main{
    background:#0f172a;
}

.block-container{
    max-width:900px;
    padding-top:2rem;
}

h1{
    text-align:center;
    font-size:3.2rem;
    font-weight:800;
    background:linear-gradient(90deg,#38bdf8,#818cf8,#ec4899);
    -webkit-background-clip:text;
    -webkit-text-fill-color:transparent;
}

.stTextArea textarea{
    border-radius:12px;
}

div[data-baseweb="select"]{
    border-radius:12px;
}

.stButton>button{
    width:100%;
    height:52px;
    border-radius:12px;
    background:linear-gradient(90deg,#2563eb,#7c3aed);
    color:white;
    font-size:18px;
    font-weight:bold;
    border:none;
}

.stButton>button:hover{
    transform:scale(1.02);
    transition:0.2s;
}

.response{
    background:#111827;
    color:white;
    padding:20px;
    border-radius:15px;
    border-left:6px solid #38bdf8;
    font-size:17px;
    line-height:1.7;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ------------------------------------
# Title
# ------------------------------------

st.markdown("<h1>🤖 LangGraph AI Agent</h1>", unsafe_allow_html=True)

st.caption("Powered by FastAPI • LangGraph • OpenAI • Groq • Tavily")

st.divider()

# ------------------------------------
# Models
# ------------------------------------

MODEL_NAMES_GROQ = [
    "llama-3.3-70b-versatile",
    "mixtral-8x7b-32768"
]

MODEL_NAMES_OPENAI = [
    "gpt-4o-mini"
]

# ------------------------------------
# Inputs
# ------------------------------------

system_prompt = st.text_area(
    "🎯 Define your AI Agent",
    placeholder="Example: Act as a Machine Learning Interviewer...",
    height=90
)

col1, col2 = st.columns(2)

with col1:
    provider = st.radio(
        "Provider",
        ["Groq", "OpenAI"]
    )

with col2:

    if provider == "Groq":
        selected_model = st.selectbox(
            "Groq Model",
            MODEL_NAMES_GROQ
        )

    else:
        selected_model = st.selectbox(
            "OpenAI Model",
            MODEL_NAMES_OPENAI
        )

allow_web_search = st.toggle(
    "🌍 Enable Web Search",
    value=True
)

user_query = st.text_area(
    "💬 Ask Anything",
    placeholder="Example: Explain LangGraph with examples...",
    height=180
)

# ------------------------------------
# Backend URL
# ------------------------------------

API_URL = "https://smart-ai-agent-api.onrender.com/chat"

# ------------------------------------
# Button
# ------------------------------------

if st.button("🚀 Ask Agent"):

    if not user_query.strip():
        st.warning("Please enter a query.")
        st.stop()

    payload = {
        "model_name": selected_model,
        "model_provider": provider,
        "system_prompt": system_prompt,
        "messages": [user_query],
        "allow_search": allow_web_search
    }

    try:

        with st.spinner("🤖 AI is Thinking..."):

            response = requests.post(
                API_URL,
                json=payload,
                timeout=120
            )

        if response.status_code == 200:

            result = response.json()

            st.success("✅ Response Generated")

            if isinstance(result, dict):

                if "response" in result:

                    answer = result["response"]

                elif "answer" in result:

                    answer = result["answer"]

                elif "output" in result:

                    answer = result["output"]

                else:

                    answer = str(result)

            else:

                answer = str(result)

            st.markdown(
                f"""
<div class="response">
{answer}
</div>
""",
                unsafe_allow_html=True
            )

        else:

            st.error(f"Error {response.status_code}")

            st.code(response.text)

    except Exception as e:

        st.error(str(e))

# ------------------------------------
# Footer
# ------------------------------------

st.markdown(
"""
<div class="footer">
Made with ❤️ using Streamlit • LangGraph • FastAPI
</div>
""",
unsafe_allow_html=True
)