def build_final_prompt(query, data):

    context = ""

    for item in data:

        if item["text"]:

            context += f"""

            SOURCE TITLE:
            {item['title']}

            SOURCE CONTENT:
            {item['text'][:800]}
            """

    return f"""
    You are a professional senior research analyst.

    Research Topic:
    {query}

    You must create a professional research report.

    Use ONLY the provided sources.

    ========================
    SOURCES
    ========================

    {context}

    ========================
    REPORT FORMAT
    ========================

    ## Summary

    ## Key Findings

    ## Detailed Analysis

    ## Real-World Implications

    ## Conclusion

    ========================
    RULES
    ========================

    - Each section must contain UNIQUE information that does not appear in other sections
    - Never repeat the same explanation, sentence, or idea across different sections
    - Summary = only overview (NO details, NO examples)
    - Key Findings = ONLY bullet points, no explanations
    - Detailed Analysis = deep explanations ONLY (no repeating Key Findings)
    - Real-World Implications = ONLY industry/business impact
    - Conclusion = ONLY synthesis, no new ideas
    - Keep paragraphs short and non-redundant
    - Avoid filler sentences or generic statements
    - Write clearly and directly
    - Use Markdown headings only as given
    - Use bullet points where required
    - Bold important terms using **markdown bold**
    - Finish all sentences completely
    - Do not write the same concept under different headings even if phrased differently.
    """
