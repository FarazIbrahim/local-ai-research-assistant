import streamlit as st
import time

from core.research_engine import research, list_reports, delete_report
from pipeline.executor import run_pipeline


# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Deep Research Clone",
    page_icon="🔎",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS
# ==========================================

st.markdown("""

<style>

/* 
========================================
GLOBAL
======================================== */

html, body, [class*="css"] {
    font-family: "Inter", sans-serif;
}

.stApp {
    background:
        radial-gradient(circle at top left, #111827 0%, #0B1120 40%, #020617 100%);
    color: #F9FAFB;
}

/* 
========================================
MAIN CONTAINER
======================================== */

.block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    padding-left: 4rem;
    padding-right: 4rem;
}

/* 
========================================
HEADINGS
======================================== */

h1 {
    font-size: 3.4rem !important;
    font-weight: 800 !important;
    letter-spacing: -2px;
    color: white;
}

h2, h3 {
    color: #F3F4F6;
}

p, li {
    font-size: 16px;
    line-height: 1.9;
    color: #D1D5DB;
}

/* 
========================================
TEXT AREA
======================================== */

textarea {
    background-color: rgba(17, 24, 39, 0.75) !important;
    color: white !important;
    border-radius: 18px !important;
    border: 1px solid rgba(255,255,255,0.08) !important;
    backdrop-filter: blur(10px);
    font-size: 16px !important;
    padding: 1rem !important;
}

/* 
========================================
BUTTONS
======================================== */

.stButton button {
    width: 100%;
    border-radius: 16px;
    height: 3.4em;
    font-size: 16px;
    font-weight: 700;
    background: linear-gradient(135deg, #2563EB, #4F46E5);
    color: white;
    border: none;
    transition: all 0.25s ease;
    box-shadow: 0 8px 30px rgba(37,99,235,0.35);
}

.stButton button:hover {
    transform: translateY(-3px);
    box-shadow: 0 12px 35px rgba(79,70,229,0.45);
}

/* 
========================================
SIDEBAR
======================================== */

section[data-testid="stSidebar"] {
    background: rgba(15, 23, 42, 0.75);
    backdrop-filter: blur(16px);
    border-right: 1px solid rgba(255,255,255,0.08);
    position: sticky;
    top: 0;
    height: 100vh;
}

/* 
========================================
METRIC CARDS
======================================== */

[data-testid="metric-container"] {
    background: rgba(17, 24, 39, 0.65);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 20px;
    border-radius: 20px;
    backdrop-filter: blur(14px);
    transition: all 0.25s ease;
}

[data-testid="metric-container"]:hover {
    transform: translateY(-4px);
    border: 1px solid rgba(99,102,241,0.4);
    box-shadow: 0 12px 40px rgba(0,0,0,0.35);
}

/* 
========================================
REPORT CONTAINER
======================================== */

.report-container {
    background: rgba(17, 24, 39, 0.72);
    border-radius: 24px;
    padding: 2rem;
    border: 1px solid rgba(255,255,255,0.08);
    backdrop-filter: blur(18px);
    box-shadow: 0 10px 40px rgba(0,0,0,0.35);
}

/* 
========================================
SOURCE CARDS
======================================== */

div[data-testid="stVerticalBlock"] div[data-testid="stLinkButton"] {
    background: rgba(17, 24, 39, 0.72);
    border-radius: 18px;
    padding: 1.2rem;
    border: 1px solid rgba(255,255,255,0.06);
    margin-bottom: 1rem;
    transition: all 0.25s ease;
}

div[data-testid="stVerticalBlock"] div[data-testid="stLinkButton"]:hover {
    transform: translateY(-3px);
    border: 1px solid rgba(99,102,241,0.35);
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
}

/* 
========================================
PROGRESS BAR
======================================== */

.stProgress > div > div > div > div {
    background: linear-gradient(90deg, #3B82F6, #8B5CF6);
}

/* 
========================================
DOWNLOAD BUTTON
======================================== */

.stDownloadButton button {
    border-radius: 14px;
    background: linear-gradient(135deg, #059669, #10B981);
    color: white;
    border: none;
    font-weight: 700;
    transition: all 0.25s ease;
}

.stDownloadButton button:hover {
    transform: translateY(-2px);
    box-shadow: 0 10px 25px rgba(16,185,129,0.35);
}

/* 
========================================
HIDE STREAMLIT ANIMATION
======================================== */

[data-testid="stStatusWidget"] {
    visibility: hidden;
    height: 0%;
    position: fixed;
}

/* 
========================================
FLOATING GLOW
========================================
*/

.glow {
    position: fixed;
    width: 500px;
    height: 500px;
    background: radial-gradient(circle, rgba(79,70,229,0.18), transparent 70%);
    filter: blur(80px);
    z-index: -1;
    animation: floatGlow 10s ease-in-out infinite;
}

.glow-2 {
    top: 20%;
    right: -100px;
}

.glow-1 {
    top: -100px;
    left: -100px;
}

@keyframes floatGlow {
    0% {
        transform: translateY(0px);
    }
    50% {
        transform: translateY(40px);
    }
    100% {
        transform: translateY(0px);
    }
}

</style>

""", unsafe_allow_html=True)

