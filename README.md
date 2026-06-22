# Q&AChatbot

# 🤖 Groq AI Assistant

A modern AI-powered Question & Answer chatbot built using **Streamlit**, **LangChain**, and **Groq LLMs**. This application provides a clean and interactive user interface that allows users to ask questions and receive intelligent responses powered by state-of-the-art Large Language Models.

---

## 🚀 Overview

Groq AI Assistant is a lightweight yet powerful chatbot application designed to demonstrate how modern Generative AI applications can be built using LangChain orchestration and Groq's ultra-fast inference infrastructure.

The application features a professional user interface, configurable model settings, customizable response generation parameters, and optional LangSmith tracing for observability and debugging.

---

## ✨ Features

### 🧠 Multiple LLM Support

Choose from multiple Groq-hosted models:

* Llama 3.1 8B Instant
* Llama 3.3 70B Versatile
* Qwen 3 32B

### ⚡ High-Speed Responses

Leverages Groq's low-latency inference engine for fast response generation.

### 🎨 Professional UI

Built with Streamlit and enhanced using custom CSS styling for a modern and visually appealing experience.

### 🔧 Configurable Parameters

Customize:

* Model Selection
* Temperature
* Maximum Response Length

### 📊 LangSmith Integration

Supports LangSmith tracing for:

* Prompt inspection
* Chain debugging
* Execution monitoring
* Performance analysis

### 🛡️ Error Handling

Includes validation and exception handling to improve user experience and application reliability.

---

## 🏗️ Architecture

```text
User Input
    │
    ▼
Streamlit UI
    │
    ▼
Prompt Template
    │
    ▼
LangChain Chain
    │
    ▼
Groq LLM
    │
    ▼
Output Parser
    │
    ▼
Response Display
```

---

## 🛠️ Tech Stack

### Frontend

* Streamlit

### LLM Framework

* LangChain

### Models

* Groq Hosted LLMs

  * Llama 3.1
  * Llama 3.3
  * Qwen 3

### Observability

* LangSmith

### Environment Management

* Python Dotenv

---

## 📂 Project Structure

```text
groq-ai-assistant/
│
├── app.py
├── .env
├── requirements.txt
├── README.md
│
└── screenshots/
    └── app-preview.png
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/groq-ai-assistant.git

cd groq-ai-assistant
```

### Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
```

The Groq API Key is entered securely through the application's sidebar.

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

After startup, open:

```text
http://localhost:8501
```

---

## 📸 Application Features

### Sidebar Configuration

* Enter Groq API Key
* Select LLM Model
* Adjust Temperature
* Configure Maximum Tokens

### Main Workspace

* User Question Input
* AI Generated Response
* Loading Indicators
* Error Notifications

---

## 📈 LangSmith Monitoring

To enable tracing:

1. Create a LangSmith account.
2. Generate an API key.
3. Add the API key to the `.env` file.
4. Run the application.

LangSmith will automatically capture:

* Prompts
* Model Calls
* Chain Executions
* Token Usage
* Response Metadata

---

## 💡 Example Questions

```text
Explain LangChain Agents in simple terms.

What is Retrieval Augmented Generation (RAG)?

How does a ReAct Agent work?

Explain Vector Databases with examples.

What are the differences between Llama and Qwen models?
```

---

## 🎯 Future Enhancements

Potential future improvements include:

* Conversation Memory
* Chat History
* Streaming Responses
* Document Upload & Q&A
* Retrieval-Augmented Generation (RAG)
* Multi-Agent Workflows
* Authentication & User Sessions
* Voice Input & Output
* Docker Deployment
* Cloud Deployment

---

## 🤝 Contributing

Contributions, feature requests, and improvements are welcome.

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Submit a pull request

---

## 📜 License

This project is intended for educational and demonstration purposes.

---

## 👨‍💻 Author

**Josin Samuel**

AI / ML Engineer | Generative AI Enthusiast

Built using Streamlit, LangChain, Groq, and LangSmith.
