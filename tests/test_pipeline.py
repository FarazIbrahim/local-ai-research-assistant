from core.research_engine import research
from utils.format_output import pretty_print
from pipeline.executor import run_pipeline

query = "impact of AI on software engineering"

print("\n")
print("=" * 80)
print(f"🔍 Research Query: {query}")
print("=" * 80)

data = run_pipeline(query)

result, pdf = research(query, data)

pretty_print(result)


