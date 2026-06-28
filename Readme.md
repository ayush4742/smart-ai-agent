# 🤖 Smart AI Agent using LangGraph, FastAPI & Streamlit

> A production-ready AI chatbot built using **LangGraph**, **FastAPI**, and **Streamlit** with support for **OpenAI**, **Groq**, and **Tavily Web Search**.

---

## 🚀 Live Demo

### 🌐 Frontend

> https://smart-ai-agent.streamlit.app

### ⚡ Backend API

> https://smart-ai-agent-api.onrender.com/docs

---

# 📌 Overview

Smart AI Agent is an intelligent chatbot that allows users to interact with multiple Large Language Models through a clean web interface.

Users can:

* 🤖 Choose between OpenAI and Groq models
* 🌍 Enable or disable real-time web search
* 🎯 Define custom system prompts
* 💬 Ask any question
* ⚡ Receive AI-generated responses instantly

The backend is built using **FastAPI** and **LangGraph**, while the frontend is developed with **Streamlit**.

---

# ✨ Features

* ✅ Multiple AI Providers

  * OpenAI GPT-4o Mini
  * Groq Llama 3.3 70B
  * Groq Mixtral 8x7B

* ✅ LangGraph ReAct Agent

* ✅ Optional Web Search using Tavily

* ✅ Custom System Prompt

* ✅ FastAPI REST API

* ✅ Streamlit User Interface

* ✅ Cloud Deployment

* ✅ Environment Variable Support

* ✅ Clean Modular Code

---

# 🛠 Tech Stack

| Category      | Technologies             |
| ------------- | ------------------------ |
| Language      | Python                   |
| Frontend      | Streamlit                |
| Backend       | FastAPI                  |
| AI Framework  | LangGraph                |
| LLM Framework | LangChain                |
| OpenAI Models | GPT-4o Mini              |
| Groq Models   | Llama 3.3 70B, Mixtral   |
| Search Tool   | Tavily Search API        |
| Deployment    | Render + Streamlit Cloud |

---

# 📂 Project Structure

```
smart-ai-agent
│
├── ai_agent.py
├── backend.py
├── frontend.py
├── requirements.txt
├── runtime.txt
└── README.md
```

---

# ⚙️ System Architecture

```
                User
                  │
                  ▼
         Streamlit Frontend
                  │
                  ▼
           FastAPI Backend
                  │
                  ▼
        LangGraph ReAct Agent
         │               │
         ▼               ▼
     OpenAI           Groq
         │
         ▼
     Tavily Search (Optional)
```

---

# 🚀 Installation

## Clone Repository

```bash
git clone https://github.com/ayush4742/smart-ai-agent.git

cd smart-ai-agent
```

---

## Create Virtual Environment

### Using Conda

```bash
conda create -n aiagent python=3.11

conda activate aiagent
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Variables

Create a **.env** file.

```
OPENAI_API_KEY=your_openai_key

GROQ_API_KEY=your_groq_key

TAVILY_API_KEY=your_tavily_key
```

---

# ▶️ Run Backend

```bash
python backend.py
```

Backend URL

```
http://127.0.0.1:9999
```

Swagger API

```
http://127.0.0.1:9999/docs
```

---

# ▶️ Run Frontend

```bash
streamlit run frontend.py
```

---

# 🧠 Supported Models

## OpenAI

* GPT-4o Mini

## Groq

* Llama 3.3 70B Versatile
* Mixtral 8x7B

---

# 🌍 Web Search

The application supports optional real-time web search using **Tavily Search API**.

Users can enable or disable web search from the UI.

---

# 📡 API Endpoint

### POST

```
/chat
```

Example Request

```json
{
  "model_name":"gpt-4o-mini",
  "model_provider":"OpenAI",
  "system_prompt":"You are a helpful AI assistant",
  "messages":["Explain LangGraph"],
  "allow_search":true
}
```

---


# 🎯 Future Improvements

* Chat History
* Conversation Memory
* PDF Question Answering (RAG)
* Voice Input
* Text-to-Speech
* Authentication
* Image Understanding
* Multi-Agent Workflow
* Streaming Responses

---

# 💼 Skills Demonstrated

* Generative AI
* LangGraph
* LangChain
* Prompt Engineering
* REST API Development
* FastAPI
* Streamlit
* LLM Integration
* OpenAI API
* Groq API
* Tavily Search API
* Cloud Deployment
* Environment Variables
* Git & GitHub

---

# 👨‍💻 Author

**Ayush Kumar**

B.Tech CSE (Data Science)

GitHub:
https://github.com/ayush4742

LinkedIn:
(https://www.linkedin.com/in/ayush-kumar-2ba43b289/)

---

# ⭐ If you found this project useful, consider giving it a Star!