st.markdown(
    """
    <div class="glow glow-1"></div>
    <div class="glow glow-2"></div>
    """,
    unsafe_allow_html=True
)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.title("⚙️ Settings")

    st.markdown("---")

    st.markdown("### Model")

    st.info("Using Ollama + qwen2.5-coder:1.5b")

    st.markdown("### Search Settings")

    max_sources = st.slider(
        "Number of Sources",
        min_value=1,
        max_value=5,
        value=3
    )

    st.markdown("---")

    st.markdown("### About")

    st.markdown(
        """
        Local AI research assistant powered by:

        - Ollama
        - Qwen2.5-Coder
        - DuckDuckGo Search
        - Streamlit
        """
    )

    st.markdown("---")
    st.markdown("### 🧾 Saved Reports")


    reports = list_reports()

    if not reports:
        st.info("No reports found.")
    else:

        for report in reports:

            col1, col2 = st.columns([3, 1])

            with col1:
                st.text(report.name)

            with col2:
                if st.button("🗑", key=report.name):

                    delete_report(report)

                    st.rerun()


# ==========================================
# MAIN HEADER
# ==========================================

st.markdown(
    """
    # 🔎 Deep Research Clone

    ### Autonomous AI Research Assistant

    Generate professional research reports using:

    - 🌐 Web Search
    - 📄 Intelligent Web Scraping
    - 🧠 Local LLM Reasoning
    - 📑 PDF Report Generation

    Built fully with local AI models for privacy-focused research workflows.

    ---
    """
)

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.metric("LLM", "Qwen2.5-Coder")

with col2:
    st.metric("Search Engine", "DuckDuckGo")

with col3:
    st.metric("Architecture", "Local AI")


# ==========================================
# INPUT SECTION
# ==========================================

query = st.text_area(
    "Research Topic",
    placeholder="Example: Impact of AI on software engineering...",
    height=140
)


# ==========================================
# RESEARCH BUTTON
# ==========================================

if st.button("🕵️ Generate Research Report"):

    if not query.strip():

        st.warning("Please enter a research topic.")

    else:

        # Progress section
        progress = st.progress(0)

        status = st.empty()


        # ==================================
        # STEP 1 — SEARCH + SCRAPE
        # ==================================

        status.info("🔍 Searching and collecting sources...")

        progress.progress(25)
        
        with st.spinner("Researching sources..."):

            data = run_pipeline(query, max_sources)


        # ==================================
        # STEP 2 — GENERATE REPORT
        # ==================================

        thinking_messages = [
            "👁️‍🗨️ Analyzing sources...",
            "📚 Extracting insights...",
            "🧩 Synthesizing research...",
            "✍️ Writing professional report..."
        ]

        for msg in thinking_messages:
            status.info(msg)
            time.sleep(0.8)

        progress.progress(70)

        with st.spinner("Generating AI report..."):
            
            result, pdf_path = research(query, data)

        progress.progress(100)

        status.success("✅ Research completed!")


        # ==================================
        # REPORT OUTPUT
        # ==================================

        st.subheader("📄 Research Report")

        report_container = st.container()

        with report_container:

            st.markdown(f"# {query}")

            report_placeholder = st.empty()

            streamed_text = ""

            lines = result["report"].split("\n")

            for line in lines:

                streamed_text += line + "\n"

                report_placeholder.markdown(streamed_text + "▌")
                time.sleep(0.03)
            
            report_placeholder.markdown(streamed_text)

        with open(pdf_path, "rb") as f:
            st.download_button(
                label="📥 Download PDF Report",
                data=f,
                file_name="research_report.pdf",
                mime="application/pdf"
            )


        # ==================================
        # SOURCES SECTION
        # ==================================

        st.markdown("---")

        st.subheader("🌐 Sources Used")

        for idx, item in enumerate(data, start=1):

            with st.container():

                st.markdown(f"### {idx}. {item['title']}")

                st.link_button(
                    "🔗 Visit Source",
                    item["url"]
                )

        st.markdown("---")

        st.markdown(
            """
            <div style='text-align: center; color: gray; padding-top: 10px;'>
            Deep Research Clone&nbsp;&nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;&nbsp;Built with Local AI&nbsp;&nbsp;&nbsp;&nbsp;•&nbsp;&nbsp;&nbsp;&nbsp;Project by Faraz Ibrahim
            </div>
            """,
            unsafe_allow_html=True
        )
