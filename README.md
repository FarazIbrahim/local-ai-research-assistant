# 🤖 Local AI Research Assistant

> Autonomous AI research pipeline powered by local LLMs, real-time web search, intelligent content extraction, and structured report generation.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Streamlit-Frontend-red?style=for-the-badge&logo=streamlit" />
  <img src="https://img.shields.io/badge/Ollama-Local%20LLM-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Qwen2.5-Coder-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Architecture-Modular-purple?style=for-the-badge" />
</p>

---

## 🎥 Project Showcase

Watch the complete project walkthrough on LinkedIn:

👉 **[View Demo Video](https://www.linkedin.com/posts/farazibrahim_ai-python-llm-activity-7460121223109423104-poDo?utm_source=share&utm_medium=member_desktop&rcm=ACoAAGgrcewBR49qNy-3GgPvd8xr_kJkQblG56U)**

📑 **[View Sample PDF Report](reports/sample_research_report.pdf)**

---

# 📖 Overview

Local AI Research Assistant is a fully local autonomous research system that performs:

* Web search
* Content extraction
* Context construction
* AI-powered report generation
* PDF report export

The system combines retrieval pipelines, prompt engineering, and local LLM inference to generate structured research reports directly on your machine using Ollama.

Unlike cloud-dependent AI applications, this project focuses on:

* privacy-first workflows
* local inference
* modular AI architecture
* autonomous report synthesis

---

# 🪄 Features

## 🔍 Autonomous Research Pipeline

End-to-end automated workflow:

```text
User Query
   ↓
Web Search
   ↓
Content Scraping
   ↓
Context Construction
   ↓
Local LLM Analysis
   ↓
Structured Research Report
   ↓
PDF Export
```

---

## 🧠 Local LLM Inference

Powered by:

* Ollama
* Qwen2.5-Coder:1.5b

Advantages:

* Fully local execution
* No external AI APIs
* Privacy-focused architecture
* Offline-capable workflow
* Lightweight deployment

---

## 📄 Structured Research Generation

The system generates professional research reports containing:

* Executive Summary
* Key Findings
* Detailed Analysis
* Real-World Implications
* Conclusion

Formatting includes:

* Markdown heading hierarchy
* Bullet point synthesis
* Highlighted concepts
* Clean paragraph segmentation

---

## 📑 PDF Report Export

Reports are automatically exported into formatted PDF documents containing:

* Research topic
* Structured sections
* Readable typography
* Source references
* Downloadable output

---

## 🎨 Streamlit Interface

Features include:

* Modern glassmorphism-inspired UI
* Animated progress states
* Streaming report rendering
* Saved reports management
* Interactive source browsing
* Responsive wide-layout design

---

# ⚙️ Technical Stack

| Category       | Technology            |
| -------------- | --------------------- |
| Frontend       | Streamlit             |
| LLM Runtime    | Ollama                |
| Language Model | Qwen2.5-Coder         |
| Search Engine  | DuckDuckGo (`ddgs`)   |
| Web Scraping   | newspaper3k           |
| PDF Generation | ReportLab             |
| HTML Parsing   | BeautifulSoup4 + lxml |
| Language       | Python                |

---

# 🏗️ System Architecture

## High-Level Architecture

```text
┌─────────────────────┐
│  Streamlit Frontend │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│  Research Pipeline  │
└──────────┬──────────┘
           │

   ┌───────┼────────┐
   ▼       ▼        ▼

Search   Scraper   Prompt Builder
  │         │            │
  ▼         ▼            ▼

DuckDuckGo  newspaper3k  Context Assembly
                     │
                     ▼
              Ollama + Qwen2.5
                     │
                     ▼
              Research Report
                     │
                     ▼
               PDF Generation
```

---

# 🔄 Pipeline Breakdown

## 1. Web Search Layer

Relevant sources are retrieved using DuckDuckGo search.

```python
results = search(query)
```

Returns:

* source titles
* URLs
* snippets

---

## 2. Content Extraction Layer

Each article is parsed using `newspaper3k`.

```python
article.download()
article.parse()
```

Extracted content is cleaned and optimized before prompt construction.

---

## 3. Context Construction

Research context is dynamically assembled into a structured LLM prompt.

The system injects:

* source titles
* extracted article content
* formatting instructions
* research constraints

This improves report consistency and output quality.

---

## 4. Local LLM Reasoning

The report is generated using:

```python
ollama.chat(
    model="qwen2.5-coder:1.5b"
)
```

The pipeline includes:

* deterministic temperature settings
* structured prompting
* continuation handling for incomplete generations

---

## 5. PDF Rendering

Generated reports are converted into downloadable PDF documents using ReportLab.

Features include:

* heading formatting
* bullet rendering
* typography styling
* source references

---

# 🚀 Quick Start

## 1. Clone Repository

```bash
git clone https://github.com/FarazIbrahim/local-ai-research-assistant.git

cd local-ai-research-assistant
```

---

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 3. Install Ollama

Download Ollama:

[https://ollama.com](https://ollama.com)

Pull the model:

```bash
ollama pull qwen2.5-coder:1.5b
```

---

## 4. Run Application

```bash
streamlit run app.py
```

---

# 📂 Project Structure

```text
local-ai-research-assistant/
│
├── core/
│   ├── prompt_builder.py
│   └── research_engine.py
│
├── pipeline/
│   └── executor.py
│
├── services/
│   ├── local_llm.py
│   ├── search.py
│   └── scraper.py
│
├── tests/
│   ├── test_pipeline.py
│   └── test_search.py
│
├── utils/
│   └── format_output.py
│
├── reports/
│   └── sample_research_report.pdf
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🧪 Example Workflow

## Input

```text
Impact of AI on software engineering
```

---

## Output

Generated report includes:

* AI-assisted development trends
* Productivity implications
* Engineering workflow transformation
* Industry impact analysis
* Future outlook predictions

Plus:

* downloadable PDF report
* referenced research sources

---

# 🏗️ Engineering Highlights

## Modular Architecture

The system separates concerns into:

* services
* pipeline
* research engine
* UI layer
* utilities

Benefits:

* maintainability
* extensibility
* scalability
* easier testing

---

## Prompt Engineering

The prompt system enforces:

* report structure consistency
* concise outputs
* professional tone
* source-grounded responses

---

## Fault Handling

The pipeline includes:

* incomplete response detection
* automatic continuation generation
* fallback completion logic
* scraper exception handling

---

# ⚠️ Current Limitations

* Depends on public web source quality
* No semantic reranking layer yet
* Sequential scraping pipeline
* No citation-level grounding
* Local inference speed depends on hardware

---

# 🔮 Future Improvements

Planned enhancements:

* RAG-based retrieval memory
* Hybrid OpenAI/Ollama switching
* Async scraping pipeline
* Vector database integration
* Multi-agent research orchestration
* Source credibility scoring
* Dockerized deployment
* Streaming token generation

---

# 👤 Author

## Faraz Ibrahim

AI Engineering • Data Science

Focused on:

* AI systems engineering
* LLM applications
* autonomous workflows
* local AI infrastructure
* applied machine learning systems

---

# 📌 Notes

This project explores how autonomous AI research systems can be built using local-first LLM infrastructure, retrieval pipelines, structured prompting, and modular orchestration without relying on external paid APIs.
