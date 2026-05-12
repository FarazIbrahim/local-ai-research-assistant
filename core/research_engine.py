import re
import hashlib
from pathlib import Path

from core.prompt_builder import build_final_prompt
from services.local_llm import generate
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet


def clean_filename(text: str) -> str:

    text = re.sub(r'[<>:"/\\|?*]', '', text)
    text = text.strip().replace(" ", "_")
    text = re.sub(r'_+', '_', text)

    return text[:80]


def stable_filename(query: str) -> str:

    clean = clean_filename(query.lower())

    hash_suffix = hashlib.md5(query.encode("utf-8")).hexdigest()[:6]

    return f"{clean}_{hash_suffix}"


def save_report(query: str, full_report: dict):

    reports_dir = Path("reports")
    reports_dir.mkdir(exist_ok=True)

    filename = stable_filename(query)
    filepath = reports_dir / f"{filename}.pdf"

    doc = SimpleDocTemplate(str(filepath))
    styles = getSampleStyleSheet()

    content = []

    
    # TITLE

    content.append(
        Paragraph(
            "AI Research Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 12))

    content.append(
        Paragraph(
            f"Topic: {query}",
            styles["Heading2"]
        )
    )

    content.append(Spacer(1, 18))

    # REPORT
    report_lines = full_report["report"].split("\n")

    for line in report_lines:

        line = line.strip()

        line = re.sub(r"\*\*(.*?)\*\*", r"<b>\1</b>", line)

        if not line:
            continue

        # HEADINGS
        if line.startswith("### "):
            heading = line.replace("### ", "")
            content.append(Paragraph(f"<b>{heading}</b>", styles["Heading3"]))
            content.append(Spacer(1, 8))

        elif line.startswith("## "):
            heading = line.replace("## ", "")
            content.append(Paragraph(f"<b>{heading}</b>", styles["Heading2"]))
            content.append(Spacer(1, 10))

        # BULLETS
        elif line.startswith("- "):

            bullet = line.replace("- ", "• ")

            content.append(
                Paragraph(bullet, styles["BodyText"])
            )

            content.append(Spacer(1, 6))

        # NUMBERED LISTS
        elif line[:2].isdigit():

            content.append(
                Paragraph(
                line,
                styles["BodyText"]
                )
            )

            content.append(Spacer(1, 6))

        # NORMAL TEXT
        else:

            content.append(
                Paragraph(line, styles["BodyText"])
            )

            content.append(Spacer(1, 8))

    # SOURCES
    content.append(Paragraph("<b>Sources:</b>", styles["Heading2"]))

    for i, src in enumerate(full_report["sources"], 1):
        text = f"{i}. {src['title']}<br/>{src['url']}"
        content.append(Paragraph(text, styles["Normal"]))
        content.append(Spacer(1, 8))

    doc.build(content)

    return filepath


def looks_incomplete(text: str) -> bool:

    text = text.strip()

    if len(text) < 200:
        return True

    if not text.endswith((".", "!", "?")):
        return True

    return False


def research(query: str, data):

    prompt = build_final_prompt(query, data)

    result = generate(prompt)

    full_report = {
        "query": query,
        "report": result,
        "sources": data
    }

    # ==========================================
    # CONTINUATION ONLY IF INCOMPLETE
    # ==========================================

    if looks_incomplete(full_report["report"]):

        continuation_prompt = f"""
    The following research report was cut off mid-writing.

    Continue ONLY from the exact last sentence.

    STRICT RULES:
    - Do NOT repeat headings
    - Do NOT restart sections
    - Do NOT write another conclusion if one already exists
    - Continue naturally from the cutoff point
    - Write only the missing continuation

    REPORT:
    {full_report["report"]}
    """

        continuation = generate(continuation_prompt)

        full_report["report"] += "\n" + continuation

    # ==========================================
    # FINAL SAFETY VALIDATION
    # ==========================================

    if looks_incomplete(full_report["report"]):

        final_fix_prompt = f"""
    Finish the ending of this report naturally.

    Only write the missing ending or conclusion.
    Do not repeat the report.

    Report:
    {full_report["report"]}
    """

        fix_response = generate(final_fix_prompt)

        full_report["report"] += "\n" + fix_response

    # Final Export Only
    pdf_path = save_report(query, full_report)

    return full_report, pdf_path


def list_reports():

    reports_dir = Path("reports")

    if not reports_dir.exists():
        return []

    return list(reports_dir.glob("*.pdf"))


def delete_report(file_path):

    try:
        Path(file_path).unlink()
        return True
    except Exception:
        return False
