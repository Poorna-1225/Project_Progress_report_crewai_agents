from src.create_crew_agents_tasks import crew
from IPython.display import Markdown

result = crew.kickoff()


markdown  = result.raw
Markdown(markdown)